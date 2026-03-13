import json
import random

from flask import render_template, request, jsonify, redirect, url_for, session, flash

from database import get_db, login_required, usuario_logado
from .game_data import (
    ATRIBUTOS, ATRIBUTOS_LABELS, ATRIBUTOS_ABREV,
    RACAS, CLASSES, ALINHAMENTOS, PERICIAS, XP_TABLE, SLOTS_MAGIA,
    calcular_modificador, calcular_bonus_proficiencia, calcular_pv_nivel,
    calcular_cd_magia, calcular_bonus_ataque_magia, calcular_percepcao_passiva,
)
from . import bp

SISTEMA = "dnd"


# ─── CÁLCULO DA FICHA ──────────────────────────────────────────────────────────

def calcular_ficha(dados):
    """Recalcula todos os valores derivados da ficha de D&D 5e."""
    attrs = dados.get("atributos", {})
    nivel = dados.get("nivel", 1)
    classe_key = dados.get("classe", "guerreiro")
    classe = CLASSES.get(classe_key, {})

    mods = {a: calcular_modificador(attrs.get(a, 10)) for a in ATRIBUTOS}
    bonus_prof = calcular_bonus_proficiencia(nivel)

    pv_max = calcular_pv_nivel(classe_key, nivel, mods["constituicao"])

    # CA base: depende da armadura equipada
    armadura_tipo = dados.get("armadura_tipo", "nenhuma")
    ca = _calcular_ca(armadura_tipo, mods["destreza"], dados.get("escudo", False))

    # Saves com proficiência
    saves_prof = set(classe.get("saves", []))
    saves = {}
    for attr in ATRIBUTOS:
        saves[attr] = mods[attr] + (bonus_prof if attr in saves_prof else 0)

    # Perícias com proficiência e expertise
    pericias_prof = set(dados.get("pericias_treinadas", []))
    pericias_expertise = set(dados.get("pericias_expertise", []))
    pericias_calc = {}
    for nome, attr in PERICIAS.items():
        base = mods.get(attr, 0)
        if nome in pericias_expertise:
            bonus = bonus_prof * 2
        elif nome in pericias_prof:
            bonus = bonus_prof
        else:
            bonus = 0
        pericias_calc[nome] = {
            "atributo": attr,
            "proficiente": nome in pericias_prof,
            "expertise": nome in pericias_expertise,
            "base_mod": base,
            "bonus": bonus,
            "total": base + bonus,
        }

    # Magia
    atributo_magia = classe.get("atributo_magia", "inteligencia") if classe.get("magias") else None
    mod_magia = mods.get(atributo_magia, 0) if atributo_magia else 0
    slots = SLOTS_MAGIA.get(nivel, [0] * 9) if classe.get("magias") else []

    dados["calculado"] = {
        "pv_max": pv_max,
        "ca": ca,
        "bonus_prof": bonus_prof,
        "iniciativa": mods["destreza"],
        "velocidade": RACAS.get(dados.get("raca", "humano"), {}).get("velocidade", 9),
        "percepcao_passiva": calcular_percepcao_passiva(
            mods["sabedoria"],
            "Percepção" in pericias_prof,
            bonus_prof
        ),
        "saves": saves,
        "saves_prof": list(saves_prof),
        "pericias": pericias_calc,
        "cd_magia": calcular_cd_magia(attrs.get(atributo_magia, 10), bonus_prof) if atributo_magia else None,
        "bonus_ataque_magia": calcular_bonus_ataque_magia(attrs.get(atributo_magia, 10), bonus_prof) if atributo_magia else None,
        "slots_magia": slots,
        "atributo_magia": atributo_magia,
        "xp_proximo": XP_TABLE.get(nivel + 1, {}).get("xp", None),
        **{f"mod_{a}": v for a, v in mods.items()},
    }
    return dados


def _calcular_ca(armadura_tipo, mod_dex, escudo):
    tabela = {
        "nenhuma":  10 + mod_dex,
        "leve":     11 + mod_dex,
        "media":    14 + min(mod_dex, 2),
        "pesada":   18,
        "natural":  10 + mod_dex,
    }
    ca = tabela.get(armadura_tipo, 10 + mod_dex)
    return ca + (2 if escudo else 0)


# ─── HELPERS ──────────────────────────────────────────────────────────────────

def _get_personagem(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return None, None
    return row, json.loads(row["dados"])


def _save_personagem(pid, dados):
    with get_db() as conn:
        conn.execute(
            "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
            (dados.get("nome", "?"), json.dumps(dados, ensure_ascii=False), pid)
        )
        conn.commit()


# ─── LISTAGEM ─────────────────────────────────────────────────────────────────

@bp.route("/")
@login_required
def index():
    uid = session["usuario_id"]
    with get_db() as conn:
        rows = conn.execute(
            "SELECT id, nome, dados, mesa_id, criado_em FROM personagens WHERE usuario_id=? AND sistema=? ORDER BY atualizado_em DESC",
            (uid, SISTEMA)
        ).fetchall()
    lista = []
    for p in rows:
        dados = json.loads(p["dados"])
        lista.append({
            "id": p["id"],
            "nome": p["nome"],
            "mesa_id": p["mesa_id"],
            "nivel": dados.get("nivel", 1),
            "classe": CLASSES.get(dados.get("classe", ""), {}).get("nome", "?"),
            "raca": RACAS.get(dados.get("raca", ""), {}).get("nome", "?"),
            "criado_em": p["criado_em"],
        })
    return render_template("dnd/index.html", personagens=lista, usuario=usuario_logado())


# ─── CRIAÇÃO ──────────────────────────────────────────────────────────────────

@bp.route("/criar")
@login_required
def criar():
    return render_template("dnd/criar_passo1.html",
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           racas=RACAS,
                           classes=CLASSES,
                           alinhamentos=ALINHAMENTOS)


@bp.route("/criar/passo2", methods=["POST"])
@login_required
def criar_passo2():
    dados = {
        "nome": request.form.get("nome", ""),
        "jogador": request.form.get("jogador", ""),
        "raca": request.form.get("raca", "humano"),
        "classe": request.form.get("classe", "guerreiro"),
        "alinhamento": request.form.get("alinhamento", "neutro"),
        "antecedente": request.form.get("antecedente", ""),
        "divindade": request.form.get("divindade", ""),
        "atributos": {
            attr: int(request.form.get(f"attr_{attr}", 10))
            for attr in ATRIBUTOS
        },
    }
    session["criacao_dnd"] = dados
    classe = CLASSES.get(dados["classe"], {})
    return render_template("dnd/criar_passo2.html",
                           dados=dados,
                           classe=classe,
                           pericias=PERICIAS,
                           atributos_labels=ATRIBUTOS_LABELS)


@bp.route("/criar/salvar", methods=["POST"])
@login_required
def criar_salvar():
    dados = session.get("criacao_dnd", {})
    if not dados:
        return redirect(url_for("dnd.criar"))

    dados["pericias_treinadas"] = request.form.getlist("pericias")
    dados["pericias_expertise"] = []
    dados["armadura_tipo"] = request.form.get("armadura_tipo", "nenhuma")
    dados["escudo"] = request.form.get("escudo") == "1"
    dados["arma_principal"] = request.form.get("arma_principal", "")
    dados["notas"] = request.form.get("notas", "")
    dados["tracos_personalidade"] = request.form.get("tracos_personalidade", "")
    dados["ideais"] = request.form.get("ideais", "")
    dados["vinculos"] = request.form.get("vinculos", "")
    dados["falhas"] = request.form.get("falhas", "")
    dados["nivel"] = 1
    dados["xp"] = 0
    dados["magias"] = []
    dados["slots_usados"] = [0] * 9

    dados = calcular_ficha(dados)
    dados["pv_atual"] = dados["calculado"]["pv_max"]

    nome = dados.get("nome", "Personagem Sem Nome")
    uid = session["usuario_id"]
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO personagens (nome, dados, usuario_id, sistema) VALUES (?, ?, ?, ?)",
            (nome, json.dumps(dados, ensure_ascii=False), uid, SISTEMA)
        )
        pid = cursor.lastrowid
        conn.commit()

    session.pop("criacao_dnd", None)
    return redirect(url_for("dnd.ver_personagem", pid=pid))


# ─── FICHA ────────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>")
@login_required
def ver_personagem(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("dnd.index"))
    dados = calcular_ficha(dados)
    return render_template("dnd/ficha.html",
                           pid=pid, dados=dados,
                           classe=CLASSES.get(dados.get("classe", ""), {}),
                           raca=RACAS.get(dados.get("raca", ""), {}),
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           atributos_abrev=ATRIBUTOS_ABREV,
                           xp_table=XP_TABLE,
                           slots_magia=SLOTS_MAGIA)


@bp.route("/personagem/<int:pid>/editar", methods=["GET", "POST"])
@login_required
def editar_personagem(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("dnd.index"))

    if request.method == "POST":
        for attr in ATRIBUTOS:
            val = request.form.get(f"attr_{attr}")
            if val:
                dados["atributos"][attr] = int(val)
        dados["nome"] = request.form.get("nome", dados.get("nome", ""))
        dados["jogador"] = request.form.get("jogador", dados.get("jogador", ""))
        dados["alinhamento"] = request.form.get("alinhamento", dados.get("alinhamento", "neutro"))
        dados["antecedente"] = request.form.get("antecedente", dados.get("antecedente", ""))
        dados["divindade"] = request.form.get("divindade", dados.get("divindade", ""))
        dados["notas"] = request.form.get("notas", dados.get("notas", ""))
        dados["tracos_personalidade"] = request.form.get("tracos_personalidade", dados.get("tracos_personalidade", ""))
        dados["xp"] = int(request.form.get("xp", dados.get("xp", 0)))
        dados["pv_atual"] = int(request.form.get("pv_atual", dados.get("pv_atual", 1)))
        dados["armadura_tipo"] = request.form.get("armadura_tipo", dados.get("armadura_tipo", "nenhuma"))
        dados["escudo"] = request.form.get("escudo") == "1"
        dados["pericias_treinadas"] = request.form.getlist("pericias")
        dados = calcular_ficha(dados)
        with get_db() as conn:
            conn.execute(
                "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
                (dados["nome"], json.dumps(dados, ensure_ascii=False), pid)
            )
            conn.commit()
        return redirect(url_for("dnd.ver_personagem", pid=pid))

    dados = calcular_ficha(dados)
    return render_template("dnd/editar.html",
                           pid=pid, dados=dados,
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           pericias=PERICIAS,
                           alinhamentos=ALINHAMENTOS)


@bp.route("/personagem/<int:pid>/atualizar_pv", methods=["POST"])
@login_required
def atualizar_pv(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404
    dados = calcular_ficha(dados)
    novo_pv = request.json.get("pv_atual")
    if novo_pv is not None:
        dados["pv_atual"] = max(0, min(int(novo_pv), dados["calculado"]["pv_max"]))
    novo_xp = request.json.get("xp")
    if novo_xp is not None:
        dados["xp"] = max(0, int(novo_xp))
    _save_personagem(pid, dados)
    return jsonify({"pv_atual": dados["pv_atual"], "xp": dados.get("xp", 0)})


@bp.route("/personagem/<int:pid>/subir_nivel", methods=["POST"])
@login_required
def subir_nivel(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404
    nivel_atual = dados.get("nivel", 1)
    if nivel_atual >= 20:
        return jsonify({"erro": "Nível máximo atingido"}), 400

    novo_nivel = nivel_atual + 1
    dados["nivel"] = novo_nivel
    classe = CLASSES.get(dados.get("classe", "guerreiro"), {})
    mod_con = calcular_modificador(dados["atributos"].get("constituicao", 10))
    dado_vida = classe.get("dado_vida", 8)

    rolar = request.json.get("rolar_pv", False) if request.is_json else False
    ganho_pv = random.randint(1, dado_vida) + mod_con if rolar else classe.get("pv_fixo", 5) + mod_con

    dados = calcular_ficha(dados)
    dados["pv_atual"] = min(dados.get("pv_atual", dados["calculado"]["pv_max"]) + ganho_pv,
                            dados["calculado"]["pv_max"])
    _save_personagem(pid, dados)
    return jsonify({
        "sucesso": True,
        "nivel": novo_nivel,
        "ganho_pv": ganho_pv,
        "pv_max": dados["calculado"]["pv_max"],
        "bonus_prof": dados["calculado"]["bonus_prof"],
        "mensagem": f"Subiu para o nível {novo_nivel}! Ganhou {ganho_pv} PV.",
    })


@bp.route("/personagem/<int:pid>/deletar", methods=["POST"])
@login_required
def deletar_personagem(pid):
    uid = session["usuario_id"]
    with get_db() as conn:
        p = conn.execute("SELECT usuario_id FROM personagens WHERE id=?", (pid,)).fetchone()
        if p and p["usuario_id"] == uid:
            conn.execute("DELETE FROM personagens WHERE id=?", (pid,))
            conn.commit()
    return redirect(url_for("dnd.index"))


# ─── API ──────────────────────────────────────────────────────────────────────

@bp.route("/api/rolar_dados", methods=["POST"])
def rolar_dados():
    data = request.json or {}
    n = int(data.get("n", 1))
    lados = int(data.get("lados", 20))
    vantagem = data.get("vantagem", False)
    desvantagem = data.get("desvantagem", False)

    if (vantagem or desvantagem) and n == 1 and lados == 20:
        r1 = random.randint(1, 20)
        r2 = random.randint(1, 20)
        resultado = max(r1, r2) if vantagem else min(r1, r2)
        tipo = "vantagem" if vantagem else "desvantagem"
        return jsonify({"rolls": [r1, r2], "resultado": resultado, "descricao": f"1d20 com {tipo}: [{r1}, {r2}] = {resultado}"})

    rolls = [random.randint(1, lados) for _ in range(n)]
    resultado = sum(rolls)
    return jsonify({"rolls": rolls, "resultado": resultado, "descricao": f"{n}d{lados}: {rolls} = {resultado}"})


@bp.route("/api/info_classe/<classe_key>")
def info_classe(classe_key):
    classe = CLASSES.get(classe_key)
    if not classe:
        return jsonify({"erro": "Classe não encontrada"}), 404
    return jsonify(classe)


@bp.route("/api/info_raca/<raca_key>")
def info_raca(raca_key):
    raca = RACAS.get(raca_key)
    if not raca:
        return jsonify({"erro": "Raça não encontrada"}), 404
    return jsonify(raca)
