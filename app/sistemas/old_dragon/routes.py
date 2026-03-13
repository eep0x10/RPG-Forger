import json
import random

from flask import render_template, request, jsonify, redirect, url_for, session, flash

from database import get_db, login_required, usuario_logado
from .game_data import (
    ATRIBUTOS, ATRIBUTOS_LABELS, ATRIBUTOS_ABREV,
    RACAS, CLASSES, ALINHAMENTOS, PERICIAS, XP_TABLE, ARMADURAS, ARMAS,
    calcular_modificador, calcular_bonus_proficiencia, calcular_ca, calcular_pv_nivel,
)
from . import bp

SISTEMA = "old_dragon"


# ─── CÁLCULO DA FICHA ──────────────────────────────────────────────────────────

def calcular_ficha(dados):
    """Recalcula todos os valores derivados da ficha de Old Dragon 2e."""
    attrs = dados.get("atributos", {})
    nivel = dados.get("nivel", 1)
    classe_key = dados.get("classe", "guerreiro")

    mod_con = calcular_modificador(attrs.get("constituicao", 10))
    mod_dex = calcular_modificador(attrs.get("destreza", 10))
    mod_for = calcular_modificador(attrs.get("forca", 10))
    mod_int = calcular_modificador(attrs.get("inteligencia", 10))
    mod_sab = calcular_modificador(attrs.get("sabedoria", 10))
    mod_car = calcular_modificador(attrs.get("carisma", 10))

    bonus_prof = calcular_bonus_proficiencia(nivel)
    pv_max = calcular_pv_nivel(classe_key, nivel, mod_con)

    armadura_nome = dados.get("armadura", "Sem Armadura")
    escudo = dados.get("escudo", False)
    ca = calcular_ca(armadura_nome, mod_dex, escudo)

    pericias_treinadas = set(dados.get("pericias_treinadas", []))
    mods_attrs = {
        "forca": mod_for, "destreza": mod_dex, "constituicao": mod_con,
        "inteligencia": mod_int, "sabedoria": mod_sab, "carisma": mod_car,
    }
    pericias_calc = {}
    for nome, attr in PERICIAS.items():
        base_mod = mods_attrs.get(attr, 0)
        proficiente = nome in pericias_treinadas
        total = base_mod + (bonus_prof if proficiente else 0)
        pericias_calc[nome] = {
            "atributo": attr,
            "proficiente": proficiente,
            "base_mod": base_mod,
            "bonus_prof": bonus_prof if proficiente else 0,
            "total": total,
        }

    dados["calculado"] = {
        "pv_max": pv_max,
        "ca": ca,
        "bonus_prof": bonus_prof,
        "iniciativa": mod_dex,
        "percepcao_passiva": 10 + mod_sab + (bonus_prof if "Percepção" in pericias_treinadas else 0),
        "mod_forca": mod_for,
        "mod_destreza": mod_dex,
        "mod_constituicao": mod_con,
        "mod_inteligencia": mod_int,
        "mod_sabedoria": mod_sab,
        "mod_carisma": mod_car,
        "xp_proximo": XP_TABLE.get(nivel + 1, {}).get("xp", None),
        "pericias": pericias_calc,
    }
    return dados


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
        classe = CLASSES.get(dados.get("classe", ""), {})
        raca = RACAS.get(dados.get("raca", ""), {})
        lista.append({
            "id": p["id"],
            "nome": p["nome"],
            "mesa_id": p["mesa_id"],
            "nivel": dados.get("nivel", 1),
            "classe": classe.get("nome", "?"),
            "raca": raca.get("nome", "?"),
            "criado_em": p["criado_em"],
        })
    return render_template("old_dragon/index.html", personagens=lista, usuario=usuario_logado())


# ─── CRIAÇÃO ──────────────────────────────────────────────────────────────────

@bp.route("/criar")
@login_required
def criar():
    return render_template("old_dragon/criar_passo1.html",
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           racas=RACAS,
                           classes=CLASSES)


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
        "atributos": {
            attr: int(request.form.get(f"attr_{attr}", 10))
            for attr in ATRIBUTOS
        },
    }
    session["criacao_od"] = dados
    return render_template("old_dragon/criar_passo2.html",
                           dados=dados,
                           pericias=PERICIAS,
                           classes=CLASSES,
                           armaduras=ARMADURAS,
                           armas=ARMAS,
                           alinhamentos=ALINHAMENTOS)


@bp.route("/criar/salvar", methods=["POST"])
@login_required
def criar_salvar():
    dados = session.get("criacao_od", {})
    if not dados:
        return redirect(url_for("old_dragon.criar"))

    dados["pericias_treinadas"] = request.form.getlist("pericias")
    dados["armadura"] = request.form.get("armadura", "Sem Armadura")
    dados["escudo"] = request.form.get("escudo") == "1"
    dados["arma_principal"] = request.form.get("arma_principal", "")
    dados["arma_secundaria"] = request.form.get("arma_secundaria", "")
    dados["notas"] = request.form.get("notas", "")
    dados["tracos_personalidade"] = request.form.get("tracos_personalidade", "")
    dados["ideais"] = request.form.get("ideais", "")
    dados["vinculos"] = request.form.get("vinculos", "")
    dados["falhas"] = request.form.get("falhas", "")
    dados["nivel"] = 1
    dados["xp"] = 0

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

    session.pop("criacao_od", None)
    return redirect(url_for("old_dragon.ver_personagem", pid=pid))


# ─── FICHA ────────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>")
@login_required
def ver_personagem(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("old_dragon.index"))
    dados = calcular_ficha(dados)
    classe = CLASSES.get(dados.get("classe", ""), {})
    raca = RACAS.get(dados.get("raca", ""), {})
    return render_template("old_dragon/ficha.html",
                           pid=pid, dados=dados,
                           classe=classe, raca=raca,
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           atributos_abrev=ATRIBUTOS_ABREV,
                           armaduras=ARMADURAS,
                           armas=ARMAS,
                           xp_table=XP_TABLE)


@bp.route("/personagem/<int:pid>/editar", methods=["GET", "POST"])
@login_required
def editar_personagem(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("old_dragon.index"))

    if request.method == "POST":
        for attr in ATRIBUTOS:
            val = request.form.get(f"attr_{attr}")
            if val:
                dados["atributos"][attr] = int(val)
        dados["nome"] = request.form.get("nome", dados.get("nome", ""))
        dados["jogador"] = request.form.get("jogador", dados.get("jogador", ""))
        dados["alinhamento"] = request.form.get("alinhamento", dados.get("alinhamento", "neutro"))
        dados["antecedente"] = request.form.get("antecedente", dados.get("antecedente", ""))
        dados["notas"] = request.form.get("notas", dados.get("notas", ""))
        dados["tracos_personalidade"] = request.form.get("tracos_personalidade", dados.get("tracos_personalidade", ""))
        dados["ideais"] = request.form.get("ideais", dados.get("ideais", ""))
        dados["vinculos"] = request.form.get("vinculos", dados.get("vinculos", ""))
        dados["falhas"] = request.form.get("falhas", dados.get("falhas", ""))
        dados["xp"] = int(request.form.get("xp", dados.get("xp", 0)))
        dados["pv_atual"] = int(request.form.get("pv_atual", dados.get("pv_atual", 1)))
        dados["armadura"] = request.form.get("armadura", dados.get("armadura", "Sem Armadura"))
        dados["escudo"] = request.form.get("escudo") == "1"
        dados["pericias_treinadas"] = request.form.getlist("pericias")
        dados = calcular_ficha(dados)
        with get_db() as conn:
            conn.execute(
                "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
                (dados["nome"], json.dumps(dados, ensure_ascii=False), pid)
            )
            conn.commit()
        return redirect(url_for("old_dragon.ver_personagem", pid=pid))

    dados = calcular_ficha(dados)
    return render_template("old_dragon/editar.html",
                           pid=pid, dados=dados,
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           pericias=PERICIAS,
                           armaduras=ARMADURAS,
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
    ganho_pv = random.randint(1, dado_vida) + mod_con if rolar else classe.get("pv_fixo", 4) + mod_con

    dados["pv_ganho_historico"] = dados.get("pv_ganho_historico", [])
    dados["pv_ganho_historico"].append({"nivel": novo_nivel, "ganho": ganho_pv})
    dados = calcular_ficha(dados)
    dados["pv_atual"] = min(dados.get("pv_atual", dados["calculado"]["pv_max"]) + ganho_pv,
                            dados["calculado"]["pv_max"])
    _save_personagem(pid, dados)
    return jsonify({
        "sucesso": True,
        "nivel": novo_nivel,
        "ganho_pv": ganho_pv,
        "pv_max": dados["calculado"]["pv_max"],
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
    return redirect(url_for("old_dragon.index"))


# ─── API ──────────────────────────────────────────────────────────────────────

@bp.route("/api/rolar_dados", methods=["POST"])
def rolar_dados():
    data = request.json or {}
    n = int(data.get("n", 1))
    lados = int(data.get("lados", 20))
    rolls = [random.randint(1, lados) for _ in range(n)]
    resultado = sum(rolls)
    return jsonify({"rolls": rolls, "resultado": resultado, "descricao": f"{n}d{lados}: {rolls} = {resultado}"})
