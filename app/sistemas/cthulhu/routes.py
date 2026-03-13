import json
import random

from flask import render_template, request, jsonify, redirect, url_for, session, flash

from database import get_db, login_required, usuario_logado
from .game_data import (
    CARACTERISTICAS, CARACTERISTICAS_LABELS, CARACTERISTICAS_ABREV, CARACTERISTICAS_ROLAGEM,
    OCUPACOES, PERICIAS, ERAS, TRANSTORNOS,
    calcular_pv, calcular_pm, calcular_san_inicial, calcular_san_maxima,
    calcular_movimento, calcular_bonus_dano, calcular_construcao, nivel_pericia,
)
from . import bp

SISTEMA = "cthulhu"


# ─── CÁLCULO DA FICHA ──────────────────────────────────────────────────────────

def calcular_ficha(dados):
    """Recalcula valores derivados da ficha de Call of Cthulhu 7e."""
    chars = dados.get("caracteristicas", {})

    for_val = chars.get("for", 50)
    con_val = chars.get("con", 50)
    tam_val = chars.get("tam", 65)
    des_val = chars.get("des", 50)
    apa_val = chars.get("apa", 50)
    edu_val = chars.get("edu", 60)
    int_val = chars.get("int", 60)
    pod_val = chars.get("pod", 50)

    pv_max = calcular_pv(con_val, tam_val)
    pm_max = calcular_pm(pod_val)
    san_inicial = calcular_san_inicial(pod_val)
    conhecimento_mitos = dados.get("conhecimento_mitos", 0)
    san_maxima = calcular_san_maxima(conhecimento_mitos)

    movimento = calcular_movimento(for_val, des_val, tam_val)
    bonus_dano = calcular_bonus_dano(for_val, tam_val)
    construcao = calcular_construcao(for_val, tam_val)

    # Calcular valores de perícias com base, hard e extreme
    pericias_valores = dados.get("pericias_valores", {})
    pericias_calc = {}
    for nome, info in PERICIAS.items():
        # Valor base da perícia
        if info.get("formula"):
            if nome == "Esquiva":
                base = des_val // 2
            elif nome == "Língua Nativa":
                base = edu_val
            elif nome == "Crédito":
                ocupacao = OCUPACOES.get(dados.get("ocupacao", ""), {})
                base = ocupacao.get("credito_minimo", 10)
            else:
                base = info.get("base", 1)
        else:
            base = info.get("base", 1)

        valor_atual = pericias_valores.get(nome, base)
        niveis = nivel_pericia(valor_atual)
        pericias_calc[nome] = {
            "base": base,
            "valor": valor_atual,
            "regular": niveis["regular"],
            "hard": niveis["hard"],
            "extreme": niveis["extreme"],
            "caracteristica": info.get("char", "edu"),
            "categoria": info.get("categoria", "geral"),
        }

    dados["calculado"] = {
        "pv_max": pv_max,
        "pm_max": pm_max,
        "san_inicial": san_inicial,
        "san_maxima": san_maxima,
        "movimento": movimento,
        "bonus_dano": bonus_dano,
        "construcao": construcao,
        "pericias": pericias_calc,
        # Metade e 1/5 das características para testes
        "for_metade": for_val // 2,  "for_quinto": for_val // 5,
        "con_metade": con_val // 2,  "con_quinto": con_val // 5,
        "tam_metade": tam_val // 2,  "tam_quinto": tam_val // 5,
        "des_metade": des_val // 2,  "des_quinto": des_val // 5,
        "apa_metade": apa_val // 2,  "apa_quinto": apa_val // 5,
        "edu_metade": edu_val // 2,  "edu_quinto": edu_val // 5,
        "int_metade": int_val // 2,  "int_quinto": int_val // 5,
        "pod_metade": pod_val // 2,  "pod_quinto": pod_val // 5,
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
        ocupacao = OCUPACOES.get(dados.get("ocupacao", ""), {})
        era = ERAS.get(dados.get("era", ""), {})
        san = dados.get("san_atual", dados.get("calculado", {}).get("san_inicial", "?"))
        lista.append({
            "id": p["id"],
            "nome": p["nome"],
            "mesa_id": p["mesa_id"],
            "ocupacao": ocupacao.get("nome", "?"),
            "era": era.get("nome", "?"),
            "san": san,
            "criado_em": p["criado_em"],
        })
    return render_template("cthulhu/index.html", personagens=lista, usuario=usuario_logado())


# ─── CRIAÇÃO ──────────────────────────────────────────────────────────────────

@bp.route("/criar")
@login_required
def criar():
    return render_template("cthulhu/criar_passo1.html",
                           caracteristicas=CARACTERISTICAS,
                           caracteristicas_labels=CARACTERISTICAS_LABELS,
                           caracteristicas_rolagem=CARACTERISTICAS_ROLAGEM,
                           ocupacoes=OCUPACOES,
                           eras=ERAS)


@bp.route("/criar/passo2", methods=["POST"])
@login_required
def criar_passo2():
    dados = {
        "nome": request.form.get("nome", ""),
        "jogador": request.form.get("jogador", ""),
        "ocupacao": request.form.get("ocupacao", "estudante"),
        "era": request.form.get("era", "1920s"),
        "idade": int(request.form.get("idade", 25)),
        "sexo": request.form.get("sexo", ""),
        "residencia": request.form.get("residencia", ""),
        "naturalidade": request.form.get("naturalidade", ""),
        "caracteristicas": {
            char: int(request.form.get(f"char_{char}", 50))
            for char in CARACTERISTICAS
        },
    }
    # Calcular pontos de perícia disponíveis
    chars = dados["caracteristicas"]
    ocupacao_info = OCUPACOES.get(dados["ocupacao"], {})
    dados["pontos_ocupacao_disponiveis"] = chars["edu"] * 4  # simplificado
    dados["pontos_interesses_disponiveis"] = chars["int"] * 2

    session["criacao_coc"] = dados
    return render_template("cthulhu/criar_passo2.html",
                           dados=dados,
                           ocupacao=ocupacao_info,
                           pericias=PERICIAS,
                           caracteristicas_labels=CARACTERISTICAS_LABELS)


@bp.route("/criar/salvar", methods=["POST"])
@login_required
def criar_salvar():
    dados = session.get("criacao_coc", {})
    if not dados:
        return redirect(url_for("cthulhu.criar"))

    # Valores das perícias (pontos distribuídos)
    pericias_valores = {}
    for nome in PERICIAS:
        val = request.form.get(f"pericia_{nome}")
        if val:
            try:
                pericias_valores[nome] = max(0, min(99, int(val)))
            except ValueError:
                pass
    dados["pericias_valores"] = pericias_valores
    dados["equipamentos"] = request.form.get("equipamentos", "")
    dados["notas"] = request.form.get("notas", "")
    dados["aparencia"] = request.form.get("aparencia", "")
    dados["tracos"] = request.form.get("tracos", "")
    dados["ideologia"] = request.form.get("ideologia", "")
    dados["pessoas_importantes"] = request.form.get("pessoas_importantes", "")
    dados["lugares_significativos"] = request.form.get("lugares_significativos", "")
    dados["tesouros"] = request.form.get("tesouros", "")
    dados["conhecimento_mitos"] = 0
    dados["transtornos"] = []
    dados["cicatrizes"] = []

    dados = calcular_ficha(dados)
    dados["pv_atual"] = dados["calculado"]["pv_max"]
    dados["pm_atual"] = dados["calculado"]["pm_max"]
    dados["san_atual"] = dados["calculado"]["san_inicial"]

    nome = dados.get("nome", "Investigador Sem Nome")
    uid = session["usuario_id"]
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO personagens (nome, dados, usuario_id, sistema) VALUES (?, ?, ?, ?)",
            (nome, json.dumps(dados, ensure_ascii=False), uid, SISTEMA)
        )
        pid = cursor.lastrowid
        conn.commit()

    session.pop("criacao_coc", None)
    return redirect(url_for("cthulhu.ver_personagem", pid=pid))


# ─── FICHA ────────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>")
@login_required
def ver_personagem(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("cthulhu.index"))
    dados = calcular_ficha(dados)
    return render_template("cthulhu/ficha.html",
                           pid=pid, dados=dados,
                           ocupacao=OCUPACOES.get(dados.get("ocupacao", ""), {}),
                           era=ERAS.get(dados.get("era", ""), {}),
                           caracteristicas=CARACTERISTICAS,
                           caracteristicas_labels=CARACTERISTICAS_LABELS,
                           caracteristicas_abrev=CARACTERISTICAS_ABREV,
                           pericias=PERICIAS,
                           transtornos=TRANSTORNOS)


@bp.route("/personagem/<int:pid>/editar", methods=["GET", "POST"])
@login_required
def editar_personagem(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("cthulhu.index"))

    if request.method == "POST":
        for char in CARACTERISTICAS:
            val = request.form.get(f"char_{char}")
            if val:
                dados["caracteristicas"][char] = max(1, min(99, int(val)))
        dados["nome"] = request.form.get("nome", dados.get("nome", ""))
        dados["jogador"] = request.form.get("jogador", dados.get("jogador", ""))
        dados["ocupacao"] = request.form.get("ocupacao", dados.get("ocupacao", ""))
        dados["idade"] = int(request.form.get("idade", dados.get("idade", 25)))
        dados["notas"] = request.form.get("notas", dados.get("notas", ""))
        dados["pv_atual"] = max(0, int(request.form.get("pv_atual", dados.get("pv_atual", 1))))
        dados["pm_atual"] = max(0, int(request.form.get("pm_atual", dados.get("pm_atual", 0))))
        dados["san_atual"] = max(0, int(request.form.get("san_atual", dados.get("san_atual", 0))))
        dados["conhecimento_mitos"] = max(0, int(request.form.get("conhecimento_mitos", dados.get("conhecimento_mitos", 0))))

        # Perícias editadas
        pericias_valores = dados.get("pericias_valores", {})
        for nome in PERICIAS:
            val = request.form.get(f"pericia_{nome}")
            if val:
                try:
                    pericias_valores[nome] = max(0, min(99, int(val)))
                except ValueError:
                    pass
        dados["pericias_valores"] = pericias_valores
        dados = calcular_ficha(dados)

        with get_db() as conn:
            conn.execute(
                "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
                (dados["nome"], json.dumps(dados, ensure_ascii=False), pid)
            )
            conn.commit()
        return redirect(url_for("cthulhu.ver_personagem", pid=pid))

    dados = calcular_ficha(dados)
    return render_template("cthulhu/editar.html",
                           pid=pid, dados=dados,
                           caracteristicas=CARACTERISTICAS,
                           caracteristicas_labels=CARACTERISTICAS_LABELS,
                           pericias=PERICIAS,
                           ocupacoes=OCUPACOES)


@bp.route("/personagem/<int:pid>/atualizar_recursos", methods=["POST"])
@login_required
def atualizar_recursos(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404
    dados = calcular_ficha(dados)
    data = request.json or {}

    novo_pv = data.get("pv_atual")
    if novo_pv is not None:
        dados["pv_atual"] = max(0, min(int(novo_pv), dados["calculado"]["pv_max"]))

    novo_pm = data.get("pm_atual")
    if novo_pm is not None:
        dados["pm_atual"] = max(0, min(int(novo_pm), dados["calculado"]["pm_max"]))

    nova_san = data.get("san_atual")
    if nova_san is not None:
        dados["san_atual"] = max(0, min(int(nova_san), dados["calculado"]["san_maxima"]))

    novos_mitos = data.get("conhecimento_mitos")
    if novos_mitos is not None:
        dados["conhecimento_mitos"] = max(0, min(int(novos_mitos), 99))
        dados = calcular_ficha(dados)  # san_maxima muda com mitos

    _save_personagem(pid, dados)
    return jsonify({
        "pv_atual": dados["pv_atual"],
        "pm_atual": dados.get("pm_atual", 0),
        "san_atual": dados.get("san_atual", 0),
        "san_maxima": dados["calculado"]["san_maxima"],
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
    return redirect(url_for("cthulhu.index"))


# ─── API ──────────────────────────────────────────────────────────────────────

@bp.route("/api/rolar_dados", methods=["POST"])
def rolar_dados():
    data = request.json or {}
    tipo = data.get("tipo", "percentual")

    if tipo == "percentual":
        # Rolagem percentual para perícias (1d100)
        resultado = random.randint(1, 100)
        return jsonify({"resultado": resultado, "descricao": f"1d100 = {resultado}"})
    else:
        n = int(data.get("n", 1))
        lados = int(data.get("lados", 6))
        rolls = [random.randint(1, lados) for _ in range(n)]
        resultado = sum(rolls)
        return jsonify({"rolls": rolls, "resultado": resultado, "descricao": f"{n}d{lados}: {rolls} = {resultado}"})


@bp.route("/api/testar_pericia", methods=["POST"])
def testar_pericia():
    """Realiza um teste de perícia e informa resultado (regular/difícil/extremo/falha/fumble)."""
    data = request.json or {}
    valor = int(data.get("valor", 50))
    rolagem = random.randint(1, 100)
    niveis = nivel_pericia(valor)

    if rolagem == 1:
        nivel_resultado = "critico"
        descricao = "Crítico! (rolou 1)"
    elif rolagem <= niveis["extreme"]:
        nivel_resultado = "extremo"
        descricao = f"Sucesso Extremo ({rolagem} ≤ {niveis['extreme']})"
    elif rolagem <= niveis["hard"]:
        nivel_resultado = "dificil"
        descricao = f"Sucesso Difícil ({rolagem} ≤ {niveis['hard']})"
    elif rolagem <= niveis["regular"]:
        nivel_resultado = "regular"
        descricao = f"Sucesso Regular ({rolagem} ≤ {niveis['regular']})"
    elif rolagem >= 96 and valor < 50:
        nivel_resultado = "fumble"
        descricao = f"Fumble! ({rolagem})"
    elif rolagem == 100:
        nivel_resultado = "fumble"
        descricao = f"Fumble! (rolou 100)"
    else:
        nivel_resultado = "falha"
        descricao = f"Falha ({rolagem} > {niveis['regular']})"

    return jsonify({
        "rolagem": rolagem,
        "nivel": nivel_resultado,
        "descricao": descricao,
        "niveis": niveis,
    })
