# ─── OLD DRAGON 2e ─────────────────────────────────────────────────────────────
# Dados do sistema Old Dragon 2ª Edição (Retropunk Editora)

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
        "descricao": "Versáteis e ambiciosos, os humanos são a raça mais comum de Arton.",
        "bonus_atributos": {},
        "habilidades": [
            "Versátil: +1 em dois atributos à sua escolha na criação",
            "Determinação: 1x/dia, pode rolar novamente qualquer teste",
        ],
        "restricoes": [],
    },
    "anao": {
        "nome": "Anão",
        "descricao": "Robustos e teimosos, especialistas em mineração e combate subterrâneo.",
        "bonus_atributos": {"constituicao": 2, "sabedoria": 1, "carisma": -1},
        "habilidades": [
            "Visão no Escuro: 18m em escuridão total",
            "Resistência Anã: +2 em Testes de Resistência contra veneno",
            "Familiaridade com Pedra: +2 em testes de percepção em ambiente subterrâneo",
        ],
        "restricoes": ["Não podem ser Magos"],
    },
    "elfo": {
        "nome": "Elfo",
        "descricao": "Graciosos e de vida longa, ligados à magia e à natureza.",
        "bonus_atributos": {"destreza": 2, "inteligencia": 1, "constituicao": -1},
        "habilidades": [
            "Visão no Escuro: 18m em escuridão total",
            "Imunidade a Sono e Charme mágicos",
            "Proficiência com arco longo e espada longa",
        ],
        "restricoes": ["Não podem ser Anões"],
    },
    "halfling": {
        "nome": "Halfling",
        "descricao": "Pequenos e ágeis, sortudos e amantes do conforto.",
        "bonus_atributos": {"destreza": 2, "carisma": 1, "forca": -1},
        "habilidades": [
            "Sorte Halfling: 1x/sessão pode forçar rerolagem de qualquer dado (seu ou do adversário)",
            "Furtivo: Vantagem em testes de Furtividade",
            "Pequenino: Ocupa apenas meia praça em combate",
        ],
        "restricoes": ["Não podem ser Guerreiros de nível acima de 6"],
    },
    "gnomo": {
        "nome": "Gnomo",
        "descricao": "Inventivos e curiosos, especialistas em ilusão e maquinaria.",
        "bonus_atributos": {"inteligencia": 2, "destreza": 1, "forca": -2},
        "habilidades": [
            "Prestidigitação Natural: conhecem 2 truques de ilusão menores",
            "Visão no Escuro: 18m",
            "Afiliação Técnica: proficiência com ferramentas de artesão",
        ],
        "restricoes": [],
    },
    "meio_elfo": {
        "nome": "Meio-Elfo",
        "descricao": "Herdeiros de dois mundos, equilibrados entre humanos e elfos.",
        "bonus_atributos": {"carisma": 2},
        "habilidades": [
            "Visão no Escuro: 18m",
            "Diplomacia: +2 em testes de interação social",
            "Versatilidade Élfica: proficiência em 2 perícias à escolha",
        ],
        "restricoes": [],
    },
    "meio_orc": {
        "nome": "Meio-Orc",
        "descricao": "Guerreiros natos, com sangue selvagem nas veias.",
        "bonus_atributos": {"forca": 2, "constituicao": 1, "inteligencia": -1, "carisma": -1},
        "habilidades": [
            "Resistência Implacável: quando reduzido a 0 PV, fica com 1 PV (1x/descanso longo)",
            "Ataques Selvagens: críticos com armas causam dado de dano extra",
            "Intimidação: +2 em testes de Intimidação",
        ],
        "restricoes": [],
    },
}

# ─── CLASSES ───────────────────────────────────────────────────────────────────

CLASSES = {
    "guerreiro": {
        "nome": "Guerreiro",
        "descricao": "Mestres do combate, especialistas em armas e armaduras.",
        "dado_vida": 10,
        "pv_fixo": 6,
        "atributo_principal": "forca",
        "atributos_secundarios": ["destreza", "constituicao"],
        "proficiencias": ["todas as armas", "todas as armaduras", "escudos"],
        "pericias": ["Atletismo", "Intimidação", "Percepção", "Sobrevivência"],
        "qtd_pericias": 2,
        "magias": False,
        "ataques_por_nivel": {1: 1, 5: 2, 11: 3, 17: 4},
    },
    "mago": {
        "nome": "Mago",
        "descricao": "Estudiosos da magia arcana, capazes de lançar feitiços poderosos.",
        "dado_vida": 4,
        "pv_fixo": 2,
        "atributo_principal": "inteligencia",
        "atributos_secundarios": ["sabedoria"],
        "proficiencias": ["adagas", "dardos", "fundas", "bastão", "bordão"],
        "pericias": ["Arcana", "História", "Investigação", "Medicina", "Natureza", "Religião"],
        "qtd_pericias": 2,
        "magias": True,
        "escola_magias": True,
    },
    "clerigo": {
        "nome": "Clérigo",
        "descricao": "Campeões divinos que canalizam o poder de seus deuses.",
        "dado_vida": 8,
        "pv_fixo": 4,
        "atributo_principal": "sabedoria",
        "atributos_secundarios": ["constituicao"],
        "proficiencias": ["armas simples", "armaduras leves", "armaduras médias", "escudos"],
        "pericias": ["História", "Intuição", "Medicina", "Persuasão", "Religião"],
        "qtd_pericias": 2,
        "magias": True,
        "divindade": True,
    },
    "ladrao": {
        "nome": "Ladrão",
        "descricao": "Especialistas em furtividade, roubo e trapaça.",
        "dado_vida": 6,
        "pv_fixo": 3,
        "atributo_principal": "destreza",
        "atributos_secundarios": ["inteligencia"],
        "proficiencias": ["armas simples", "besta de mão", "espada longa", "espada curta", "rapieira",
                          "armaduras leves", "ferramentas de ladrão"],
        "pericias": ["Acrobacia", "Atletismo", "Enganação", "Furtividade", "Intimidação",
                     "Investigação", "Percepção", "Persuasão", "Prestidigitação"],
        "qtd_pericias": 4,
        "magias": False,
        "ataque_furtivo": True,
    },
    "barbaro": {
        "nome": "Bárbaro",
        "descricao": "Guerreiros selvagens que entram em fúria durante o combate.",
        "dado_vida": 12,
        "pv_fixo": 7,
        "atributo_principal": "forca",
        "atributos_secundarios": ["constituicao"],
        "proficiencias": ["todas as armas", "armaduras leves", "armaduras médias", "escudos"],
        "pericias": ["Adestramento", "Atletismo", "Intimidação", "Natureza", "Percepção", "Sobrevivência"],
        "qtd_pericias": 2,
        "magias": False,
        "furia": True,
    },
    "druida": {
        "nome": "Druida",
        "descricao": "Guardiões da natureza com poderes de transformação e magia natural.",
        "dado_vida": 8,
        "pv_fixo": 4,
        "atributo_principal": "sabedoria",
        "atributos_secundarios": ["inteligencia"],
        "proficiencias": ["clavas", "adagas", "dardos", "azagaias", "maças", "cajados", "cimitarras",
                          "foices", "fundas", "lanças", "armaduras leves", "armaduras médias", "escudos (exceto metal)"],
        "pericias": ["Adestramento", "Arcana", "Intuição", "Medicina", "Natureza", "Percepção", "Religião", "Sobrevivência"],
        "qtd_pericias": 2,
        "magias": True,
        "transformacao": True,
    },
    "paladino": {
        "nome": "Paladino",
        "descricao": "Guerreiros sagrados que juram lealdade a um ideal ou divindade.",
        "dado_vida": 10,
        "pv_fixo": 6,
        "atributo_principal": "carisma",
        "atributos_secundarios": ["forca", "constituicao"],
        "proficiencias": ["todas as armas", "todas as armaduras", "escudos"],
        "pericias": ["Atletismo", "Intuição", "Intimidação", "Medicina", "Persuasão", "Religião"],
        "qtd_pericias": 2,
        "magias": True,
        "imposicao_de_maos": True,
    },
    "ranger": {
        "nome": "Caçador",
        "descricao": "Exploradores das fronteiras, rastreadores e arqueiros habilidosos.",
        "dado_vida": 10,
        "pv_fixo": 6,
        "atributo_principal": "destreza",
        "atributos_secundarios": ["sabedoria", "forca"],
        "proficiencias": ["todas as armas", "armaduras leves", "armaduras médias", "escudos"],
        "pericias": ["Adestramento", "Atletismo", "Furtividade", "Intuição", "Investigação",
                     "Natureza", "Percepção", "Sobrevivência"],
        "qtd_pericias": 3,
        "magias": True,
        "inimigo_favorito": True,
    },
}

# ─── ALINHAMENTOS ──────────────────────────────────────────────────────────────

ALINHAMENTOS = {
    "leal_bom":    "Leal e Bom",
    "neutro_bom":  "Neutro e Bom",
    "caótico_bom": "Caótico e Bom",
    "leal_neutro": "Leal e Neutro",
    "neutro":      "Neutro",
    "caotico_neutro": "Caótico e Neutro",
    "leal_mau":    "Leal e Mau",
    "neutro_mau":  "Neutro e Mau",
    "caotico_mau": "Caótico e Mau",
}

# ─── PERÍCIAS ──────────────────────────────────────────────────────────────────

PERICIAS = {
    "Acrobacia":      "destreza",
    "Adestramento":   "sabedoria",
    "Arcana":         "inteligencia",
    "Atletismo":      "forca",
    "Enganação":      "carisma",
    "Furtividade":    "destreza",
    "História":       "inteligencia",
    "Intimidação":    "carisma",
    "Intuição":       "sabedoria",
    "Investigação":   "inteligencia",
    "Medicina":       "sabedoria",
    "Natureza":       "inteligencia",
    "Percepção":      "sabedoria",
    "Performance":    "carisma",
    "Persuasão":      "carisma",
    "Prestidigitação":"destreza",
    "Religião":       "inteligencia",
    "Sobrevivência":  "sabedoria",
}

# ─── PROGRESSÃO DE NÍVEL ───────────────────────────────────────────────────────

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

# ─── ARMADURAS ─────────────────────────────────────────────────────────────────

ARMADURAS = [
    {"nome": "Sem Armadura",       "ca_base": 10, "tipo": "nenhuma",  "req_forca": 0,  "furtividade": False},
    {"nome": "Couro",              "ca_base": 11, "tipo": "leve",     "req_forca": 0,  "furtividade": False},
    {"nome": "Couro Batido",       "ca_base": 12, "tipo": "leve",     "req_forca": 0,  "furtividade": False},
    {"nome": "Camisão de Malhas",  "ca_base": 13, "tipo": "leve",     "req_forca": 0,  "furtividade": False},
    {"nome": "Malha Grossa",       "ca_base": 14, "tipo": "media",    "req_forca": 0,  "furtividade": True},
    {"nome": "Brunea",             "ca_base": 14, "tipo": "media",    "req_forca": 0,  "furtividade": True},
    {"nome": "Cota de Malha",      "ca_base": 15, "tipo": "media",    "req_forca": 0,  "furtividade": True},
    {"nome": "Meia Armadura",      "ca_base": 15, "tipo": "media",    "req_forca": 0,  "furtividade": True},
    {"nome": "Peitoral",           "ca_base": 14, "tipo": "pesada",   "req_forca": 10, "furtividade": True},
    {"nome": "Armadura de Placas", "ca_base": 17, "tipo": "pesada",   "req_forca": 13, "furtividade": True},
    {"nome": "Armadura Completa",  "ca_base": 18, "tipo": "pesada",   "req_forca": 15, "furtividade": True},
    {"nome": "Escudo",             "ca_base": 2,  "tipo": "escudo",   "req_forca": 0,  "furtividade": False},
]

# ─── ARMAS ─────────────────────────────────────────────────────────────────────

ARMAS = [
    {"nome": "Adaga",           "dano": "1d4",  "tipo": "perfurante", "propriedades": ["ágil", "arremessável", "leve"]},
    {"nome": "Maça",            "dano": "1d6",  "tipo": "concussão",  "propriedades": ["simples"]},
    {"nome": "Cajado",          "dano": "1d6",  "tipo": "concussão",  "propriedades": ["versátil (1d8)"]},
    {"nome": "Azagaia",         "dano": "1d6",  "tipo": "perfurante", "propriedades": ["arremessável"]},
    {"nome": "Lança",           "dano": "1d6",  "tipo": "perfurante", "propriedades": ["versátil (1d8)"]},
    {"nome": "Arco Curto",      "dano": "1d6",  "tipo": "perfurante", "propriedades": ["à distância (18/60m)", "munição"]},
    {"nome": "Espada Curta",    "dano": "1d6",  "tipo": "perfurante", "propriedades": ["ágil", "certeira", "leve"]},
    {"nome": "Machado de Mão",  "dano": "1d6",  "tipo": "cortante",   "propriedades": ["leve", "arremessável"]},
    {"nome": "Espada Longa",    "dano": "1d8",  "tipo": "cortante",   "propriedades": ["versátil (1d10)"]},
    {"nome": "Machado de Batalha","dano":"1d8",  "tipo": "cortante",   "propriedades": ["versátil (1d10)"]},
    {"nome": "Maça de Armas",   "dano": "1d8",  "tipo": "concussão",  "propriedades": []},
    {"nome": "Arco Longo",      "dano": "1d8",  "tipo": "perfurante", "propriedades": ["à distância (45/180m)", "munição", "pesada", "duas mãos"]},
    {"nome": "Alabarda",        "dano": "1d10", "tipo": "cortante",   "propriedades": ["pesada", "alcance", "duas mãos"]},
    {"nome": "Espada Grande",   "dano": "2d6",  "tipo": "cortante",   "propriedades": ["pesada", "duas mãos"]},
    {"nome": "Machado Grande",  "dano": "1d12", "tipo": "cortante",   "propriedades": ["pesada", "duas mãos"]},
]

# ─── FUNÇÕES DE CÁLCULO ────────────────────────────────────────────────────────

def calcular_modificador(valor):
    """Modificador de atributo padrão D20: (valor - 10) // 2"""
    return (valor - 10) // 2


def calcular_bonus_proficiencia(nivel):
    return XP_TABLE.get(nivel, {}).get("bonus_prof", 2)


def calcular_ca(armadura_nome, mod_dex, escudo=False):
    """Calcula CA baseada na armadura equipada."""
    armadura = next((a for a in ARMADURAS if a["nome"] == armadura_nome), ARMADURAS[0])
    if armadura["tipo"] in ("pesada",):
        ca = armadura["ca_base"]
    elif armadura["tipo"] in ("media",):
        ca = armadura["ca_base"] + min(mod_dex, 2)
    else:
        ca = armadura["ca_base"] + mod_dex
    if escudo:
        ca += 2
    return ca


def calcular_pv_inicial(classe_key, mod_con):
    """PV inicial = dado de vida máximo + modificador de CON."""
    classe = CLASSES.get(classe_key, {})
    return classe.get("dado_vida", 8) + mod_con


def calcular_pv_nivel(classe_key, nivel, mod_con):
    """PV total pelo nível médio."""
    classe = CLASSES.get(classe_key, {})
    dado = classe.get("dado_vida", 8)
    pv_fixo = classe.get("pv_fixo", 4)
    if nivel <= 1:
        return dado + mod_con
    return dado + mod_con + (nivel - 1) * (pv_fixo + mod_con)
