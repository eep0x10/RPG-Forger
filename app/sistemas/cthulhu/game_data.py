# ─── CALL OF CTHULHU 7ª EDIÇÃO ─────────────────────────────────────────────────
# Dados do sistema Call of Cthulhu (Chaosium)
# Sistema percentual — características e perícias em 0-100

# ─── CARACTERÍSTICAS ───────────────────────────────────────────────────────────
# Em CoC, características são valores 1-99 (derivados de rolagens 3d6 × 5 ou 2d6+6 × 5)

CARACTERISTICAS = ["for", "con", "tam", "des", "apa", "edu", "int", "pod"]

CARACTERISTICAS_LABELS = {
    "for": "Força (FOR)",
    "con": "Constituição (CON)",
    "tam": "Tamanho (TAM)",
    "des": "Destreza (DES)",
    "apa": "Aparência (APA)",
    "edu": "Educação (EDU)",
    "int": "Inteligência (INT)",
    "pod": "Poder (POD)",
}

CARACTERISTICAS_ABREV = {
    "for": "FOR",
    "con": "CON",
    "tam": "TAM",
    "des": "DES",
    "apa": "APA",
    "edu": "EDU",
    "int": "INT",
    "pod": "POD",
}

# Rolagem padrão por característica (em múltiplos de 5)
CARACTERISTICAS_ROLAGEM = {
    "for": "3d6 × 5",
    "con": "3d6 × 5",
    "tam": "(2d6+6) × 5",
    "des": "3d6 × 5",
    "apa": "3d6 × 5",
    "edu": "(2d6+6) × 5",
    "int": "(2d6+6) × 5",
    "pod": "3d6 × 5",
}

# ─── OCUPAÇÕES ─────────────────────────────────────────────────────────────────

OCUPACOES = {
    "antiquario": {
        "nome": "Antiquário",
        "descricao": "Especialista em objetos antigos e raridades. Frequentemente se depara com artefatos de origem duvidosa.",
        "credito_minimo": 30,
        "credito_maximo": 70,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 4",
        "pericias_ocupacao": [
            "Avaliação", "Arte/Artesanato (qualquer)", "História",
            "Biblioteconomia", "Persuasão", "Língua (qualquer)",
            "uma à escolha", "uma à escolha",
        ],
    },
    "detetive": {
        "nome": "Detetive Particular",
        "descricao": "Investigador particular que resolve casos que a polícia ignora ou não consegue resolver.",
        "credito_minimo": 20,
        "credito_maximo": 45,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 2 + (DES ou FOR) × 2",
        "pericias_ocupacao": [
            "Arte/Artesanato (Fotografia)", "Disfarce", "Direito",
            "Intimidação", "Lábia", "Percepção",
            "Psicologia", "uma à escolha",
        ],
    },
    "doutor_medico": {
        "nome": "Médico",
        "descricao": "Profissional de medicina com conhecimento de anatomia e ciências biológicas.",
        "credito_minimo": 30,
        "credito_maximo": 80,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 4",
        "pericias_ocupacao": [
            "Primeiros Socorros", "Medicina", "Psicologia",
            "Ciências (Biologia ou Farmacologia)", "Língua Estrangeira (Latim)",
            "uma à escolha", "uma à escolha", "uma à escolha",
        ],
    },
    "jornalista": {
        "nome": "Jornalista",
        "descricao": "Repórter em busca de furos. Sempre no lugar errado na hora errada.",
        "credito_minimo": 9,
        "credito_maximo": 30,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 4",
        "pericias_ocupacao": [
            "Arte/Artesanato (Fotografia ou Digitação)", "Biblioteconomia",
            "História", "Língua Nativa", "Lábia",
            "Percepção", "Psicologia", "uma à escolha",
        ],
    },
    "estudante": {
        "nome": "Estudante",
        "descricao": "Jovem universitário em busca de conhecimento, frequentemente em áreas das ciências ocultas.",
        "credito_minimo": 5,
        "credito_maximo": 25,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 4",
        "pericias_ocupacao": [
            "Biblioteconomia", "Ciências (qualquer)",
            "História", "Língua Estrangeira (qualquer)",
            "uma à escolha", "uma à escolha", "uma à escolha", "uma à escolha",
        ],
    },
    "policial": {
        "nome": "Policial",
        "descricao": "Agente da lei que investiga crimes e mantém a ordem pública.",
        "credito_minimo": 20,
        "credito_maximo": 40,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 2 + DES × 2",
        "pericias_ocupacao": [
            "Armas de Fogo", "Esquiva", "Intimidação",
            "Lábia", "Luta", "Percepção",
            "Psicologia", "uma à escolha",
        ],
    },
    "professor": {
        "nome": "Professor",
        "descricao": "Acadêmico especialista em um campo do conhecimento.",
        "credito_minimo": 20,
        "credito_maximo": 60,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 4",
        "pericias_ocupacao": [
            "Biblioteconomia", "Ciências (qualquer 2)",
            "História", "Língua Estrangeira (qualquer)",
            "Língua Nativa", "Persuasão",
            "uma à escolha", "uma à escolha",
        ],
    },
    "artista": {
        "nome": "Artista",
        "descricao": "Criativo que vive de sua arte — pintor, escritor, músico, ator.",
        "credito_minimo": 9,
        "credito_maximo": 50,
        "atributo_credito": "apa",
        "pontos_ocupacao": "EDU × 2 + APA × 2",
        "pericias_ocupacao": [
            "Arte/Artesanato (qualquer, 2×)", "História",
            "Língua Nativa", "Percepção",
            "Psicologia", "uma à escolha", "uma à escolha",
        ],
    },
    "soldado": {
        "nome": "Soldado",
        "descricao": "Veterano militar com treinamento em combate e sobrevivência.",
        "credito_minimo": 9,
        "credito_maximo": 30,
        "atributo_credito": "edu",
        "pontos_ocupacao": "EDU × 2 + (DES ou FOR) × 2",
        "pericias_ocupacao": [
            "Armas de Fogo", "Esquiva", "Luta",
            "Primeiros Socorros", "Sobrevivência",
            "uma à escolha", "uma à escolha", "uma à escolha",
        ],
    },
}

# ─── PERÍCIAS ──────────────────────────────────────────────────────────────────
# Cada perícia tem: base (%), característica vinculada, categoria

PERICIAS = {
    # Combate
    "Armas de Fogo":        {"base": 20, "char": "des",  "categoria": "combate"},
    "Armas Pesadas":        {"base": 10, "char": "des",  "categoria": "combate"},
    "Artilharia":           {"base": 15, "char": "des",  "categoria": "combate"},
    "Esquiva":              {"base": None, "char": "des", "categoria": "combate",  "formula": "DES // 2"},
    "Lança de Haste":       {"base": 20, "char": "for",  "categoria": "combate"},
    "Luta":                 {"base": 25, "char": "for",  "categoria": "combate"},
    # Perícias gerais
    "Alpinismo":            {"base": 20, "char": "des",  "categoria": "fisico"},
    "Arqueologia":          {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Arte/Artesanato":      {"base": 5,  "char": "des",  "categoria": "social"},
    "Astronomia":           {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Avaliação":            {"base": 5,  "char": "edu",  "categoria": "academico"},
    "Biblioteconomia":      {"base": 20, "char": "edu",  "categoria": "academico"},
    "Ciências":             {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Crédito":              {"base": None, "char": "apa", "categoria": "social", "formula": "ver ocupação"},
    "Direito":              {"base": 5,  "char": "edu",  "categoria": "academico"},
    "Direção":              {"base": 20, "char": "des",  "categoria": "fisico"},
    "Disfarce":             {"base": 5,  "char": "apa",  "categoria": "social"},
    "Eletrônica":           {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Encantamento":         {"base": 5,  "char": "apa",  "categoria": "social"},
    "Escuta":               {"base": 20, "char": "int",  "categoria": "percep"},
    "Escalar":              {"base": 20, "char": "des",  "categoria": "fisico"},
    "Furtividade":          {"base": 20, "char": "des",  "categoria": "fisico"},
    "Hipnose":              {"base": 1,  "char": "edu",  "categoria": "social"},
    "História":             {"base": 5,  "char": "edu",  "categoria": "academico"},
    "Intimidação":          {"base": 15, "char": "for",  "categoria": "social"},
    "Lábia":                {"base": 5,  "char": "edu",  "categoria": "social"},
    "Língua Estrangeira":   {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Língua Nativa":        {"base": None, "char": "edu", "categoria": "academico", "formula": "EDU × 1"},
    "Literatura":           {"base": 5,  "char": "edu",  "categoria": "academico"},
    "Medicina":             {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Mecânica":             {"base": 10, "char": "edu",  "categoria": "academico"},
    "Navegação":            {"base": 10, "char": "edu",  "categoria": "academico"},
    "Ocultismo":            {"base": 5,  "char": "edu",  "categoria": "academico"},
    "Percepção":            {"base": 25, "char": "int",  "categoria": "percep"},
    "Persuasão":            {"base": 10, "char": "apa",  "categoria": "social"},
    "Pilotagem":            {"base": 1,  "char": "des",  "categoria": "fisico"},
    "Pistas":               {"base": 25, "char": "int",  "categoria": "percep"},
    "Primeiros Socorros":   {"base": 30, "char": "des",  "categoria": "academico"},
    "Psicologia":           {"base": 10, "char": "edu",  "categoria": "academico"},
    "Química":              {"base": 1,  "char": "edu",  "categoria": "academico"},
    "Saltar":               {"base": 20, "char": "for",  "categoria": "fisico"},
    "Sobrevivência":        {"base": 10, "char": "edu",  "categoria": "fisico"},
    "Natação":              {"base": 20, "char": "des",  "categoria": "fisico"},
}

# ─── ERAS / CENÁRIOS ───────────────────────────────────────────────────────────

ERAS = {
    "1920s": {
        "nome": "Anos 1920",
        "descricao": "A era clássica do CoC. Jazz, Proibição e os Mitos surgindo nas sombras.",
    },
    "moderno": {
        "nome": "Era Moderna",
        "descricao": "Investigações contemporâneas. Tecnologia avançada, mas os Mitos são os mesmos.",
    },
    "guerra": {
        "nome": "Segunda Guerra Mundial",
        "descricao": "Conflito mundial e horrores que vão além das trincheiras.",
    },
    "vitoriano": {
        "nome": "Era Vitoriana / Gaslight",
        "descricao": "Final do séc. XIX. Névoa, vapor e mistérios nas ruas de Londres.",
    },
}

# ─── TRANSTORNOS MENTAIS ────────────────────────────────────────────────────────

TRANSTORNOS = [
    "Amnésia",
    "Ansiedade",
    "Compulsão (especificar)",
    "Delírios de grandeza",
    "Dependência química",
    "Depressão",
    "Esquizofrenia",
    "Fobia (especificar)",
    "Histeria",
    "Megalomania",
    "Paranoia",
    "Personalidade múltipla",
    "PTSD",
]

# ─── FUNÇÕES DE CÁLCULO ────────────────────────────────────────────────────────

def calcular_pv(con, tam):
    """PV = (CON + TAM) // 10"""
    return (con + tam) // 10


def calcular_pm(pod):
    """Pontos de Magia = POD // 5"""
    return pod // 5


def calcular_san_inicial(pod):
    """Sanidade inicial = POD"""
    return pod


def calcular_san_maxima(conhecimento_mitos):
    """SAN máxima = 99 - Conhecimento dos Mitos"""
    return max(0, 99 - conhecimento_mitos)


def calcular_movimento(for_val, des_val, tam):
    """Movimento em metros por rodada (padrão CoC 7e)."""
    if for_val < tam and des_val < tam:
        return 7
    elif for_val >= tam or des_val >= tam:
        return 8
    else:
        return 9


def calcular_bonus_dano(for_val, tam):
    """Bonus de dano por FOR+TAM."""
    total = for_val + tam
    if total <= 12:
        return "-1d6"
    elif total <= 16:
        return "-1d4"
    elif total <= 24:
        return "Nenhum"
    elif total <= 32:
        return "+1d4"
    elif total <= 40:
        return "+1d6"
    else:
        return "+2d6"


def calcular_construcao(for_val, tam):
    """Construção física (afeta PV e dano)."""
    total = for_val + tam
    if total <= 64:
        return -2
    elif total <= 84:
        return -1
    elif total <= 124:
        return 0
    elif total <= 164:
        return 1
    else:
        return 2


def nivel_pericia(valor):
    """Retorna os níveis de teste da perícia: regular, hard (½), extreme (⅕)"""
    return {
        "regular": valor,
        "hard": valor // 2,
        "extreme": valor // 5,
    }
