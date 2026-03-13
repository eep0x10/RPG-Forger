import json
import random

from flask import render_template, request, jsonify, redirect, url_for, session, flash

from database import get_db, login_required, usuario_logado
from .game_data import (
    ORIGENS, ESPECIALIZACOES, PERICIAS, PERICIAS_TREINO, TESTES_RESISTENCIA,
    ARMAS_INICIAIS, UNIFORMES, KITS, ATRIBUTOS, ATRIBUTOS_LABELS,
    XP_TABLE, calcular_modificador, calcular_grau, calcular_pv,
    calcular_pe, calcular_bonus_treinamento, VALORES_FIXOS, POINT_BUY_COSTS,
    INVOCACAO_GRADES, INVOCACAO_DANO, INVOCACAO_AREA, INVOCACAO_AUXILIO,
    INVOCACAO_CARAC, GRADE_NOMES, GRADE_ORDEM, get_grades_acesso, calcular_invocacao,
    TECNICA_DANO_ALVO_TR, TECNICA_DANO_ALVO_ATAQUE, TECNICA_DANO_AREA_TR,
    TECNICA_ALCANCE_M, TECNICA_AREA_M,
    TECNICA_AUX_CA, TECNICA_AUX_RD, TECNICA_AUX_BONUS, TECNICA_AUX_MOVIMENTO,
    TECNICA_AUX_DANO_ADD, TECNICA_AUX_CURA_UNICO, TECNICA_AUX_CURA_AREA, TECNICA_AUX_CD,
    TECNICA_PASSIVA_RED_PE, TECNICA_MAXIMA_REF,
    TECNICA_TIPOS, TECNICA_CONJURACAO, TECNICA_DURACAO,
    CONDICOES_POR_FORCA, CONDICAO_CUSTO_DADOS, CONDICAO_DURACAO_PADRAO,
    LIBERACAO_MAXIMA_CUSTO,
    APTIDOES_DOMINIO, APTIDOES_ADICIONAIS, DOMINIO_TIPOS,
    INVOCACAO_ACOES_LISTA, INVOCACAO_CARAC_LISTA,
    ARMAS_DADOS, ESCUDOS_DADOS, ATTR_ABREV,
)
from . import bp

SISTEMA = "jujutsu"


# ─── CÁLCULO DA FICHA ──────────────────────────────────────────────────────────

def calcular_ficha(dados):
    """Recalcula todos os valores derivados da ficha"""
    attrs = dados.get("atributos", {})
    nivel = dados.get("nivel", 1)
    spec_key = dados.get("especializacao", "lutador")

    mod_con = calcular_modificador(attrs.get("constituicao", 10))
    mod_dex = calcular_modificador(attrs.get("destreza", 10))

    spec = ESPECIALIZACOES.get(spec_key, {})
    atrib_chave = dados.get("atributo_chave", spec.get("atributos_chave", ["forca"])[0] if spec.get("atributos_chave") else "forca")
    mod_chave = calcular_modificador(attrs.get(atrib_chave, 10))

    bt = calcular_bonus_treinamento(nivel)
    pv_max = calcular_pv(spec_key, nivel, mod_con)
    pe_max = calcular_pe(spec_key, nivel, mod_chave)

    origem = dados.get("origem", "inato")
    if origem == "herdado_kamo":
        pv_max += nivel
        if nivel >= 10:
            pv_max += mod_con

    uniforme_nome = dados.get("uniforme", "Uniforme Comum")
    uni_data = next((u for u in UNIFORMES if u["nome"] == uniforme_nome), UNIFORMES[0])
    defesa_base = 10 + mod_dex + (nivel // 2) + uni_data["bonus_defesa"]

    if spec_key == "restringido":
        mod_forca = calcular_modificador(attrs.get("forca", 10))
        mod_const = calcular_modificador(attrs.get("constituicao", 10))
        bonus_restringido = min(max(mod_forca, mod_const), nivel)
        defesa_base += bonus_restringido

    penalidade_uniforme = uni_data["penalidade"]
    bonus_sob_medida = uni_data["key"] == "sob_medida"

    deslocamento = 9
    if origem == "restringido":
        deslocamento += 3

    iniciativa = mod_dex

    pericias_raw = dados.get("pericias_treinadas", {})
    if isinstance(pericias_raw, list):
        pericias_dict = {p: "treinado" for p in pericias_raw}
    else:
        pericias_dict = pericias_raw

    mods_attrs = {
        "forca":        calcular_modificador(attrs.get("forca", 10)),
        "destreza":     mod_dex,
        "constituicao": mod_con,
        "inteligencia": calcular_modificador(attrs.get("inteligencia", 10)),
        "sabedoria":    calcular_modificador(attrs.get("sabedoria", 10)),
        "presenca":     calcular_modificador(attrs.get("presenca", 10)),
    }
    pericias_calc = {}
    for nome, attr in PERICIAS.items():
        nivel_pericia = pericias_dict.get(nome)
        bonus = 0 if not nivel_pericia else (bt if nivel_pericia == "treinado" else bt + bt // 2)
        total = mods_attrs[attr] + bonus
        pericias_calc[nome] = {
            "atributo": attr,
            "nivel": nivel_pericia,
            "mod_attr": mods_attrs[attr],
            "bonus": bonus,
            "total": total,
        }

    bonus_percepcao = pericias_calc["Percepção"]["bonus"]
    atencao = 10 + calcular_modificador(attrs.get("sabedoria", 10)) + bonus_percepcao
    integridade_alma = pv_max
    pe_label = "Pontos de Estamina" if spec_key == "restringido" else "Pontos de Energia"

    dados["calculado"] = {
        "pv_max": pv_max,
        "pe_max": pe_max,
        "pe_label": pe_label,
        "defesa": defesa_base,
        "penalidade_uniforme": penalidade_uniforme,
        "bonus_sob_medida": bonus_sob_medida,
        "iniciativa": iniciativa,
        "atencao": atencao,
        "deslocamento": deslocamento,
        "integridade_alma": integridade_alma,
        "bonus_treinamento": bt,
        "grau": calcular_grau(nivel),
        "mod_forca": mods_attrs["forca"],
        "mod_destreza": mod_dex,
        "mod_constituicao": mod_con,
        "mod_inteligencia": mods_attrs["inteligencia"],
        "mod_sabedoria": mods_attrs["sabedoria"],
        "mod_presenca": mods_attrs["presenca"],
        "xp_proximo": XP_TABLE.get(nivel + 1, {}).get("xp", None),
        "xp_atual_nivel": XP_TABLE.get(nivel, {}).get("xp", 0),
        "pericias": pericias_calc,
    }
    return dados


# ─── HELPERS INTERNOS ──────────────────────────────────────────────────────────

def _get_personagem(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return None, None
    dados = json.loads(row["dados"])
    return row, dados


def _save_personagem(pid, dados):
    with get_db() as conn:
        conn.execute(
            "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
            (dados.get("nome", "?"), json.dumps(dados, ensure_ascii=False), pid)
        )
        conn.commit()


# ─── LISTAGEM DE PERSONAGENS ────────────────────────────────────────────────────

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
            "grau": calcular_grau(dados.get("nivel", 1)),
            "especializacao": ESPECIALIZACOES.get(dados.get("especializacao", ""), {}).get("nome", "?"),
            "origem": ORIGENS.get(dados.get("origem", ""), {}).get("nome", "?"),
            "criado_em": p["criado_em"],
        })
    return render_template("jujutsu/index.html", personagens=lista, usuario=usuario_logado())


# ─── CRIAÇÃO DE PERSONAGEM (WIZARD) ────────────────────────────────────────────

@bp.route("/criar")
@login_required
def criar():
    return render_template("jujutsu/criar_passo1.html",
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           valores_fixos=VALORES_FIXOS)


@bp.route("/criar/passo2", methods=["POST"])
@login_required
def criar_passo2():
    dados = {
        "nome": request.form.get("nome", ""),
        "jogador": request.form.get("jogador", ""),
        "tecnica": request.form.get("tecnica", ""),
        "dominio_inato": request.form.get("dominio_inato", ""),
        "tracos": request.form.get("tracos", ""),
        "ideais": request.form.get("ideais", ""),
        "ligacoes": request.form.get("ligacoes", ""),
        "complicacoes": request.form.get("complicacoes", ""),
        "metodo_atributos": request.form.get("metodo_atributos", "fixos"),
        "atributos": {
            attr: int(request.form.get(f"attr_{attr}", 10))
            for attr in ATRIBUTOS
        }
    }
    session["criacao"] = dados
    return render_template("jujutsu/criar_passo2.html",
                           dados=dados,
                           origens=ORIGENS,
                           pericias=PERICIAS,
                           pericias_treino=PERICIAS_TREINO,
                           attr_abrev=ATTR_ABREV)


@bp.route("/criar/passo3", methods=["POST"])
@login_required
def criar_passo3():
    dados = session.get("criacao", {})
    dados["origem"] = request.form.get("origem", "inato")

    origem_info = ORIGENS.get(dados["origem"], {})
    dados["bonus_origem"] = {}

    for attr in ATRIBUTOS:
        bonus = int(request.form.get(f"bonus_{attr}", 0))
        dados["bonus_origem"][attr] = bonus
        dados["atributos"][attr] = dados["atributos"].get(attr, 10) + bonus

    if dados["origem"] == "herdado_personalizado":
        dados["clan_personalizado"] = {
            "nome": request.form.get("clan_nome", "Clã Desconhecido"),
            "pericias": request.form.getlist("clan_pericias"),
            "habilidade_nome": request.form.get("clan_habilidade_nome", ""),
            "habilidade_desc": request.form.get("clan_habilidade_desc", ""),
        }

    session["criacao"] = dados

    pericias_anteriores = []
    if dados.get("origem") == "herdado_personalizado":
        pericias_anteriores = dados.get("clan_personalizado", {}).get("pericias", [])

    return render_template("jujutsu/criar_passo3.html",
                           dados=dados,
                           especializacoes=ESPECIALIZACOES,
                           atributos_labels=ATRIBUTOS_LABELS,
                           pericias=PERICIAS,
                           pericias_treino=PERICIAS_TREINO,
                           attr_abrev=ATTR_ABREV,
                           pericias_anteriores=pericias_anteriores)


@bp.route("/criar/passo4", methods=["POST"])
@login_required
def criar_passo4():
    dados = session.get("criacao", {})
    dados["especializacao"] = request.form.get("especializacao", "lutador")
    dados["atributo_chave"] = request.form.get("atributo_chave", "forca")
    dados["tr_escolhido"] = request.form.get("tr_escolhido", "Fortitude")
    pericias_json = request.form.get("pericias_json", "")
    if pericias_json:
        try:
            dados["pericias_treinadas"] = json.loads(pericias_json)
        except Exception:
            dados["pericias_treinadas"] = {}
    else:
        pericias_list = request.form.getlist("pericias")
        dados["pericias_treinadas"] = {p: "treinado" for p in pericias_list}

    session["criacao"] = dados
    return render_template("jujutsu/criar_passo4.html",
                           dados=dados,
                           armas=ARMAS_INICIAIS,
                           uniformes=UNIFORMES,
                           kits=KITS,
                           especializacoes=ESPECIALIZACOES,
                           armas_dados_json=json.dumps(ARMAS_DADOS),
                           escudos_dados_json=json.dumps(ESCUDOS_DADOS))


@bp.route("/criar/passo5", methods=["POST"])
@login_required
def criar_passo5():
    dados = session.get("criacao", {})
    dados["arma1"] = request.form.get("arma1", "")
    dados["arma2"] = request.form.get("arma2", "")
    dados["uniforme"] = request.form.get("uniforme", "Uniforme Comum")
    dados["kit"] = request.form.get("kit", "")
    dados["inventario"] = []
    dados["nivel"] = 1
    dados["xp"] = 0
    dados["pv_atual"] = None
    dados["pe_atual"] = None

    dados = calcular_ficha(dados)
    dados["pv_atual"] = dados["calculado"]["pv_max"]
    dados["pe_atual"] = dados["calculado"]["pe_max"]

    session["criacao"] = dados
    return render_template("jujutsu/criar_passo5.html",
                           dados=dados,
                           origens=ORIGENS,
                           especializacoes=ESPECIALIZACOES,
                           atributos_labels=ATRIBUTOS_LABELS,
                           pericias=PERICIAS,
                           pericias_treino=PERICIAS_TREINO,
                           attr_abrev=ATTR_ABREV)


@bp.route("/criar/salvar", methods=["POST"])
@login_required
def criar_salvar():
    dados = session.get("criacao", {})
    if not dados:
        return redirect(url_for("jujutsu.criar"))

    dados["notas"] = request.form.get("notas", "")
    dados["habilidades_extras"] = request.form.getlist("habilidades_extras") or []
    dados.setdefault("feiticos", [])

    pericias_extras_raw = request.form.get("pericias_extras_json", "{}")
    try:
        pericias_extras = json.loads(pericias_extras_raw)
    except Exception:
        pericias_extras = {}
    pt = dados.get("pericias_treinadas", {})
    if isinstance(pt, list):
        pt = {p: "treinado" for p in pt}
    for nome, nivel in pericias_extras.items():
        if nome in PERICIAS:
            pt[nome] = nivel
    dados["pericias_treinadas"] = pt

    dados = calcular_ficha(dados)

    nome = dados.get("nome", "Personagem Sem Nome")
    uid = session["usuario_id"]
    with get_db() as conn:
        cursor = conn.execute(
            "INSERT INTO personagens (nome, dados, usuario_id, sistema) VALUES (?, ?, ?, ?)",
            (nome, json.dumps(dados, ensure_ascii=False), uid, SISTEMA)
        )
        pid = cursor.lastrowid
        conn.commit()

    session.pop("criacao", None)
    return redirect(url_for("jujutsu.ver_personagem", pid=pid))


# ─── FICHA DO PERSONAGEM ────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>")
@login_required
def ver_personagem(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return redirect(url_for("jujutsu.index"))
    dados = json.loads(row["dados"])
    dados = calcular_ficha(dados)

    nivel = dados.get("nivel", 1)
    bt = dados["calculado"]["bonus_treinamento"]
    for inv in dados.get("invocacoes", []):
        calcular_invocacao(inv, nivel, bt)

    spec = ESPECIALIZACOES.get(dados.get("especializacao", ""), {})
    origem = ORIGENS.get(dados.get("origem", ""), {})

    pt_raw = dados.get("pericias_treinadas", {})
    if isinstance(pt_raw, list):
        pt_raw = {p: "treinado" for p in pt_raw}
    calc = dados.get("calculado", {})
    bt = calc.get("bonus_treinamento", 2)
    sob_medida = calc.get("bonus_sob_medida", False)
    penalidade_uni = calc.get("penalidade_uniforme", 0)
    attr_mods = {
        "forca":        calc.get("mod_forca", 0),
        "destreza":     calc.get("mod_destreza", 0),
        "constituicao": calc.get("mod_constituicao", 0),
        "inteligencia": calc.get("mod_inteligencia", 0),
        "sabedoria":    calc.get("mod_sabedoria", 0),
        "presenca":     calc.get("mod_presenca", 0),
    }
    pericias_calc = {}
    for nome, attr in PERICIAS.items():
        treinamento = pt_raw.get(nome)
        base_mod = attr_mods.get(attr, 0)
        train_bonus = bt if treinamento == "treinado" else (bt + bt // 2 if treinamento == "mestre" else 0)
        especiais = []
        if attr == "destreza" and sob_medida:
            especiais.append({"fonte": "Uniforme Sob Medida", "valor": 2})
        if attr == "destreza" and penalidade_uni != 0:
            especiais.append({"fonte": f"Penalidade ({dados.get('uniforme', 'uniforme')})", "valor": penalidade_uni})
        total = base_mod + train_bonus + sum(e["valor"] for e in especiais)
        pericias_calc[nome] = {
            "attr": attr,
            "base_mod": base_mod,
            "treinamento": treinamento,
            "train_bonus": train_bonus,
            "especiais": especiais,
            "total": total,
            "requer_treino": nome in PERICIAS_TREINO,
        }

    return render_template("jujutsu/ficha.html",
                           pid=pid,
                           dados=dados,
                           spec=spec,
                           origem=origem,
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           xp_table=XP_TABLE,
                           armas_dados=ARMAS_DADOS,
                           escudos_dados=ESCUDOS_DADOS,
                           kits=KITS,
                           uniformes=UNIFORMES,
                           pericias_calc=pericias_calc,
                           attr_abrev=ATTR_ABREV)


@bp.route("/personagem/<int:pid>/editar", methods=["GET", "POST"])
@login_required
def editar_personagem(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return redirect(url_for("jujutsu.index"))

    dados = json.loads(row["dados"])

    if request.method == "POST":
        for attr in ATRIBUTOS:
            val = request.form.get(f"attr_{attr}")
            if val:
                dados["atributos"][attr] = int(val)

        dados["nome"] = request.form.get("nome", dados.get("nome", ""))
        dados["jogador"] = request.form.get("jogador", dados.get("jogador", ""))
        dados["tecnica"] = request.form.get("tecnica", dados.get("tecnica", ""))
        dados["tracos"] = request.form.get("tracos", dados.get("tracos", ""))
        dados["ideais"] = request.form.get("ideais", dados.get("ideais", ""))
        dados["ligacoes"] = request.form.get("ligacoes", dados.get("ligacoes", ""))
        dados["complicacoes"] = request.form.get("complicacoes", dados.get("complicacoes", ""))
        dados["notas"] = request.form.get("notas", dados.get("notas", ""))
        feiticos_text = request.form.get("feiticos_text", "")
        dados["feiticos"] = [{"nome": l, "desc": ""} for l in feiticos_text.splitlines() if l.strip()]
        dados["xp"] = int(request.form.get("xp", dados.get("xp", 0)))
        dados["pv_atual"] = int(request.form.get("pv_atual", dados.get("pv_atual", 1)))
        dados["pe_atual"] = int(request.form.get("pe_atual", dados.get("pe_atual", 0)))
        pericias_json = request.form.get("pericias_json")
        if pericias_json:
            try:
                dados["pericias_treinadas"] = json.loads(pericias_json)
            except Exception:
                pass

        dados = calcular_ficha(dados)

        with get_db() as conn:
            conn.execute(
                "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
                (dados["nome"], json.dumps(dados, ensure_ascii=False), pid)
            )
            conn.commit()

        return redirect(url_for("jujutsu.ver_personagem", pid=pid))

    dados = calcular_ficha(dados)
    return render_template("jujutsu/editar.html",
                           pid=pid,
                           dados=dados,
                           atributos=ATRIBUTOS,
                           atributos_labels=ATRIBUTOS_LABELS,
                           pericias=PERICIAS,
                           attr_abrev=ATTR_ABREV)


@bp.route("/personagem/<int:pid>/subir_nivel", methods=["POST"])
@login_required
def subir_nivel(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return jsonify({"erro": "Personagem não encontrado"}), 404

    dados = json.loads(row["dados"])
    nivel_atual = dados.get("nivel", 1)

    if nivel_atual >= 20:
        return jsonify({"erro": "Já está no nível máximo (20)"}), 400

    novo_nivel = nivel_atual + 1
    dados["nivel"] = novo_nivel

    spec_key = dados.get("especializacao", "lutador")
    spec = ESPECIALIZACOES.get(spec_key, {})
    mod_con = calcular_modificador(dados["atributos"].get("constituicao", 10))

    dado_vida = spec.get("pv_dado", 8)
    rolar_pv = request.json.get("rolar_pv", False) if request.is_json else False
    if rolar_pv:
        ganho_pv = random.randint(1, dado_vida) + mod_con
    else:
        ganho_pv = spec.get("pv_fixo_nivel", 5) + mod_con

    dados["pv_ganho_historico"] = dados.get("pv_ganho_historico", [])
    dados["pv_ganho_historico"].append({"nivel": novo_nivel, "ganho": ganho_pv})

    pe_ganho = spec.get("pe_por_nivel", 4)

    dados["pontos_atributo_disponivel"] = dados.get("pontos_atributo_disponivel", 0)
    if novo_nivel % 4 == 0:
        dados["pontos_atributo_disponivel"] += 2

    if spec_key != "restringido":
        dados["aptidoes_pendentes"] = dados.get("aptidoes_pendentes", 0) + 1

    dados["habilidades_pendentes"] = dados.get("habilidades_pendentes", 0) + 1

    dados = calcular_ficha(dados)
    dados["pv_atual"] = min(dados.get("pv_atual", dados["calculado"]["pv_max"]) + ganho_pv,
                            dados["calculado"]["pv_max"])
    dados["pe_atual"] = dados["calculado"]["pe_max"]

    historico = dados.get("historico_nivel", [])
    historico.append({
        "de": nivel_atual,
        "para": novo_nivel,
        "ganho_pv": ganho_pv,
        "ganho_pe": pe_ganho,
    })
    dados["historico_nivel"] = historico

    with get_db() as conn:
        conn.execute(
            "UPDATE personagens SET nome=?, dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
            (dados["nome"], json.dumps(dados, ensure_ascii=False), pid)
        )
        conn.commit()

    return jsonify({
        "sucesso": True,
        "nivel": novo_nivel,
        "ganho_pv": ganho_pv,
        "pv_max": dados["calculado"]["pv_max"],
        "pe_max": dados["calculado"]["pe_max"],
        "bonus_treinamento": dados["calculado"]["bonus_treinamento"],
        "grau": dados["calculado"]["grau"],
        "pontos_atributo_disponivel": dados.get("pontos_atributo_disponivel", 0),
        "mensagem": f"Subiu para o nível {novo_nivel}! Ganhou {ganho_pv} PV."
    })


@bp.route("/personagem/<int:pid>/salvar_feiticos", methods=["POST"])
@login_required
def salvar_feiticos(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404
    try:
        feiticos = json.loads(request.get_json(force=True).get("feiticos_json", "[]"))
    except Exception:
        return jsonify({"erro": "JSON inválido"}), 400
    dados["feiticos"] = feiticos
    _save_personagem(pid, dados)
    return jsonify({"sucesso": True})


@bp.route("/personagem/<int:pid>/atualizar_pv", methods=["POST"])
@login_required
def atualizar_pv(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404

    dados = json.loads(row["dados"])
    dados = calcular_ficha(dados)

    novo_pv = request.json.get("pv_atual")
    if novo_pv is not None:
        dados["pv_atual"] = max(0, min(int(novo_pv), dados["calculado"]["pv_max"]))

    novo_pe = request.json.get("pe_atual")
    if novo_pe is not None:
        dados["pe_atual"] = max(0, min(int(novo_pe), dados["calculado"]["pe_max"]))

    novo_xp = request.json.get("xp")
    if novo_xp is not None:
        dados["xp"] = max(0, int(novo_xp))

    with get_db() as conn:
        conn.execute(
            "UPDATE personagens SET dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
            (json.dumps(dados, ensure_ascii=False), pid)
        )
        conn.commit()

    return jsonify({
        "pv_atual": dados["pv_atual"],
        "pe_atual": dados["pe_atual"],
        "xp": dados.get("xp", 0),
    })


@bp.route("/personagem/<int:pid>/distribuir_atributo", methods=["POST"])
@login_required
def distribuir_atributo(pid):
    with get_db() as conn:
        row = conn.execute("SELECT * FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404

    dados = json.loads(row["dados"])
    pontos = dados.get("pontos_atributo_disponivel", 0)

    if pontos <= 0:
        return jsonify({"erro": "Sem pontos de atributo disponíveis"}), 400

    attr = request.json.get("atributo")
    if attr not in ATRIBUTOS:
        return jsonify({"erro": "Atributo inválido"}), 400

    limite = 30 if dados.get("especializacao") == "restringido" and attr in ["forca", "destreza", "constituicao"] else 20
    atual = dados["atributos"].get(attr, 10)

    if atual >= limite:
        return jsonify({"erro": f"Atributo já no limite ({limite})"}), 400

    dados["atributos"][attr] = atual + 1
    dados["pontos_atributo_disponivel"] = pontos - 1
    dados = calcular_ficha(dados)

    with get_db() as conn:
        conn.execute(
            "UPDATE personagens SET dados=?, atualizado_em=CURRENT_TIMESTAMP WHERE id=?",
            (json.dumps(dados, ensure_ascii=False), pid)
        )
        conn.commit()

    return jsonify({
        "sucesso": True,
        "atributo": attr,
        "novo_valor": dados["atributos"][attr],
        "modificador": calcular_modificador(dados["atributos"][attr]),
        "pontos_restantes": dados["pontos_atributo_disponivel"],
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
    return redirect(url_for("jujutsu.index"))


# ─── API JUJUTSU ────────────────────────────────────────────────────────────────

@bp.route("/api/rolar_dados", methods=["POST"])
def rolar_dados():
    dados_req = request.json or {}
    tipo = dados_req.get("tipo", "4d6drop")
    n = int(dados_req.get("n", 1))
    lados = int(dados_req.get("lados", 6))

    if tipo == "4d6drop":
        rolls = [random.randint(1, 6) for _ in range(4)]
        resultado = sum(sorted(rolls)[1:])
        return jsonify({"rolls": rolls, "resultado": resultado, "descricao": f"4d6 (descarta o menor): {rolls} = {resultado}"})
    else:
        rolls = [random.randint(1, lados) for _ in range(n)]
        resultado = sum(rolls)
        return jsonify({"rolls": rolls, "resultado": resultado, "descricao": f"{n}d{lados}: {rolls} = {resultado}"})


@bp.route("/api/info_origem/<origem_key>")
def info_origem(origem_key):
    origem = ORIGENS.get(origem_key)
    if not origem:
        return jsonify({"erro": "Origem não encontrada"}), 404
    return jsonify(origem)


@bp.route("/api/info_especializacao/<spec_key>")
def info_especializacao(spec_key):
    spec = ESPECIALIZACOES.get(spec_key)
    if not spec:
        return jsonify({"erro": "Especialização não encontrada"}), 404
    return jsonify(spec)


# ─── INVOCAÇÕES ────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>/invocacoes")
@login_required
def listar_invocacoes(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    if dados.get("especializacao") != "controlador":
        return redirect(url_for("jujutsu.ver_personagem", pid=pid))
    dados = calcular_ficha(dados)

    nivel = dados.get("nivel", 1)
    bt = dados["calculado"]["bonus_treinamento"]
    invocacoes = dados.get("invocacoes", [])
    for inv in invocacoes:
        calcular_invocacao(inv, nivel, bt)

    grades_acesso = get_grades_acesso(nivel) if dados.get("especializacao") == "controlador" else GRADE_ORDEM

    return render_template("jujutsu/invocacoes.html",
                           pid=pid, dados=dados, invocacoes=invocacoes,
                           grades_acesso=grades_acesso, grade_nomes=GRADE_NOMES,
                           inv_grades=INVOCACAO_GRADES)


@bp.route("/personagem/<int:pid>/invocacoes/criar", methods=["GET", "POST"])
@login_required
def criar_invocacao(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    if dados.get("especializacao") != "controlador":
        return redirect(url_for("jujutsu.ver_personagem", pid=pid))
    dados = calcular_ficha(dados)

    nivel = dados.get("nivel", 1)
    bt = dados["calculado"]["bonus_treinamento"]
    grades_acesso = get_grades_acesso(nivel) if dados.get("especializacao") == "controlador" else GRADE_ORDEM

    if request.method == "POST":
        inv = _parse_invocacao_form(request.form, nivel, bt)
        dados.setdefault("invocacoes", []).append(inv)
        _save_personagem(pid, dados)
        return redirect(url_for("jujutsu.listar_invocacoes", pid=pid))

    return render_template("jujutsu/criar_invocacao.html",
                           pid=pid, dados=dados, inv=None, iid=None,
                           grades_acesso=grades_acesso, grade_nomes=GRADE_NOMES,
                           inv_grades=INVOCACAO_GRADES, inv_dano=INVOCACAO_DANO,
                           inv_auxilio=INVOCACAO_AUXILIO, inv_carac=INVOCACAO_CARAC,
                           inv_area=INVOCACAO_AREA, pericias=PERICIAS,
                           pericias_treino=PERICIAS_TREINO,
                           atributos=ATRIBUTOS, atributos_labels=ATRIBUTOS_LABELS,
                           nivel=nivel, bt=bt)


@bp.route("/personagem/<int:pid>/invocacoes/<int:iid>/editar", methods=["GET", "POST"])
@login_required
def editar_invocacao(pid, iid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    if dados.get("especializacao") != "controlador":
        return redirect(url_for("jujutsu.ver_personagem", pid=pid))
    dados = calcular_ficha(dados)

    nivel = dados.get("nivel", 1)
    bt = dados["calculado"]["bonus_treinamento"]
    invocacoes = dados.get("invocacoes", [])
    grades_acesso = get_grades_acesso(nivel) if dados.get("especializacao") == "controlador" else GRADE_ORDEM

    if iid >= len(invocacoes):
        return redirect(url_for("jujutsu.listar_invocacoes", pid=pid))

    if request.method == "POST":
        inv = _parse_invocacao_form(request.form, nivel, bt)
        invocacoes[iid] = inv
        dados["invocacoes"] = invocacoes
        _save_personagem(pid, dados)
        return redirect(url_for("jujutsu.listar_invocacoes", pid=pid))

    inv = invocacoes[iid]
    calcular_invocacao(inv, nivel, bt)
    return render_template("jujutsu/criar_invocacao.html",
                           pid=pid, dados=dados, inv=inv, iid=iid,
                           grades_acesso=grades_acesso, grade_nomes=GRADE_NOMES,
                           inv_grades=INVOCACAO_GRADES, inv_dano=INVOCACAO_DANO,
                           inv_auxilio=INVOCACAO_AUXILIO, inv_carac=INVOCACAO_CARAC,
                           inv_area=INVOCACAO_AREA, pericias=PERICIAS,
                           pericias_treino=PERICIAS_TREINO,
                           atributos=ATRIBUTOS, atributos_labels=ATRIBUTOS_LABELS,
                           nivel=nivel, bt=bt)


@bp.route("/personagem/<int:pid>/invocacoes/<int:iid>/deletar", methods=["POST"])
@login_required
def deletar_invocacao(pid, iid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    invocacoes = dados.get("invocacoes", [])
    if 0 <= iid < len(invocacoes):
        invocacoes.pop(iid)
        dados["invocacoes"] = invocacoes
        _save_personagem(pid, dados)
    return redirect(url_for("jujutsu.listar_invocacoes", pid=pid))


@bp.route("/personagem/<int:pid>/invocacoes/<int:iid>/pv", methods=["POST"])
@login_required
def atualizar_pv_invocacao(pid, iid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404
    dados = calcular_ficha(dados)
    nivel = dados.get("nivel", 1)
    bt = dados["calculado"]["bonus_treinamento"]
    invocacoes = dados.get("invocacoes", [])
    if iid >= len(invocacoes):
        return jsonify({"erro": "Invocação não encontrada"}), 404

    inv = invocacoes[iid]
    calcular_invocacao(inv, nivel, bt)
    pv_max = inv["calculado"]["pv_max"]

    novo_pv = request.json.get("pv_atual")
    if novo_pv is not None:
        inv["pv_atual"] = max(0, min(int(novo_pv), pv_max))

    dados["invocacoes"] = invocacoes
    _save_personagem(pid, dados)
    return jsonify({"pv_atual": inv.get("pv_atual", pv_max), "pv_max": pv_max})


def _parse_invocacao_form(form, nivel, bt):
    grau = form.get("grau", "4")
    atributos = {attr: int(form.get(f"attr_{attr}", 8))
                 for attr in ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "presenca"]}
    try:
        acoes = json.loads(form.get("acoes_json", "[]"))
    except Exception:
        acoes = []
    try:
        caracs = json.loads(form.get("caracteristicas_json", "[]"))
    except Exception:
        caracs = []

    inv = {
        "nome": form.get("nome", "Sem Nome"),
        "tipo": form.get("tipo", "shikigami"),
        "grau": grau,
        "descricao": form.get("descricao", ""),
        "intermediario": form.get("intermediario", ""),
        "atributos": atributos,
        "atrib_ataque": form.get("atrib_ataque", "forca"),
        "jogada_ataque_tipo": form.get("jogada_ataque_tipo", "corpo_a_corpo"),
        "tr_treinado": form.get("tr_treinado", "Fortitude"),
        "pericias_treinadas": form.getlist("pericias_treinadas"),
        "acoes": acoes,
        "caracteristicas": caracs,
        "pv_atual": None,
    }
    calcular_invocacao(inv, nivel, bt)
    inv["pv_atual"] = inv["calculado"]["pv_max"]
    return inv


@bp.route("/api/invocacao_calc", methods=["POST"])
def api_invocacao_calc():
    data = request.json or {}
    nivel = int(data.get("nivel", 1))
    bt = calcular_bonus_treinamento(nivel)
    inv = {
        "grau": data.get("grau", "4"),
        "atributos": data.get("atributos", {}),
        "atrib_ataque": data.get("atrib_ataque", "forca"),
        "acoes": data.get("acoes", []),
        "caracteristicas": data.get("caracteristicas", []),
    }
    calcular_invocacao(inv, nivel, bt)
    return jsonify(inv["calculado"])


# ─── TÉCNICAS ───────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>/tecnicas")
@login_required
def listar_tecnicas(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    dados = calcular_ficha(dados)
    tecnicas = dados.get("tecnicas", [])
    return render_template("jujutsu/tecnicas.html",
                           pid=pid, dados=dados, tecnicas=tecnicas,
                           tecnica_tipos=TECNICA_TIPOS,
                           tecnica_conjuracao=TECNICA_CONJURACAO)


@bp.route("/personagem/<int:pid>/tecnicas/criar", methods=["GET", "POST"])
@login_required
def criar_tecnica(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    dados = calcular_ficha(dados)

    if request.method == "POST":
        tec = _parse_tecnica_form(request.form)
        dados.setdefault("tecnicas", []).append(tec)
        _save_personagem(pid, dados)
        return redirect(url_for("jujutsu.listar_tecnicas", pid=pid))

    return _render_criar_tecnica(pid, dados, None, None)


@bp.route("/personagem/<int:pid>/tecnicas/<int:tid>/editar", methods=["GET", "POST"])
@login_required
def editar_tecnica(pid, tid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    dados = calcular_ficha(dados)
    tecnicas = dados.get("tecnicas", [])
    if tid >= len(tecnicas):
        return redirect(url_for("jujutsu.listar_tecnicas", pid=pid))

    if request.method == "POST":
        tec = _parse_tecnica_form(request.form)
        tecnicas[tid] = tec
        dados["tecnicas"] = tecnicas
        _save_personagem(pid, dados)
        return redirect(url_for("jujutsu.listar_tecnicas", pid=pid))

    return _render_criar_tecnica(pid, dados, tecnicas[tid], tid)


@bp.route("/personagem/<int:pid>/tecnicas/<int:tid>/deletar", methods=["POST"])
@login_required
def deletar_tecnica(pid, tid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    tecnicas = dados.get("tecnicas", [])
    if 0 <= tid < len(tecnicas):
        tecnicas.pop(tid)
        dados["tecnicas"] = tecnicas
        _save_personagem(pid, dados)
    return redirect(url_for("jujutsu.listar_tecnicas", pid=pid))


def _parse_tecnica_form(form):
    try:
        condicoes = json.loads(form.get("condicoes_json", "[]"))
    except Exception:
        condicoes = []
    try:
        liberacoes = json.loads(form.get("liberacoes_json", "[]"))
    except Exception:
        liberacoes = []
    return {
        "nome": form.get("nome", "Sem Nome"),
        "nivel": int(form.get("nivel", 0)),
        "tipo": form.get("tipo", "ofensiva_ataque"),
        "duracao_tipo": form.get("duracao_tipo", "imediata"),
        "conjuracao": form.get("conjuracao", "acao_comum"),
        "alcance": form.get("alcance", ""),
        "area": form.get("area", ""),
        "alvo": form.get("alvo", ""),
        "duracao": form.get("duracao", ""),
        "custo_pe": form.get("custo_pe", ""),
        "descricao": form.get("descricao", ""),
        "condicoes": condicoes,
        "liberacoes_maximas": liberacoes,
        "tem_tecnica_maxima": form.get("tem_tecnica_maxima") == "1",
    }


def _render_criar_tecnica(pid, dados, tec, tid):
    return render_template("jujutsu/criar_tecnica.html",
                           pid=pid, dados=dados, tec=tec, tid=tid,
                           tecnica_tipos=TECNICA_TIPOS,
                           tecnica_conjuracao=TECNICA_CONJURACAO,
                           tecnica_duracao=TECNICA_DURACAO,
                           dano_alvo_tr=TECNICA_DANO_ALVO_TR,
                           dano_alvo_ataque=TECNICA_DANO_ALVO_ATAQUE,
                           dano_area_tr=TECNICA_DANO_AREA_TR,
                           alcance_m=TECNICA_ALCANCE_M,
                           area_m=TECNICA_AREA_M,
                           aux_ca=TECNICA_AUX_CA,
                           aux_rd=TECNICA_AUX_RD,
                           aux_bonus=TECNICA_AUX_BONUS,
                           aux_movimento=TECNICA_AUX_MOVIMENTO,
                           aux_dano_add=TECNICA_AUX_DANO_ADD,
                           aux_cura_unico=TECNICA_AUX_CURA_UNICO,
                           aux_cura_area=TECNICA_AUX_CURA_AREA,
                           aux_cd=TECNICA_AUX_CD,
                           passiva_red_pe=TECNICA_PASSIVA_RED_PE,
                           tecnica_maxima_ref=TECNICA_MAXIMA_REF,
                           condicoes_por_forca=CONDICOES_POR_FORCA,
                           condicao_custo_dados=CONDICAO_CUSTO_DADOS,
                           condicao_duracao_padrao=CONDICAO_DURACAO_PADRAO,
                           liberacao_maxima_custo=LIBERACAO_MAXIMA_CUSTO,
                           testes_resistencia=TESTES_RESISTENCIA)


# ─── APTIDÕES ───────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>/aptidoes", methods=["GET", "POST"])
@login_required
def gerenciar_aptidoes(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    dados = calcular_ficha(dados)

    if request.method == "POST":
        aptidoes_selecionadas = request.form.getlist("aptidoes")
        dados["aptidoes"] = aptidoes_selecionadas
        _save_personagem(pid, dados)
        return redirect(url_for("jujutsu.ver_personagem", pid=pid))

    aptidoes_atuais = set(dados.get("aptidoes", []))
    nivel = dados.get("nivel", 1)

    eh_restringido = dados.get("especializacao") == "restringido"
    dom = APTIDOES_DOMINIO if not eh_restringido else []

    def apt_info(apt):
        req_ids = apt.get("req", [])
        req_ok = all(r in aptidoes_atuais for r in req_ids)
        level_ok = nivel >= apt.get("nivel_req", 1)
        return {**apt, "pode": req_ok and level_ok, "tem": apt["id"] in aptidoes_atuais}

    dom_info = [apt_info(a) for a in dom]
    adic_info = [apt_info(a) for a in APTIDOES_ADICIONAIS]

    return render_template("jujutsu/aptidoes.html",
                           pid=pid, dados=dados,
                           aptidoes_dominio=dom_info,
                           aptidoes_adicionais=adic_info,
                           aptidoes_atuais=list(aptidoes_atuais),
                           nivel=nivel)


# ─── DOMÍNIO ────────────────────────────────────────────────────────────────────

@bp.route("/personagem/<int:pid>/dominio", methods=["GET", "POST"])
@login_required
def gerenciar_dominio(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return redirect(url_for("jujutsu.index"))
    dados = calcular_ficha(dados)

    if dados.get("especializacao") == "restringido":
        return redirect(url_for("jujutsu.ver_personagem", pid=pid))

    if request.method == "POST":
        action = request.form.get("action")
        if action == "salvar":
            dados["dominio"] = {
                "nome": request.form.get("nome", ""),
                "tipo": request.form.get("tipo", "incompleta"),
                "efeito_acerto_garantido": request.form.get("efeito_acerto_garantido", ""),
                "amplificacoes": request.form.get("amplificacoes", ""),
                "efeito_ambiental": request.form.get("efeito_ambiental", ""),
                "descricao": request.form.get("descricao", ""),
            }
        elif action == "deletar":
            dados.pop("dominio", None)
        _save_personagem(pid, dados)
        return redirect(url_for("jujutsu.ver_personagem", pid=pid))

    aptidoes_atuais = set(dados.get("aptidoes", []))
    nivel = dados.get("nivel", 1)
    tipos_disponiveis = {}
    for k, v in DOMINIO_TIPOS.items():
        req = v["req_aptidao"]
        if req in aptidoes_atuais:
            tipos_disponiveis[k] = v

    return render_template("jujutsu/dominio.html",
                           pid=pid, dados=dados,
                           dominio=dados.get("dominio"),
                           dominio_tipos=DOMINIO_TIPOS,
                           tipos_disponiveis=tipos_disponiveis,
                           aptidoes_atuais=aptidoes_atuais,
                           nivel=nivel)
