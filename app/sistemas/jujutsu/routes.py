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
    APTIDOES_DOMINIO, APTIDOES_ADICIONAIS, TODAS_APTIDOES, APTIDOES_CATEGORIAS, DOMINIO_TIPOS,
    INVOCACAO_ACOES_LISTA, INVOCACAO_CARAC_LISTA, get_max_invocacoes,
    ARMAS_DADOS, ESCUDOS_DADOS, ATTR_ABREV,
    ESTILOS_COMBATE,
    get_ganhos_nivel, TABELAS_NIVEIS, get_habilidades_catalogadas,
    NIVEIS_APTIDAO_CATEGORIAS, NIVEIS_APTIDAO_LABELS,
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
                           pericias_anteriores=pericias_anteriores,
                           estilos_combate=ESTILOS_COMBATE)


@bp.route("/criar/passo4", methods=["POST"])
@login_required
def criar_passo4():
    dados = session.get("criacao", {})
    dados["especializacao"] = request.form.get("especializacao", "lutador")
    dados["atributo_chave"] = request.form.get("atributo_chave", "forca")
    dados["tr_escolhido"] = request.form.get("tr_escolhido", "Fortitude")
    if dados["especializacao"] == "especialista_combate":
        dados["estilo_combate"] = request.form.get("estilo_combate", "")
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

_MECANICAS_DESC = {
    "+2 Pontos de Atributo": "Distribua 2 pontos em atributos a sua escolha (máx. +1 por atributo por nível).",
    "BT +1": "Seu Bônus de Treinamento aumenta em +1.",
    "Mestre em uma Perícia": "Escolha uma perícia que seja treinado: você se torna Mestre nela.",
    "Aptidão Amaldiçoada (escolha)": "Aprenda uma nova Aptidão Amaldiçoada a sua escolha.",
    "+1 Invocação": "Você recebe uma nova Invocação (Treinamento em Controle).",
    "+Comandos por Ação": "A quantidade de comandos que você pode dar por Ação Comum e Ação Bônus aumenta em 1.",
    "+2° Estilo de Combate": "Você aprende um segundo Estilo de Combate do Repertório do Especialista.",
    "+3° Estilo de Combate": "Você aprende um terceiro Estilo de Combate do Repertório do Especialista.",
    "Mudança de Fundamento adicional": "Aprenda mais uma Mudança de Fundamento (Domínio dos Fundamentos).",
    "Aptidão: Energia Reversa (automático)": "Você aprende a Aptidão Amaldiçoada Energia Reversa automaticamente.",
    "Aptidão: Liberação de Energia Reversa (automático)": "Você aprende a Aptidão Amaldiçoada Liberação de Energia Reversa automaticamente.",
    "Treinamento em Controle: +1 Invocação": "Mais uma Invocação liberada pelo Treinamento em Controle.",
    "Dádiva do Céu": "Escolha uma Dádiva do Céu da lista do Restringido.",
}


def _build_ganhos_por_nivel(spec_key, spec_data):
    """Retorna dict {nivel: [{nome, desc, tipo}]} para o bloco Level Up Upgrades."""
    # Monta lookup nome → desc a partir das habilidades do spec
    desc_lookup = {}
    for hab in spec_data.get("habilidades_base", []):
        desc_lookup[hab["nome"].strip()] = hab.get("desc", "")
    for _lvl, lista in spec_data.get("habilidades_nivel", {}).items():
        for item in lista:
            if "–" in item:
                partes = item.split("–", 1)
                desc_lookup[partes[0].strip()] = partes[1].strip()

    result = {}
    nome_hab = {
        "lutador": "Habilidade de Lutador",
        "especialista_combate": "Habilidade de Especialista em Combate",
        "especialista_tecnica": "Habilidade de Especialista em Técnica",
        "controlador": "Habilidade de Controlador",
        "suporte": "Habilidade de Suporte",
        "restringido": "Habilidade de Restringido",
    }.get(spec_key, "Habilidade de Especialização")

    for nivel in range(1, 21):
        itens = []

        # Ganhos automáticos da tabela
        tabela = TABELAS_NIVEIS.get(spec_key, {})
        for nome in tabela.get(nivel, []):
            desc = desc_lookup.get(nome) or _MECANICAS_DESC.get(nome, "")
            tipo = "mecanica" if nome.startswith(("+", "BT", "Mestre", "Aptidão:", "Mudança")) else "habilidade"
            itens.append({"nome": nome, "desc": desc, "tipo": tipo})

        # Habilidade de especialização (escolha) — todo nível > 1
        if nivel > 1:
            itens.append({
                "nome": nome_hab + " (escolha)",
                "desc": "Escolha qualquer habilidade da lista desta especialização que você atenda os pré-requisitos.",
                "tipo": "escolha",
            })

        # Aptidão amaldiçoada — todo nível, exceto restringido
        # (a aptidão escolhida é injetada dinamicamente no template via aptidoes_por_nivel)
        if spec_key != "restringido":
            itens.append({
                "nome": "aptidao_escolha",  # sentinela — tratado no template
                "desc": "",
                "tipo": "aptidao",
            })

        if itens:
            result[nivel] = itens

    return result

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
                           attr_abrev=ATTR_ABREV,
                           tabela_niveis=TABELAS_NIVEIS,
                           ganhos_por_nivel=_build_ganhos_por_nivel(
                               dados.get("especializacao", "lutador"), spec),
                           todas_aptidoes=TODAS_APTIDOES,
                           aptidoes_categorias=APTIDOES_CATEGORIAS,
                           aptidoes_por_nivel=dados.get("aptidoes_por_nivel", {}),
                           habilidades_catalogadas=get_habilidades_catalogadas(
                               dados.get("especializacao", "lutador")),
                           habilidades_por_nivel=dados.get("habilidades_por_nivel", {}),
                           niveis_aptidao_cats=NIVEIS_APTIDAO_CATEGORIAS,
                           niveis_aptidao_labels=NIVEIS_APTIDAO_LABELS,
                           niveis_aptidao=dados.get("niveis_aptidao", {}))


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

    ganhos_nivel = get_ganhos_nivel(spec_key, novo_nivel)

    catalogo = get_habilidades_catalogadas(spec_key)
    habs_por_nivel = dados.get("habilidades_por_nivel", {})
    used_hab_ids = set(habs_por_nivel.values())
    habilidades_disponiveis = [
        h for h in catalogo
        if h["nivel"] <= novo_nivel and h["id"] not in used_hab_ids
    ]

    return jsonify({
        "sucesso": True,
        "nivel": novo_nivel,
        "ganho_pv": ganho_pv,
        "pv_max": dados["calculado"]["pv_max"],
        "pe_max": dados["calculado"]["pe_max"],
        "bonus_treinamento": dados["calculado"]["bonus_treinamento"],
        "grau": dados["calculado"]["grau"],
        "pontos_atributo_disponivel": dados.get("pontos_atributo_disponivel", 0),
        "ganhos_nivel": ganhos_nivel,
        "habilidades_disponiveis": habilidades_disponiveis,
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

    max_invocacoes = get_max_invocacoes(nivel)
    return render_template("jujutsu/invocacoes.html",
                           pid=pid, dados=dados, invocacoes=invocacoes,
                           grades_acesso=grades_acesso, grade_nomes=GRADE_NOMES,
                           inv_grades=INVOCACAO_GRADES,
                           max_invocacoes=max_invocacoes)


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

    max_inv = get_max_invocacoes(nivel)
    invocacoes_atuais = dados.get("invocacoes", [])

    if request.method == "POST":
        if len(invocacoes_atuais) >= max_inv:
            return redirect(url_for("jujutsu.listar_invocacoes", pid=pid))
        inv = _parse_invocacao_form(request.form, nivel, bt)
        invocacoes_atuais.append(inv)
        dados["invocacoes"] = invocacoes_atuais
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


@bp.route("/personagem/<int:pid>/api/escolher_aptidao", methods=["POST"])
@login_required
def api_escolher_aptidao(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404

    data = request.json or {}
    nivel_str = str(data.get("nivel", ""))
    apt_id = data.get("apt_id", "")

    if not nivel_str or not apt_id:
        return jsonify({"erro": "Parâmetros inválidos"}), 400

    nivel_char = dados.get("nivel", 1)
    nivel_int = int(nivel_str)
    if nivel_int > nivel_char:
        return jsonify({"erro": "Nível não alcançado"}), 400

    todas = TODAS_APTIDOES
    apt = next((a for a in todas if a["id"] == apt_id), None)
    if not apt:
        return jsonify({"erro": "Aptidão não encontrada"}), 400

    if apt["nivel_req"] > nivel_char:
        return jsonify({"erro": f"Requer nível {apt['nivel_req']}"}), 400

    aptidoes_atuais = set(dados.get("aptidoes", []))
    for req in apt.get("req", []):
        if req not in aptidoes_atuais:
            return jsonify({"erro": "Pré-requisito não atendido"}), 400

    apt_por_nivel = dados.get("aptidoes_por_nivel", {})

    # Remove a aptidão antiga desse nível da lista global (se houver)
    antiga = apt_por_nivel.get(nivel_str)
    if antiga and antiga != apt_id:
        # Verifica se a antiga ainda é usada em outro nível antes de remover
        usada_outro = any(v == antiga for k, v in apt_por_nivel.items() if k != nivel_str)
        if not usada_outro:
            aptidoes_atuais.discard(antiga)

    apt_por_nivel[nivel_str] = apt_id
    aptidoes_atuais.add(apt_id)

    dados["aptidoes_por_nivel"] = apt_por_nivel
    dados["aptidoes"] = list(aptidoes_atuais)
    _save_personagem(pid, dados)

    return jsonify({
        "sucesso": True,
        "apt_id": apt_id,
        "apt_nome": apt["nome"],
        "apt_desc": apt["descricao"],
    })


@bp.route("/personagem/<int:pid>/api/escolher_habilidade_spec", methods=["POST"])
@login_required
def api_escolher_habilidade_spec(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404

    data = request.json or {}
    nivel_str = str(data.get("nivel", ""))
    hab_id = data.get("hab_id", "")

    if not nivel_str or not hab_id:
        return jsonify({"erro": "Parâmetros inválidos"}), 400

    nivel_char = dados.get("nivel", 1)
    nivel_int = int(nivel_str)
    if nivel_int > nivel_char:
        return jsonify({"erro": "Nível não alcançado"}), 400

    spec_key = dados.get("especializacao", "lutador")
    catalogo = get_habilidades_catalogadas(spec_key)
    hab = next((h for h in catalogo if h["id"] == hab_id), None)
    if not hab:
        return jsonify({"erro": "Habilidade não encontrada"}), 400

    if hab["nivel"] > nivel_char:
        return jsonify({"erro": f"Requer nível {hab['nivel']}"}), 400

    habs_por_nivel = dados.get("habilidades_por_nivel", {})
    antiga_id = habs_por_nivel.get(nivel_str)

    usada_outro = any(v == hab_id for k, v in habs_por_nivel.items() if k != nivel_str)
    if usada_outro:
        return jsonify({"erro": "Esta habilidade já foi escolhida em outro nível"}), 400

    habs_por_nivel[nivel_str] = hab_id
    dados["habilidades_por_nivel"] = habs_por_nivel

    # Update feiticos
    feiticos = dados.get("feiticos", [])
    feiticos = [f if isinstance(f, dict) else {"nome": f, "desc": ""} for f in feiticos]

    if antiga_id and antiga_id != hab_id:
        old_hab = next((h for h in catalogo if h["id"] == antiga_id), None)
        if old_hab:
            feiticos = [f for f in feiticos if f.get("nome") != old_hab["nome"]]

    if not any(f.get("nome") == hab["nome"] for f in feiticos):
        feiticos.append({"nome": hab["nome"], "desc": hab["desc"]})
    dados["feiticos"] = feiticos

    _save_personagem(pid, dados)
    return jsonify({"sucesso": True, "hab_nome": hab["nome"], "hab_desc": hab["desc"]})


@bp.route("/personagem/<int:pid>/api/atualizar_nivel_aptidao", methods=["POST"])
@login_required
def api_atualizar_nivel_aptidao(pid):
    row, dados = _get_personagem(pid)
    if not row:
        return jsonify({"erro": "Não encontrado"}), 404
    data = request.json or {}
    cat_id = data.get("categoria", "")
    nivel = data.get("nivel", 0)
    ids_validos = {c["id"] for c in NIVEIS_APTIDAO_CATEGORIAS}
    if cat_id not in ids_validos:
        return jsonify({"erro": "Categoria inválida"}), 400
    if not isinstance(nivel, int) or nivel < 0 or nivel > 4:
        return jsonify({"erro": "Nível inválido (0-4)"}), 400
    niveis = dados.get("niveis_aptidao", {})
    niveis[cat_id] = nivel
    dados["niveis_aptidao"] = niveis
    _save_personagem(pid, dados)
    label = NIVEIS_APTIDAO_LABELS[nivel]
    return jsonify({"sucesso": True, "nivel": nivel, "nome": label["nome"], "cor": label["cor"]})


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

    def apt_info(apt):
        req_ids = apt.get("req", [])
        req_ok = all(r in aptidoes_atuais for r in req_ids)
        level_ok = nivel >= apt.get("nivel_req", 1)
        return {**apt, "pode": req_ok and level_ok, "tem": apt["id"] in aptidoes_atuais}

    categorias_info = []
    for cat in APTIDOES_CATEGORIAS:
        if eh_restringido and cat["id"] in ("dominio", "energia_reversa", "especiais"):
            continue
        categorias_info.append({
            **cat,
            "lista": [apt_info(a) for a in cat["lista"]],
        })

    return render_template("jujutsu/aptidoes.html",
                           pid=pid, dados=dados,
                           categorias=categorias_info,
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
