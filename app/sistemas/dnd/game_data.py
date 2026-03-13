# ─── DUNGEONS & DRAGONS 5ª EDIÇÃO ──────────────────────────────────────────────
# Dados do sistema D&D 5e (SRD — System Reference Document)

ATRIBUTOS = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

ATRIBUTOS_LABELS = {
    "forca":        "Força",
    "destreza":     "Destreza",
    "constituicao": "Constituição",
    "inteligencia": "Inteligência",
    "sabedoria":    "Sabedoria",
    "carisma":      "Carisma",
}

ATRIBUTOS_ABREV = {
    "forca":        "FOR",
    "destreza":     "DES",
    "constituicao": "CON",
    "inteligencia": "INT",
    "sabedoria":    "SAB",
    "carisma":      "CAR",
}

# ─── RAÇAS ─────────────────────────────────────────────────────────────────────

RACAS = {
    "humano": {
        "nome": "Humano",
        "bonus_atributos": {a: 1 for a in ATRIBUTOS},
        "habilidades": ["Versatilidade: proficiência em uma perícia e uma ferramenta à escolha"],
        "velocidade": 9,
        "idiomas": ["Comum", "1 à escolha"],
    },
    "elfo_alto": {
        "nome": "Elfo Alto",
        "bonus_atributos": {"destreza": 2, "inteligencia": 1},
        "habilidades": [
            "Sentidos Aguçados: proficiência em Percepção",
            "Ancestralidade Feérica: vantagem em saves contra enfeitiçamento",
            "Transe: 4h de transe substitui 8h de sono",
            "Cantrip: aprende 1 truque de mago",
        ],
        "velocidade": 9,
        "idiomas": ["Comum", "Élfico", "1 à escolha"],
    },
    "elfo_silvestre": {
        "nome": "Elfo Silvestre",
        "bonus_atributos": {"destreza": 2, "sabedoria": 1},
        "habilidades": [
            "Sentidos Aguçados: proficiência em Percepção",
            "Máscara da Floresta: pode tentar se esconder quando parcialmente coberto por vegetação",
            "Pés Velozes: velocidade 10,5m",
        ],
        "velocidade": 10,
        "idiomas": ["Comum", "Élfico"],
    },
    "anao_escudo": {
        "nome": "Anão Escudo",
        "bonus_atributos": {"constituicao": 2, "forca": 2},
        "habilidades": [
            "Resiliência Anã: vantagem em saves contra veneno, resistência a dano de veneno",
            "Treinamento em Combate: proficiência em machados e martelos",
            "Familiaridade com Ferramentas: proficiência com ferramentas de ferreiro, cervejeiro ou pedreiro",
            "Familiaridade com Pedra: dobrar proficiência em testes de história sobre pedra",
        ],
        "velocidade": 7,
        "idiomas": ["Comum", "Anão"],
    },
    "anao_montanha": {
        "nome": "Anão da Montanha",
        "bonus_atributos": {"constituicao": 2, "forca": 2},
        "habilidades": [
            "Resiliência Anã: vantagem em saves contra veneno",
            "Treinamento em Armaduras: proficiência com armaduras leves e médias",
        ],
        "velocidade": 7,
        "idiomas": ["Comum", "Anão"],
    },
    "halfling_pe_leve": {
        "nome": "Halfling Pé-Leve",
        "bonus_atributos": {"destreza": 2, "carisma": 1},
        "habilidades": [
            "Sortudo: ao rolar 1 em d20, pode rolar novamente",
            "Corajoso: vantagem em saves contra medo",
            "Furtividade Natural: pode tentar se esconder atrás de criaturas maiores",
        ],
        "velocidade": 7,
        "idiomas": ["Comum", "Halfling"],
    },
    "gnomo_florestal": {
        "nome": "Gnomo Florestal",
        "bonus_atributos": {"inteligencia": 2, "destreza": 1},
        "habilidades": [
            "Ilusão Natural: conhece o truque Ilusão Menor",
            "Falar com Animais Pequenos: pode se comunicar com animais pequenos",
        ],
        "velocidade": 7,
        "idiomas": ["Comum", "Gnômico"],
    },
    "meio_elfo": {
        "nome": "Meio-Elfo",
        "bonus_atributos": {"carisma": 2},
        "bonus_outros": "+1 em dois atributos à escolha",
        "habilidades": [
            "Ancestralidade Feérica: vantagem em saves contra enfeitiçamento",
            "Habilidade Versátil: proficiência em 2 perícias à escolha",
        ],
        "velocidade": 9,
        "idiomas": ["Comum", "Élfico", "1 à escolha"],
    },
    "meio_orc": {
        "nome": "Meio-Orc",
        "bonus_atributos": {"forca": 2, "constituicao": 1},
        "habilidades": [
            "Resistência Implacável: ao cair a 0 PV, fica com 1 PV (1x/descanso longo)",
            "Ataques Selvagens: dado de dano extra em críticos com armas",
            "Intimidação: proficiência em Intimidação",
        ],
        "velocidade": 9,
        "idiomas": ["Comum", "Orc"],
    },
    "tiefling": {
        "nome": "Tiefling",
        "bonus_atributos": {"inteligencia": 1, "carisma": 2},
        "habilidades": [
            "Resistência Infernal: resistência a dano de fogo",
            "Legado Infernal: conhece Taumaturgia; Nv3 Punição Infernal; Nv5 Escuridão",
        ],
        "velocidade": 9,
        "idiomas": ["Comum", "Infernal"],
    },
    "draconato": {
        "nome": "Draconato",
        "bonus_atributos": {"forca": 2, "carisma": 1},
        "habilidades": [
            "Ancestralidade Dracônica: escolha tipo de dragão (define tipo de sopro e resistência)",
            "Sopro: 2d6 de dano (cresce com nível), TR Destreza ou Constituição CD 8+Prof+Con",
            "Resistência ao Dano do sopro",
        ],
        "velocidade": 9,
        "idiomas": ["Comum", "Dracônico"],
    },
}

# ─── CLASSES ───────────────────────────────────────────────────────────────────

CLASSES = {
    "barbaro": {
        "nome": "Bárbaro",
        "descricao": "Guerreiro selvagem que canaliza fúria primal em combate.",
        "dado_vida": 12,
        "pv_fixo": 7,
        "atributo_principal": "forca",
        "saves": ["forca", "constituicao"],
        "pericias_disponiveis": ["Adestramento", "Atletismo", "Intimidação", "Natureza", "Percepção", "Sobrevivência"],
        "qtd_pericias": 2,
        "proficiencias_armas": "todas as armas",
        "proficiencias_armaduras": "leves, médias, escudos",
        "magias": False,
        "furia_por_nivel": {1: 2, 3: 3, 6: 4, 12: 5, 17: 6, 20: "ilimitado"},
    },
    "bardo": {
        "nome": "Bardo",
        "descricao": "Artista mágico que usa música e palavras para dobrar a realidade.",
        "dado_vida": 8,
        "pv_fixo": 5,
        "atributo_principal": "carisma",
        "saves": ["destreza", "carisma"],
        "pericias_disponiveis": "todas",
        "qtd_pericias": 3,
        "proficiencias_armas": "simples, algumas marciais",
        "proficiencias_armaduras": "leves",
        "magias": True,
        "atributo_magia": "carisma",
    },
    "clerigo": {
        "nome": "Clérigo",
        "descricao": "Servo divino que canaliza o poder do seu deus.",
        "dado_vida": 8,
        "pv_fixo": 5,
        "atributo_principal": "sabedoria",
        "saves": ["sabedoria", "carisma"],
        "pericias_disponiveis": ["História", "Intuição", "Medicina", "Persuasão", "Religião"],
        "qtd_pericias": 2,
        "proficiencias_armas": "simples",
        "proficiencias_armaduras": "leves, médias, escudos",
        "magias": True,
        "atributo_magia": "sabedoria",
    },
    "druida": {
        "nome": "Druida",
        "descricao": "Guardião da natureza que pode se transformar em animais.",
        "dado_vida": 8,
        "pv_fixo": 5,
        "atributo_principal": "sabedoria",
        "saves": ["inteligencia", "sabedoria"],
        "pericias_disponiveis": ["Adestramento", "Arcana", "Intuição", "Medicina", "Natureza", "Percepção", "Religião", "Sobrevivência"],
        "qtd_pericias": 2,
        "proficiencias_armas": "simples (não metal)",
        "proficiencias_armaduras": "leves, médias, escudos (não metal)",
        "magias": True,
        "atributo_magia": "sabedoria",
    },
    "guerreiro": {
        "nome": "Guerreiro",
        "descricao": "Mestre do combate físico com diversas especializações.",
        "dado_vida": 10,
        "pv_fixo": 6,
        "atributo_principal": "forca",
        "saves": ["forca", "constituicao"],
        "pericias_disponiveis": ["Acrobacia", "Adestramento", "Atletismo", "História", "Intuição", "Intimidação", "Percepção", "Sobrevivência"],
        "qtd_pericias": 2,
        "proficiencias_armas": "todas as armas",
        "proficiencias_armaduras": "todas as armaduras e escudos",
        "magias": False,
    },
    "monge": {
        "nome": "Monge",
        "descricao": "Artista marcial que canaliza ki para feitos sobre-humanos.",
        "dado_vida": 8,
        "pv_fixo": 5,
        "atributo_principal": "destreza",
        "saves": ["forca", "destreza"],
        "pericias_disponiveis": ["Acrobacia", "Atletismo", "Furtividade", "História", "Intuição", "Religião"],
        "qtd_pericias": 2,
        "proficiencias_armas": "simples, espadas curtas",
        "proficiencias_armaduras": "nenhuma",
        "magias": False,
        "ki": True,
    },
    "paladino": {
        "nome": "Paladino",
        "descricao": "Guerreiro sagrado que jurou defender um ideal.",
        "dado_vida": 10,
        "pv_fixo": 6,
        "atributo_principal": "carisma",
        "saves": ["sabedoria", "carisma"],
        "pericias_disponiveis": ["Atletismo", "Intuição", "Intimidação", "Medicina", "Persuasão", "Religião"],
        "qtd_pericias": 2,
        "proficiencias_armas": "todas as armas",
        "proficiencias_armaduras": "todas as armaduras e escudos",
        "magias": True,
        "atributo_magia": "carisma",
    },
    "ranger": {
        "nome": "Patrulheiro",
        "descricao": "Explorador especializado em terrenos e inimigos favoritos.",
        "dado_vida": 10,
        "pv_fixo": 6,
        "atributo_principal": "destreza",
        "saves": ["forca", "destreza"],
        "pericias_disponiveis": ["Adestramento", "Atletismo", "Furtividade", "Investigação", "Natureza", "Percepção", "Sobrevivência"],
        "qtd_pericias": 3,
        "proficiencias_armas": "simples e marciais",
        "proficiencias_armaduras": "leves, médias, escudos",
        "magias": True,
        "atributo_magia": "sabedoria",
    },
    "ladino": {
        "nome": "Ladino",
        "descricao": "Especialista em furtividade, trapaça e ataques cirúrgicos.",
        "dado_vida": 8,
        "pv_fixo": 5,
        "atributo_principal": "destreza",
        "saves": ["destreza", "inteligencia"],
        "pericias_disponiveis": ["Acrobacia", "Atletismo", "Enganação", "Furtividade", "Intimidação", "Investigação", "Percepção", "Persuasão", "Prestidigitação", "Atuação"],
        "qtd_pericias": 4,
        "proficiencias_armas": "simples, besta de mão, espada longa, rapieira, espada curta",
        "proficiencias_armaduras": "leves",
        "magias": False,
        "ataque_furtivo": True,
    },
    "feiticeiro": {
        "nome": "Feiticeiro",
        "descricao": "Lançador de magia nato com poder inato em seu sangue.",
        "dado_vida": 6,
        "pv_fixo": 4,
        "atributo_principal": "carisma",
        "saves": ["constituicao", "carisma"],
        "pericias_disponiveis": ["Arcana", "Enganação", "Intuição", "Intimidação", "Persuasão", "Religião"],
        "qtd_pericias": 2,
        "proficiencias_armas": "adagas, dardos, fundas, bastão, besta leve",
        "proficiencias_armaduras": "nenhuma",
        "magias": True,
        "atributo_magia": "carisma",
        "pontos_feiticeria": True,
    },
    "bruxo": {
        "nome": "Bruxo",
        "descricao": "Faz um pacto com um ser poderoso em troca de poderes mágicos.",
        "dado_vida": 8,
        "pv_fixo": 5,
        "atributo_principal": "carisma",
        "saves": ["sabedoria", "carisma"],
        "pericias_disponiveis": ["Arcana", "Enganação", "História", "Intimidação", "Investigação", "Natureza", "Religião"],
        "qtd_pericias": 2,
        "proficiencias_armas": "simples",
        "proficiencias_armaduras": "leves",
        "magias": True,
        "atributo_magia": "carisma",
        "patrono": True,
        "magia_pacto": True,
    },
    "mago": {
        "nome": "Mago",
        "descricao": "Estudioso da magia arcana com um grimório de feitiços.",
        "dado_vida": 6,
        "pv_fixo": 4,
        "atributo_principal": "inteligencia",
        "saves": ["inteligencia", "sabedoria"],
        "pericias_disponiveis": ["Arcana", "História", "Intuição", "Investigação", "Medicina", "Religião"],
        "qtd_pericias": 2,
        "proficiencias_armas": "adagas, dardos, fundas, bastão, besta leve",
        "proficiencias_armaduras": "nenhuma",
        "magias": True,
        "atributo_magia": "inteligencia",
        "grimorio": True,
    },
}

# ─── ALINHAMENTOS ──────────────────────────────────────────────────────────────

ALINHAMENTOS = {
    "leal_bom":     "Leal e Bom",
    "neutro_bom":   "Neutro e Bom",
    "caotico_bom":  "Caótico e Bom",
    "leal_neutro":  "Leal e Neutro",
    "neutro":       "Neutro",
    "caotico_neutro":"Caótico e Neutro",
    "leal_mau":     "Leal e Mau",
    "neutro_mau":   "Neutro e Mau",
    "caotico_mau":  "Caótico e Mau",
}

# ─── PERÍCIAS ──────────────────────────────────────────────────────────────────

PERICIAS = {
    "Acrobacia":      "destreza",
    "Adestramento":   "sabedoria",
    "Arcana":         "inteligencia",
    "Atletismo":      "forca",
    "Atuação":        "carisma",
    "Enganação":      "carisma",
    "Furtividade":    "destreza",
    "História":       "inteligencia",
    "Intimidação":    "carisma",
    "Intuição":       "sabedoria",
    "Investigação":   "inteligencia",
    "Medicina":       "sabedoria",
    "Natureza":       "inteligencia",
    "Percepção":      "sabedoria",
    "Persuasão":      "carisma",
    "Prestidigitação":"destreza",
    "Religião":       "inteligencia",
    "Sobrevivência":  "sabedoria",
}

# ─── TESTES DE RESISTÊNCIA ─────────────────────────────────────────────────────

# Cada classe tem proficiência em 2 saves (ver CLASSES[x]["saves"])

# ─── PROGRESSÃO ────────────────────────────────────────────────────────────────

XP_TABLE = {
    1:  {"xp": 0,      "bonus_prof": 2},
    2:  {"xp": 300,    "bonus_prof": 2},
    3:  {"xp": 900,    "bonus_prof": 2},
    4:  {"xp": 2700,   "bonus_prof": 2},
    5:  {"xp": 6500,   "bonus_prof": 3},
    6:  {"xp": 14000,  "bonus_prof": 3},
    7:  {"xp": 23000,  "bonus_prof": 3},
    8:  {"xp": 34000,  "bonus_prof": 3},
    9:  {"xp": 48000,  "bonus_prof": 4},
    10: {"xp": 64000,  "bonus_prof": 4},
    11: {"xp": 85000,  "bonus_prof": 4},
    12: {"xp": 100000, "bonus_prof": 4},
    13: {"xp": 120000, "bonus_prof": 5},
    14: {"xp": 140000, "bonus_prof": 5},
    15: {"xp": 165000, "bonus_prof": 5},
    16: {"xp": 195000, "bonus_prof": 5},
    17: {"xp": 225000, "bonus_prof": 6},
    18: {"xp": 265000, "bonus_prof": 6},
    19: {"xp": 305000, "bonus_prof": 6},
    20: {"xp": 355000, "bonus_prof": 6},
}

# Slots de magia por nível de personagem e nível de spell
SLOTS_MAGIA = {
    1:  [2, 0, 0, 0, 0, 0, 0, 0, 0],
    2:  [3, 0, 0, 0, 0, 0, 0, 0, 0],
    3:  [4, 2, 0, 0, 0, 0, 0, 0, 0],
    4:  [4, 3, 0, 0, 0, 0, 0, 0, 0],
    5:  [4, 3, 2, 0, 0, 0, 0, 0, 0],
    6:  [4, 3, 3, 0, 0, 0, 0, 0, 0],
    7:  [4, 3, 3, 1, 0, 0, 0, 0, 0],
    8:  [4, 3, 3, 2, 0, 0, 0, 0, 0],
    9:  [4, 3, 3, 3, 1, 0, 0, 0, 0],
    10: [4, 3, 3, 3, 2, 0, 0, 0, 0],
    11: [4, 3, 3, 3, 2, 1, 0, 0, 0],
    12: [4, 3, 3, 3, 2, 1, 0, 0, 0],
    13: [4, 3, 3, 3, 2, 1, 1, 0, 0],
    14: [4, 3, 3, 3, 2, 1, 1, 0, 0],
    15: [4, 3, 3, 3, 2, 1, 1, 1, 0],
    16: [4, 3, 3, 3, 2, 1, 1, 1, 0],
    17: [4, 3, 3, 3, 2, 1, 1, 1, 1],
    18: [4, 3, 3, 3, 3, 1, 1, 1, 1],
    19: [4, 3, 3, 3, 3, 2, 1, 1, 1],
    20: [4, 3, 3, 3, 3, 2, 2, 1, 1],
}

# ─── FUNÇÕES DE CÁLCULO ────────────────────────────────────────────────────────

def calcular_modificador(valor):
    return (valor - 10) // 2


def calcular_bonus_proficiencia(nivel):
    return XP_TABLE.get(nivel, {}).get("bonus_prof", 2)


def calcular_cd_magia(atributo_magia_valor, bonus_prof):
    return 8 + calcular_modificador(atributo_magia_valor) + bonus_prof


def calcular_bonus_ataque_magia(atributo_magia_valor, bonus_prof):
    return calcular_modificador(atributo_magia_valor) + bonus_prof


def calcular_pv_inicial(classe_key, mod_con):
    classe = CLASSES.get(classe_key, {})
    return classe.get("dado_vida", 8) + mod_con


def calcular_pv_nivel(classe_key, nivel, mod_con):
    classe = CLASSES.get(classe_key, {})
    dado = classe.get("dado_vida", 8)
    pv_fixo = classe.get("pv_fixo", 5)
    if nivel <= 1:
        return dado + mod_con
    return dado + mod_con + (nivel - 1) * (pv_fixo + mod_con)


def calcular_percepcao_passiva(mod_sab, prof_percepcao, bonus_prof):
    bonus = bonus_prof if prof_percepcao else 0
    return 10 + mod_sab + bonus
