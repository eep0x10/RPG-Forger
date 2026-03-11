# Dados do jogo Feiticeiros & Maldições v2.5.2

XP_TABLE = {
    1: {"xp": 0, "bonus_treinamento": 2},
    2: {"xp": 1000, "bonus_treinamento": 2},
    3: {"xp": 3000, "bonus_treinamento": 2},
    4: {"xp": 6000, "bonus_treinamento": 2},
    5: {"xp": 10000, "bonus_treinamento": 3},
    6: {"xp": 15000, "bonus_treinamento": 3},
    7: {"xp": 21000, "bonus_treinamento": 3},
    8: {"xp": 28000, "bonus_treinamento": 3},
    9: {"xp": 36000, "bonus_treinamento": 4},
    10: {"xp": 45000, "bonus_treinamento": 4},
    11: {"xp": 55000, "bonus_treinamento": 4},
    12: {"xp": 66000, "bonus_treinamento": 4},
    13: {"xp": 78000, "bonus_treinamento": 5},
    14: {"xp": 91000, "bonus_treinamento": 5},
    15: {"xp": 105000, "bonus_treinamento": 5},
    16: {"xp": 120000, "bonus_treinamento": 5},
    17: {"xp": 136000, "bonus_treinamento": 6},
    18: {"xp": 153000, "bonus_treinamento": 6},
    19: {"xp": 171000, "bonus_treinamento": 6},
    20: {"xp": 190000, "bonus_treinamento": 6},
}

GRAUS_FEITICEIRO = {
    (1, 4): "4° Grau",
    (5, 7): "3° Grau",
    (8, 13): "2° Grau",
    (14, 18): "1° Grau",
    (19, 20): "Especial",
}

ATRIBUTOS = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "presenca"]
ATRIBUTOS_LABELS = {
    "forca": "Força",
    "destreza": "Destreza",
    "constituicao": "Constituição",
    "inteligencia": "Inteligência",
    "sabedoria": "Sabedoria",
    "presenca": "Presença",
}

VALORES_FIXOS = [15, 14, 13, 12, 10, 8]

POINT_BUY_COSTS = {8: -2, 9: -1, 10: 0, 11: 2, 12: 3, 13: 4, 14: 5, 15: 7}

ORIGENS = {
    "inato": {
        "nome": "Inato",
        "descricao": "Nasceu com afinidade para energia amaldiçoada e uma técnica própria. A origem mais comum.",
        "exemplos": "Nobara Kugisaki, Kento Nanami",
        "bonus_atributo": "Um atributo +2, outro +1",
        "caracteristicas": [
            {
                "nome": "Bônus em Atributo",
                "desc": "Aumenta um atributo em 2 e outro em 1."
            },
            {
                "nome": "Talento Natural",
                "desc": "Recebe um Talento à escolha no 1° nível. Uma vez a partir do 4° nível, pode receber um talento adicional ao subir de nível."
            },
            {
                "nome": "Marca Registrada",
                "desc": "Recebe um Feitiço adicional com custo reduzido em 1 PE."
            }
        ]
    },
    "herdado_gojo": {
        "nome": "Herdado – Clã Gojo",
        "descricao": "Descende do clã Gojo, com as técnicas Ilimitado e Seis Olhos.",
        "exemplos": "Satoru Gojo",
        "bonus_atributo": "Inteligência ou Sabedoria +2, o outro +1",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Inteligência ou Sabedoria +2, o outro +1."},
            {"nome": "Treinamentos de Clã", "desc": "Treinado em 2 perícias entre Feitiçaria, Percepção e Intuição (ou especialista em uma)."},
            {"nome": "Potencial Lendário", "desc": "Em todo nível par recebe 1 PE adicional. Feitiço extra no 1° nível e nos níveis 5, 10, 15 e 20."}
        ]
    },
    "herdado_inumaki": {
        "nome": "Herdado – Clã Inumaki",
        "descricao": "Clã da Fala Amaldiçoada, com o sigilo característico ao redor da boca.",
        "exemplos": "Toge Inumaki",
        "bonus_atributo": "Inteligência ou Presença +2, o outro +1",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Inteligência ou Presença +2, o outro +1."},
            {"nome": "Treinamentos de Clã", "desc": "Treinado em 2 perícias entre Feitiçaria, Percepção e Intuição (ou especialista em uma)."},
            {"nome": "Olhos de Cobra e Presas", "desc": "Número de vezes igual ao bônus de treinamento, pode dar comando de ação bônus para um aliado como reação. Recupera após descanso longo."}
        ]
    },
    "herdado_kamo": {
        "nome": "Herdado – Clã Kamo",
        "descricao": "Clã que valoriza laços de sangue com a técnica Manipulação de Sangue.",
        "exemplos": "Noritoshi Kamo",
        "bonus_atributo": "Constituição ou Sabedoria +2, o outro +1",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Constituição ou Sabedoria +2, o outro +1."},
            {"nome": "Treinamentos de Clã", "desc": "Treinado em 2 perícias entre Atletismo, Medicina e Persuasão (ou especialista em uma)."},
            {"nome": "Valor do Sangue", "desc": "Ao subir de nível, PV máximo aumenta em 1 adicional. A partir do nível 10, soma o mod. de Constituição ao total."}
        ]
    },
    "herdado_zenin": {
        "nome": "Herdado – Clã Zenin",
        "descricao": "Clã poderoso com técnicas variadas: Dez Sombras, Projeção.",
        "exemplos": "Megumi Fushiguro, Maki Zenin",
        "bonus_atributo": "Qualquer atributo +2, outro +1",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Um atributo +2, outro +1 (qualquer)."},
            {"nome": "Treinamentos de Clã", "desc": "Treinado em 2 perícias quaisquer (ou especialista em uma)."},
            {"nome": "Foco no Poder", "desc": "No 1° nível, escolhe um Feitiço Focado. Nos níveis 5, 10, 15 e 20 pode escolher outro. Um Feitiço Focado pode: +1 dado de dano, +1 dado de cura, dobrar o alcance, ou CD +bônus de treinamento."}
        ]
    },
    "herdado_personalizado": {
        "nome": "Herdado – Clã Personalizado",
        "descricao": "Você pertence a um clã de feiticeiros com suas próprias tradições, técnicas e segredos herdados de geração em geração.",
        "exemplos": "Qualquer clã criado pelo jogador",
        "bonus_atributo": "Um atributo +2, outro +1 (livre)",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Um atributo +2, outro +1 (livre escolha)."},
            {"nome": "Treinamentos de Clã", "desc": "Treinado em 2 perícias à escolha do jogador (ou especialista em uma)."},
            {"nome": "Habilidade do Clã", "desc": "Define uma habilidade especial única para o seu clã, criada pelo jogador em conjunto com o Narrador."}
        ]
    },
    "derivado": {
        "nome": "Derivado",
        "descricao": "Energia derivada de fonte alternativa (objeto amaldiçoado, alteração na alma).",
        "exemplos": "Yuuji Itadori, Junpei",
        "bonus_atributo": "Um atributo +2, outro +1",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Um atributo +2, outro +1."},
            {"nome": "Energia Antinatural", "desc": "Recebe uma Aptidão Amaldiçoada de Aura. Como Ação Bônus, recupera PE igual ao dobro do bônus de treinamento uma vez por dia."},
            {"nome": "Desenvolvimento Inesperado", "desc": "A cada 4 níveis, recebe um ponto de atributo adicional e o limite do atributo escolhido aumenta em 1."}
        ]
    },
    "restringido": {
        "nome": "Restringido",
        "descricao": "Energia quase nula, físico extraordinário. Vinculado à especialização Restringido.",
        "exemplos": "Toji Fushiguro",
        "bonus_atributo": "Força, Destreza e Constituição +1 + 2 pontos adicionais em atributos físicos",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Força, Destreza e Constituição +1, mais 2 pontos adicionais para atributos físicos."},
            {"nome": "Físico Abençoado", "desc": "Deslocamento +3m, imune a doenças mundanas, vantagem contra venenos. Acesso à especialização Restringido."},
            {"nome": "Ápice Corporal Humano", "desc": "Limite de Força, Destreza e Constituição é 30. A cada 6 níveis, +2 em um desses atributos."},
            {"nome": "Resiliência Imediata", "desc": "Número de vezes igual ao bônus de treinamento, ao receber dano pode reduzir em nível/2 × 5 (mín. 1)."}
        ]
    },
    "feto_amaldicado": {
        "nome": "Feto Amaldiçoado Híbrido",
        "descricao": "Híbrido entre humano e maldição, com anatomia única e capacidade maldita.",
        "exemplos": "Choso",
        "bonus_atributo": "Um atributo +2, outro +1",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "Um atributo +2, outro +1."},
            {"nome": "Herança Maldita", "desc": "Cura de energia reversa reduzida à metade (exceto se usar EA diretamente). Pode usar energia amaldiçoada como reversa gastando 2x."},
            {"nome": "Físico Amaldiçoado", "desc": "Recebe uma Característica de Anatomia. A cada 5 níveis, recebe mais uma."},
            {"nome": "Vigor Maldito", "desc": "Uma vez por descanso longo, ação bônus para curar 5 + mod. Constituição. Nos níveis 4, 8 e 12 recebe uso adicional e cura +5."}
        ]
    },
    "sem_tecnica": {
        "nome": "Sem Técnica",
        "descricao": "Sem técnica inata, compensam com dedicação extrema e domínio de perícias.",
        "exemplos": "Kasumi Miwa, Atsuya Kusakabe",
        "bonus_atributo": "4 pontos para distribuir (máx. 3 no mesmo atributo)",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "4 pontos para distribuir (máx. 3 no mesmo atributo). Não tem acesso a Feitiços nem à especialização Especialista em Técnica."},
            {"nome": "Estudos Dedicados", "desc": "Treinado em 2 perícias à escolha."},
            {"nome": "Empenho Implacável", "desc": "Bônus progressivos por nível: talentos, bônus em perícias, habilidades extras. No 4° nível, acesso ao Novo Estilo da Sombra e Domínio Simples."}
        ]
    },
    "corpo_amaldicado": {
        "nome": "Corpo Amaldiçoado Mutante",
        "descricao": "Forma de vida artificial com múltiplos núcleos e energia renovável.",
        "exemplos": "Panda",
        "bonus_atributo": "2 pontos adicionais",
        "caracteristicas": [
            {"nome": "Bônus em Atributo", "desc": "2 pontos adicionais para distribuir."},
            {"nome": "Forma de Vida Sintética", "desc": "Imune a veneno e à condição envenenado. Não recebe efeitos de refeições ou itens de Medicina."},
            {"nome": "Mutação Abrupta", "desc": "Inicia com 3 núcleos (escolhe um como Primário). Trocar de núcleo é Ação Bônus. Desenvolvimento especial por nível."}
        ]
    },
}

ESPECIALIZACOES = {
    "lutador": {
        "nome": "Lutador",
        "descricao": "Combate físico, resistência, mobilidade e potência. Manobras de combo.",
        "exemplos": "Yuuji Itadori, Kinji Hakari, Hajime Kashimo",
        "pv_inicial": 12,
        "pv_dado": 10,
        "pv_fixo_nivel": 6,
        "pe_por_nivel": 4,
        "pe_soma_mod": False,
        "atributos_chave": ["forca", "destreza"],
        "req_multiclasse": "Força ou Destreza 16",
        "treinamentos": "Armas Simples, Armas Marciais e Escudo Leve. Fortitude ou Reflexos. Atletismo ou Acrobacia + 3 perícias quaisquer.",
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Corpo Treinado",
                "desc": "Ataques desarmados como ação bônus após ataque desarmado/marcial. Dano desarmado 1d8 (aumenta nos níveis 5, 9, 13, 17). Pode usar Força ou Destreza nos ataques."
            },
            {
                "nivel": 1,
                "nome": "Empolgação",
                "desc": "Começa combate com Empolgação 1. Ao acertar ataque/manobra no turno, sobe um nível (máx. 5). Aprende 2 manobras de Empolgação."
            }
        ],
        "habilidades_nivel": {
            2: ["Reflexo Evasivo – Redução de dano a todo tipo (exceto alma) = nível de Lutador / 2"],
            4: ["Implemento Marcial – +2 na CD (aumenta nos níveis 8 e 16)"],
            5: ["Gosto pela Luta – +2 em ataques desarmados/marciais, +1 em Fortitude e dano"],
            9: ["Teste de Resistência Mestre – Treinado em 2° TR, mestre no da especialização"],
            11: ["Empolgação Máxima – Dados de Empolgação melhorados: 2d4/2d6/2d8/3d6"],
            20: ["Lutador Superior – +1 dado desarmado, 1 ataque desarmado por rodada (ação livre, 2PE), +1 Empolgação inicial"]
        }
    },
    "especialista_combate": {
        "nome": "Especialista em Combate",
        "descricao": "Arte do combate com estratégia, versatilidade e letalidade. Estilos de luta.",
        "exemplos": "Kento Nanami, Yuta Okkotsu, Atsuya Kusakabe",
        "pv_inicial": 12,
        "pv_dado": 10,
        "pv_fixo_nivel": 6,
        "pe_por_nivel": 4,
        "pe_soma_mod": False,
        "atributos_chave": ["forca", "destreza", "sabedoria"],
        "req_multiclasse": "Força ou Destreza 16",
        "treinamentos": "Todas as armas e escudos. Fortitude ou Reflexos. 2 perícias de Ofício/Atletismo/Acrobacia + 3 perícias quaisquer.",
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Repertório do Especialista",
                "desc": "Escolhe um Estilo de Combate no 1° nível (Defensivo, Duelista, Duplo, Massivo, Distante, etc.). Recebe novos estilos nos níveis 6 e 12."
            },
            {
                "nivel": 1,
                "nome": "Artes do Combate",
                "desc": "Pontos de Preparo = nível EC + mod. Sabedoria. Usa para artes especiais de combate (Arremesso Ágil, Distração Letal, Execução Silenciosa, etc.)."
            }
        ],
        "habilidades_nivel": {
            4: ["Golpe Especial – Monta ataques com propriedades extras (gastando PE)", "Implemento Marcial – +2 na CD"],
            6: ["Renovação pelo Sangue – Recupera 1 PE ao acertar crítico ou reduzir inimigo a 0 PV"],
            9: ["Teste de Resistência Mestre"],
            20: ["Autossuficiente – 3 PE temporários por Golpe Especial, +1 dado de dano em todos os ataques"]
        }
    },
    "especialista_tecnica": {
        "nome": "Especialista em Técnica",
        "descricao": "Maximiza energia amaldiçoada e técnica. Altera fundamentos do jujutsu.",
        "exemplos": "Satoru Gojo, Ryomen Sukuna",
        "pv_inicial": 10,
        "pv_dado": 8,
        "pv_fixo_nivel": 5,
        "pe_por_nivel": 6,
        "pe_soma_mod": True,
        "atributos_chave": ["inteligencia", "sabedoria"],
        "req_multiclasse": "Inteligência ou Sabedoria 16",
        "treinamentos": "Armas Simples e a Distância. Astúcia ou Vontade. Feitiçaria, Ocultismo + 2 perícias quaisquer.",
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Domínio dos Fundamentos",
                "desc": "Aprende 2 Mudanças de Fundamento (Feitiço Cruel, Distante, Duplicado, Expansivo, Potente, Preciso, Rápido). Mais 1 no nível 12."
            },
            {
                "nivel": 1,
                "nome": "Conjuração Aprimorada",
                "desc": "Habilidades que melhoram e potencializam a conjuração dos feitiços."
            }
        ],
        "habilidades_nivel": {
            9: ["Teste de Resistência Mestre"],
            20: ["Técnica Absoluta – Habilidade definitiva do Especialista em Técnica"]
        }
    },
    "controlador": {
        "nome": "Controlador",
        "descricao": "Controla Marionetes ou Shikigamis para dominar o campo de batalha.",
        "exemplos": "Megumi Fushiguro (Dez Sombras)",
        "pv_inicial": 10,
        "pv_dado": 8,
        "pv_fixo_nivel": 5,
        "pe_por_nivel": 5,
        "pe_soma_mod": True,
        "atributos_chave": ["presenca", "sabedoria"],
        "req_multiclasse": "Presença ou Sabedoria 16",
        "treinamentos": "Armas Simples e a Distância. Astúcia ou Vontade. Percepção, Persuasão + 2 perícias quaisquer.",
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Treinamento em Controle",
                "desc": "Recebe 2 invocações iniciais (mais nos níveis 3, 6, 9, 10, 12, 15 e 18). +1 invocação ativa em campo. Mais comandos por ação nos níveis 6, 12 e 18."
            }
        ],
        "habilidades_nivel": {
            4: ["Controle Aprimorado – +2 em testes das invocações (+1 por grau acima do 4°)"],
            6: ["Apogeu – Escolhe estilo de controle: Concentrado, Disperso ou Sintonizado"],
            9: ["Teste de Resistência Mestre"],
            10: ["Reserva para Invocação – 1 vez por descanso curto, invoca 2 com custo pela metade ou 1 grátis"],
            20: ["Ápice do Controle – +2 ações/características por invocação, invocar como ação livre"]
        }
    },
    "suporte": {
        "nome": "Suporte",
        "descricao": "Apoia aliados, cura, motiva e abre possibilidades em campo.",
        "exemplos": "Haibara, Shoko Ieiri",
        "pv_inicial": 10,
        "pv_dado": 8,
        "pv_fixo_nivel": 5,
        "pe_por_nivel": 5,
        "pe_soma_mod": True,
        "atributos_chave": ["presenca", "sabedoria"],
        "req_multiclasse": "Presença ou Sabedoria 16",
        "treinamentos": "Armas Simples e Escudos. Astúcia ou Vontade. Medicina, Prestidigitação + 3 perícias quaisquer.",
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Suporte em Combate",
                "desc": "Apoiar como ação bônus. Cura (2d6 + mod Presença/Sab) como ação bônus no toque, mod vezes por descanso. Escala nos níveis 4, 8, 12 e 16."
            }
        ],
        "habilidades_nivel": {
            3: ["Presença Inspiradora – 2 PE para inspirar aliados em 9m (+1 em perícias)"],
            5: ["Versatilidade – 1 PE para rolar perícia não treinada como treinado"],
            6: ["Aptidão: Energia Reversa"],
            8: ["Aptidão: Liberação de Energia Reversa"],
            9: ["Teste de Resistência Mestre"],
            10: ["Medicina Infalível – Maximiza dados de cura, soma bônus de treinamento nas curas"],
            20: ["Suporte Absoluto – Apoiar como ação livre por rodada, usos de cura dobrados"]
        }
    },
    "restringido": {
        "nome": "Restringido",
        "descricao": "Sem energia amaldiçoada, físico sobre-humano e técnicas marciais únicas.",
        "exemplos": "Toji Fushiguro",
        "pv_inicial": 16,
        "pv_dado": 12,
        "pv_fixo_nivel": 7,
        "pe_por_nivel": 0,
        "pe_soma_mod": False,
        "atributos_chave": ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "presenca"],
        "req_multiclasse": "Não pode fazer Multiclasse",
        "treinamentos": "Todas as armas e escudos. Fortitude e Reflexos. 1 perícia de Ofício + 4 quaisquer (exceto Feitiçaria).",
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Restrito pelos Céus",
                "desc": "Adiciona mod. Força ou Constituição na Defesa (limitado pelo nível). Inicia com ferramenta amaldiçoada grau 4 e meio de ver maldições. Pontos de Estamina (4 por nível) no lugar de PE."
            }
        ],
        "habilidades_nivel": {
            2: ["Ataque Furtivo – 1d8 dano extra (escala por nível: 2d8 no 3, 3d8 no 6, etc.)", "Versatilidade – +1 em todas as perícias (+2 no nível 10)"],
            3: ["Esquiva Sobre-humana – +1 Defesa e Reflexos (escala nos níveis 9 e 16)"],
            4: ["Implemento Celeste – +2 na CD (aumenta nos níveis 8 e 16)"],
            9: ["Teste de Resistência Mestre – Mestre nos dois TRs da especialização"],
            10: ["Restrição Definitiva – Vantagem em furtividade vs. usuários de EA, ver alma, armas 1 nível acima, etc."],
            20: ["Libertação do Destino – Resistência a danos físicos + 1 tipo, +5 ataques, +nível/2 no dano"]
        }
    },
}

# Perícias: nome → atributo base
# Graus: nenhum (só atributo) | treinado (+BT) | mestre (+2×BT)
PERICIAS = {
    "Acrobacia":       "destreza",
    "Atletismo":       "forca",
    "Atuação":         "presenca",
    "Condução":        "destreza",
    "Diplomacia":      "presenca",
    "Enganação":       "presenca",
    "Feitiçaria":      "inteligencia",
    "Furtividade":     "destreza",
    "História":        "inteligencia",
    "Intuição":        "sabedoria",
    "Intimidação":     "presenca",
    "Investigação":    "inteligencia",
    "Medicina":        "sabedoria",
    "Natureza":        "inteligencia",
    "Ocultismo":       "inteligencia",
    "Percepção":       "sabedoria",
    "Persuasão":       "presenca",
    "Prestidigitação": "destreza",
    "Religião":        "inteligencia",
    "Sobrevivência":   "sabedoria",
    "Tecnologia":      "inteligencia",
}

ATTR_ABREV = {
    "forca": "FOR", "destreza": "DES", "constituicao": "CON",
    "inteligencia": "INT", "sabedoria": "SAB", "presenca": "PRE",
}

TESTES_RESISTENCIA = ["Fortitude", "Reflexos", "Vontade", "Astúcia"]

ARMAS_INICIAIS = [
    "Espada Curta", "Espada Longa", "Faca", "Machado de Mão",
    "Cajado", "Lança", "Arco Curto", "Arco Longo",
    "Adaga", "Martelo", "Machado de Guerra", "Espada Grande",
    "Faixas/Bandagem", "Nunchaku", "Tonfa", "Katana",
    "Kusarigama", "Shuriken (x10)", "Kunai (x5)", "Mão desarmada (sem arma)"
]

# Dados completos das armas (Livro Básico v2.5.2)
ARMAS_DADOS = {
    "Adaga": {
        "dano": "1d6", "tipo_dano": "Perfurante / Cortante",
        "atributo": "Força ou Destreza", "categoria": "Simples",
        "critico": 18, "alcance": "Corpo a corpo (1,5m) ou arremesso 6/18m",
        "propriedades": ["Apunhaladora", "Arremessável [6/18m]", "Fineza", "Leve", "Marcial", "Modular Ct"],
        "efeito_critico": "",
        "obs": "Apunhaladora: +BT de dano em criaturas desprevenidas. Pode ser arremessada."
    },
    "Espada Curta": {
        "dano": "1d6", "tipo_dano": "Cortante / Perfurante",
        "atributo": "Força ou Destreza", "categoria": "Simples",
        "critico": 19, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Fineza", "Leve", "Marcial", "Modular Pf"],
        "efeito_critico": "",
        "obs": "Leve: usável em combate de duas armas. Fineza: pode usar Destreza."
    },
    "Faca": {
        "dano": "1d6", "tipo_dano": "Perfurante / Cortante",
        "atributo": "Força ou Destreza", "categoria": "Simples",
        "critico": 20, "alcance": "Arremesso 12/24m",
        "propriedades": ["Leve", "Arremessável [12/24m]", "Modular Ct"],
        "efeito_critico": "",
        "obs": "Arma de arremesso. Leva BT×10 unidades."
    },
    "Cajado": {
        "dano": "1d6 / 1d8 (2 mãos)", "tipo_dano": "Impacto",
        "atributo": "Força", "categoria": "Simples",
        "critico": 19, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Ampla", "Dupla", "Marcial", "Versátil"],
        "efeito_critico": "",
        "obs": "Versátil: 1d6 com uma mão, 1d8 com duas. Dupla: usável com Lutando com Duas Armas."
    },
    "Lança": {
        "dano": "1d6 / 1d8 (2 mãos)", "tipo_dano": "Perfurante",
        "atributo": "Força", "categoria": "Simples",
        "critico": 19, "alcance": "Corpo a corpo (1,5m+) ou arremesso 6/18m",
        "propriedades": ["Arremessável [6/18m]", "Estendida", "Versátil"],
        "efeito_critico": "",
        "obs": "Estendida: alcance corpo a corpo +1,5m. Versátil."
    },
    "Machado de Mão": {
        "dano": "1d8 / 1d10 (2 mãos)", "tipo_dano": "Cortante",
        "atributo": "Força", "categoria": "Simples",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Versátil"],
        "efeito_critico": "Criatura adjacente ao alvo recebe metade do dano se Defesa < resultado do crítico.",
        "obs": "Versátil: 1d8 uma mão, 1d10 duas mãos."
    },
    "Martelo": {
        "dano": "1d8 / 1d10 (2 mãos)", "tipo_dano": "Impacto",
        "atributo": "Força", "categoria": "Simples",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Versátil"],
        "efeito_critico": "Alvo faz TR Fortitude vs CD especialização ou fica Derrubado.",
        "obs": "Versátil: 1d8 uma mão, 1d10 duas mãos."
    },
    "Arco Curto": {
        "dano": "1d6", "tipo_dano": "Perfurante",
        "atributo": "Destreza", "categoria": "Simples",
        "critico": 19, "alcance": "24m / 48m (máx)",
        "propriedades": ["Duas Mãos", "Mortal d10", "Alcance [24/48m]"],
        "efeito_critico": "Se alvo adjacente a superfície, fica Imóvel até arrancar projétil (ação bônus).",
        "obs": "Mortal d10: em crítico, +1d10 de dano extra. Não precisa recarregar (usa aljava)."
    },
    "Arco Longo": {
        "dano": "1d10", "tipo_dano": "Perfurante",
        "atributo": "Destreza", "categoria": "Complexa / Marcial",
        "critico": 19, "alcance": "30m / 60m (máx)",
        "propriedades": ["Duas Mãos", "Mortal d12", "Alcance [30/60m]"],
        "efeito_critico": "Se alvo adjacente a superfície, fica Imóvel até arrancar projétil (ação bônus).",
        "obs": "Mortal d12: em crítico, +1d12 de dano extra. Não precisa recarregar (usa aljava)."
    },
    "Espada Longa": {
        "dano": "1d8 / 1d10 (2 mãos)", "tipo_dano": "Cortante / Perfurante",
        "atributo": "Força", "categoria": "Complexa / Marcial",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Modular Pf", "Versátil"],
        "efeito_critico": "",
        "obs": "Versátil: 1d8 uma mão, 1d10 duas mãos. Modular Pf: pode causar dano perfurante."
    },
    "Machado de Guerra": {
        "dano": "1d10", "tipo_dano": "Cortante",
        "atributo": "Força (mín. 16)", "categoria": "Complexa / Marcial",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Ampla", "Duas Mãos", "Pesada [16]"],
        "efeito_critico": "Criatura adjacente ao alvo recebe metade do dano se Defesa < resultado do crítico.",
        "obs": "Duas mãos. Pesada [16]: desvantagem em ataques se Força < 16."
    },
    "Espada Grande": {
        "dano": "1d12", "tipo_dano": "Cortante / Perfurante",
        "atributo": "Força (mín. 14)", "categoria": "Complexa / Marcial",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Ampla", "Duas Mãos", "Modular Pf", "Pesada [14]"],
        "efeito_critico": "",
        "obs": "Duas mãos. Ampla: 1×/rodada criatura adjacente recebe metade do dano. Pesada [14]."
    },
    "Katana": {
        "dano": "1d6 / 1d8 (2 mãos)", "tipo_dano": "Cortante",
        "atributo": "Força ou Destreza", "categoria": "Complexa / Marcial",
        "critico": 19, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Versátil", "Fatal d10", "Fineza"],
        "efeito_critico": "Fatal d10: dado de dano aumenta para d10 (inclusive no dano adicional do crítico).",
        "obs": "Versátil. Fineza: pode usar Destreza. Fatal d10 em acertos críticos."
    },
    "Nunchaku": {
        "dano": "1d8", "tipo_dano": "Impacto",
        "atributo": "Força ou Destreza", "categoria": "Complexa / Marcial",
        "critico": 19, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Dupla", "Enérgica", "Fineza", "Marcial"],
        "efeito_critico": "",
        "obs": "Enérgica: 2º ataque no mesmo turno recebe +dados de dano da arma. Dupla. Fineza."
    },
    "Tonfa": {
        "dano": "1d8", "tipo_dano": "Impacto",
        "atributo": "Força ou Destreza", "categoria": "Complexa / Marcial",
        "critico": 19, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Dupla", "Enérgica", "Fineza", "Marcial"],
        "efeito_critico": "",
        "obs": "Arma de bastão marcial. Enérgica. Dupla. Fineza: pode usar Destreza."
    },
    "Kusarigama": {
        "dano": "1d6 Ct + 1d6 Im", "tipo_dano": "Cortante + Impacto",
        "atributo": "Força", "categoria": "Complexa / Marcial",
        "critico": 19, "alcance": "Corpo a corpo (+1,5m estendido)",
        "propriedades": ["Duas Mãos", "Dupla", "Estendida", "Enérgica"],
        "efeito_critico": "",
        "obs": "+2 em testes de manobra. Foice (dano Ct) ou peso (dano Im) alternável. Estendida: +1,5m de alcance."
    },
    "Shuriken (x10)": {
        "dano": "1d4", "tipo_dano": "Cortante",
        "atributo": "Força ou Destreza", "categoria": "Complexa / Marcial",
        "critico": 18, "alcance": "Arremesso 12/24m",
        "propriedades": ["Arremessável [12/24m]", "Mortal d8", "Leve"],
        "efeito_critico": "Mortal d8: em crítico, +1d8 de dano extra.",
        "obs": "Leva BT×10 unidades. Recupera metade no final do combate."
    },
    "Kunai (x5)": {
        "dano": "1d6", "tipo_dano": "Perfurante",
        "atributo": "Força ou Destreza", "categoria": "Complexa / Marcial",
        "critico": 19, "alcance": "Corpo a corpo ou arremesso 9/18m",
        "propriedades": ["Apunhaladora", "Arremessável [9/18m]", "Fineza", "Leve"],
        "efeito_critico": "",
        "obs": "Apunhaladora: +BT de dano em desprevenidos. Leva BT×10 unidades. Fineza."
    },
    "Faixas/Bandagem": {
        "dano": "Como ataque desarmado", "tipo_dano": "Impacto",
        "atributo": "Força", "categoria": "Simples",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Especial (Pugilato)"],
        "efeito_critico": "Alvo faz TR Fortitude vs CD especialização ou fica Desorientado por 1 rodada.",
        "obs": "Não é arma — ataques com faixas = ataques desarmados. Beneficia habilidades de ataque desarmado. Pode virar Ferramenta Amaldiçoada."
    },
    "Mão desarmada (sem arma)": {
        "dano": "1d4→1d12 (por nível)", "tipo_dano": "Impacto",
        "atributo": "Força", "categoria": "—",
        "critico": 20, "alcance": "Corpo a corpo (1,5m)",
        "propriedades": ["Pugilato"],
        "efeito_critico": "Alvo faz TR Fortitude vs CD especialização ou fica Desorientado por 1 rodada.",
        "obs": "Progressão: Nv1–4: 1d4 / Nv5–8: 1d6 / Nv9–12: 1d8 / Nv13–16: 1d10 / Nv17–20: 1d12. Lutador: começa em 1d8."
    },
}

ESCUDOS_DADOS = {
    "Escudo Pequeno": {
        "rd": 2, "dano_escudo": "1d3 Im", "penalidade": 0,
        "ocupa_mao": False,
        "obs": "Preso ao braço — mantém uma mão livre. Se atacar, perde RD até próximo turno."
    },
    "Escudo Leve": {
        "rd": 2, "dano_escudo": "1d4 Im", "penalidade": -1,
        "ocupa_mao": True,
        "obs": "Pequeno e leve. Penalidade cumulativa com uniforme."
    },
    "Escudo Médio": {
        "rd": 4, "dano_escudo": "1d6 Im", "penalidade": -2,
        "ocupa_mao": True,
        "obs": "Equilibra defesa e agilidade."
    },
    "Escudo Pesado": {
        "rd": 6, "dano_escudo": "1d8 Im", "penalidade": -4,
        "ocupa_mao": True,
        "obs": "Maior sacrifício de agilidade. Maior proteção."
    },
}

FERRAMENTAS_AMALDICADAS_BONUS = {
    "4° Grau":     {"bonus_ataque": "+1", "encantamentos": 0},
    "3° Grau":     {"bonus_ataque": "+2", "encantamentos": 1},
    "2° Grau":     {"bonus_ataque": "+3", "encantamentos": 1},
    "1° Grau":     {"bonus_ataque": "+4", "encantamentos": 2},
    "Grau Especial":{"bonus_ataque": "+5", "encantamentos": "Habilidade Única"},
}

ARMAS_ESPECIAIS_GRAU = {
    "Lâmina da Totalidade": {
        "base": "Espada Longa", "grau": "Grau Especial",
        "propriedades": ["Certeira", "Harmonizada", "Longa", "Sintonizada"],
        "habilidade": "Totalidade Elemental: ao atacar, escolha qualquer tipo de dano elemental — esse se torna o tipo causado.",
    },
    "Véu da Noite": {
        "base": "Adaga", "grau": "Grau Especial",
        "propriedades": ["Certeira", "Discreta", "Fidedigna", "Infalível"],
        "habilidade": "Véu Noturno (Ação Bônus): fica invisível por 1 minuto. Recarrega na próxima noite.",
    },
}

UNIFORMES = [
    {"nome": "Uniforme Comum", "desc": "DEF = 10 + Destreza + Nível/2"},
    {"nome": "Uniforme Reforçado", "desc": "DEF = 12 + Destreza + Nível/2"},
    {"nome": "Armadura Leve", "desc": "DEF = 11 + Destreza + Nível/2"},
]

KITS = [
    "Kit de Ferramentas de Ladrão",
    "Kit Médico",
    "Kit de Herbalismo",
    "Kit de Artesão",
    "Kit de Caligrafia",
    "Kit de Explorador",
    "Instrumentos Musicais",
    "Kit de Disfarce",
]

def calcular_modificador(valor):
    """Calcula o modificador de atributo"""
    return (valor - 10) // 2

def calcular_grau(nivel):
    """Retorna o grau do feiticeiro baseado no nível"""
    for (min_n, max_n), grau in GRAUS_FEITICEIRO.items():
        if min_n <= nivel <= max_n:
            return grau
    return "Especial"

def calcular_pv(especializacao, nivel, mod_con, historico_niveis=None):
    """Calcula PV máximo baseado na especialização e nível"""
    spec = ESPECIALIZACOES.get(especializacao)
    if not spec:
        return 0
    # Nível 1
    pv = spec["pv_inicial"] + mod_con
    # Níveis subsequentes usam valor fixo
    for n in range(2, nivel + 1):
        pv += spec["pv_fixo_nivel"] + mod_con
    return max(1, pv)

def calcular_pe(especializacao, nivel, mod_atributo=0):
    """Calcula PE máximo"""
    spec = ESPECIALIZACOES.get(especializacao)
    if not spec:
        return 0
    if especializacao == "restringido":
        return nivel * 4  # Pontos de Estamina
    pe = spec["pe_por_nivel"] * nivel
    if spec["pe_soma_mod"]:
        pe += mod_atributo
    return pe

def calcular_bonus_treinamento(nivel):
    return XP_TABLE.get(nivel, {}).get("bonus_treinamento", 2)


# ─── INVOCAÇÕES ────────────────────────────────────────────────────────────────

INVOCACAO_GRADES = {
    "4": {
        "nome": "Quarto Grau", "pontos_atributo": 10, "max_atributo": 16,
        "pv_base": 10, "pv_con_tipo": "metade", "pv_nivel_mult": 1.0,
        "def_base": 10, "acoes_caracteristicas": 2, "custo_pe_base": 2,
        "alcance": 6, "pericias_bonus": 1, "acoes_custo_max": 1,
    },
    "3": {
        "nome": "Terceiro Grau", "pontos_atributo": 15, "max_atributo": 20,
        "pv_base": 25, "pv_con_tipo": "metade", "pv_nivel_mult": 1.0,
        "def_base": 12, "acoes_caracteristicas": 2, "custo_pe_base": 4,
        "alcance": 9, "pericias_bonus": 1, "acoes_custo_max": 1,
    },
    "2": {
        "nome": "Segundo Grau", "pontos_atributo": 20, "max_atributo": 24,
        "pv_base": 40, "pv_con_tipo": "total", "pv_nivel_mult": 1.0,
        "def_base": 16, "acoes_caracteristicas": 3, "custo_pe_base": 6,
        "alcance": 15, "pericias_bonus": 2, "acoes_custo_max": 2,
    },
    "1": {
        "nome": "Primeiro Grau", "pontos_atributo": 30, "max_atributo": 26,
        "pv_base": 60, "pv_con_tipo": "total", "pv_nivel_mult": 1.5,
        "def_base": 20, "acoes_caracteristicas": 3, "custo_pe_base": 8,
        "alcance": 21, "pericias_bonus": 2, "acoes_custo_max": 2,
    },
    "especial": {
        "nome": "Grau Especial", "pontos_atributo": 40, "max_atributo": 30,
        "pv_base": 80, "pv_con_tipo": "total", "pv_nivel_mult": 2.0,
        "def_base": 24, "acoes_caracteristicas": 4, "custo_pe_base": 12,
        "alcance": 30, "pericias_bonus": 3, "acoes_custo_max": 3,
    },
}

INVOCACAO_DANO = {
    "jogada_alvo_unico": {"4": "1d12", "3": "1d12+1d6", "2": "2d12", "1": "2d12+1d6", "especial": "3d12"},
    "tr_alvo_unico":     {"4": "1d8",  "3": "1d12",    "2": "1d12+1d6", "1": "2d12",    "especial": "2d12+1d6"},
    "jogada_multiplos":  {"3": "1d10", "2": "1d12",    "1": "1d12+1d6", "especial": "2d12"},
    "jogada_area":       {"3": "1d8",  "2": "1d10",    "1": "1d12",     "especial": "1d12+1d8"},
    "cura_alvo_unico":   {"4": "1d4",  "3": "1d8",     "2": "1d12",     "1": "1d12+1d8", "especial": "2d12+1d6"},
    "cura_multiplos":    {"3": "1d4",  "2": "1d6",     "1": "1d8",      "especial": "1d12+1d4"},
}

INVOCACAO_AREA = {"3": 3.0, "2": 4.5, "1": 6.0, "especial": 7.5}

INVOCACAO_AUXILIO = {
    "bonus_defesa":   {"4": 1, "3": 2, "2": 3, "1": 4, "especial": 5},
    "bonus_acerto":   {"4": 1, "3": 2, "2": 3, "1": 4, "especial": 5},
    "dano_adicional": {"4": "1d6", "3": "1d10", "2": "2d6", "1": "2d8", "especial": "2d12"},
    "reducao_dano":   {"4": 2, "3": 4, "2": 6, "1": 8, "especial": 10},
}

INVOCACAO_CARAC = {
    "aumento_vida": {"4": 5,  "3": 10, "2": 15, "1": 20, "especial": 30},
    "bonus_teste":  {"4": 2,  "3": 4,  "2": 6,  "1": 8,  "especial": 10},
    "reducao_dano": {"4": 2,  "3": 4,  "2": 6,  "1": 8,  "especial": 12},
}

CONTROLADOR_GRADES_ACESSO = {
    (1, 4):   ["4"],
    (5, 8):   ["4", "3"],
    (9, 12):  ["4", "3", "2"],
    (13, 16): ["4", "3", "2", "1"],
    (17, 20): ["4", "3", "2", "1", "especial"],
}

GRADE_ORDEM = ["4", "3", "2", "1", "especial"]
GRADE_NOMES = {"4": "4° Grau", "3": "3° Grau", "2": "2° Grau", "1": "1° Grau", "especial": "Grau Especial"}


def get_grades_acesso(nivel_controlador):
    for (mn, mx), grades in CONTROLADOR_GRADES_ACESSO.items():
        if mn <= nivel_controlador <= mx:
            return grades
    return ["4"]


def calcular_invocacao(inv, nivel_usuario, bt_usuario):
    """Calcula PV, DEF, custo PE e bônus de invocação."""
    grau = inv.get("grau", "4")
    grade = INVOCACAO_GRADES.get(grau, INVOCACAO_GRADES["4"])
    attrs = inv.get("atributos", {})

    con = attrs.get("constituicao", 8)
    dex = attrs.get("destreza", 8)
    mod_dex = (dex - 10) // 2

    # Pontos de Vida
    nivel_contrib = int(nivel_usuario * grade["pv_nivel_mult"])
    if grade["pv_con_tipo"] == "metade":
        pv = grade["pv_base"] + con // 2 + nivel_contrib
    else:
        pv = grade["pv_base"] + con + nivel_contrib

    # Bonus de características de aumento de vida
    for c in inv.get("caracteristicas", []):
        if c.get("tipo") == "aumento_vida":
            pv += INVOCACAO_CARAC["aumento_vida"].get(grau, 0)

    # Defesa
    defesa = grade["def_base"] + mod_dex + bt_usuario

    # Custo PE total = base + extras por slots adicionais
    custo_pe = grade["custo_pe_base"]
    n_base = grade["acoes_caracteristicas"]
    acoes = inv.get("acoes", [])
    caracs = inv.get("caracteristicas", [])
    total_slots = len(acoes) + len(caracs)
    extras = max(0, total_slots - n_base)
    # Each extra slot: complexa = +2 PE, simples/carac = +1 PE
    # We track which are extra in is_extra flag
    for a in acoes:
        if a.get("is_extra"):
            custo_pe += 2 if a.get("tipo") == "complexa" else 1
    for c in caracs:
        if c.get("is_extra"):
            custo_pe += 1

    # Bônus de invocação
    atrib_ataque = inv.get("atrib_ataque", "forca")
    val_chave = attrs.get(atrib_ataque, 8)
    mod_chave = (val_chave - 10) // 2
    bonus_inv = mod_chave + bt_usuario + (nivel_usuario // 2)

    inv["calculado"] = {
        "pv_max": max(1, pv),
        "defesa": defesa,
        "custo_pe_total": custo_pe,
        "bonus_invocacao": bonus_inv,
        "deslocamento": 9,
        "alcance": INVOCACAO_GRADES[grau]["alcance"],
    }
    return inv


# ─── TÉCNICAS AMALDIÇOADAS – TABELAS (Expansão) ───────────────────────────────

# Dano por nível para habilidades ofensivas
TECNICA_DANO_ALVO_TR = {
    0: "1d10", 1: "3d8", 2: "7d8", 3: "12d8", 4: "14d10", 5: "18d12"
}
TECNICA_DANO_ALVO_ATAQUE = {
    0: "1d10", 1: "4d8", 2: "8d8", 3: "14d8", 4: "16d10", 5: "20d12"
}
TECNICA_DANO_AREA_TR = {
    1: "2d8", 2: "4d8", 3: "5d12", 4: "10d10", 5: "12d12"
}
TECNICA_ALCANCE_M = {0: 9, 1: 12, 2: 18, 3: 24, 4: 30, 5: 48}
TECNICA_AREA_M = {1: 4.5, 2: 6.0, 3: 9.0, 4: 12.0, 5: 18.0}

# Tabelas de habilidades auxiliares (Imediata / Duradoura / Sustentada)
TECNICA_AUX_CA = {
    0: {"imediata": 3,  "duradoura": 2,  "sustentada": 2},
    1: {"imediata": 5,  "duradoura": 4,  "sustentada": 4},
    2: {"imediata": 10, "duradoura": 8,  "sustentada": 7},
    3: {"imediata": 14, "duradoura": 11, "sustentada": 10},
    4: {"imediata": 18, "duradoura": 14, "sustentada": 12},
    5: {"imediata": 25, "duradoura": 20, "sustentada": 18},
}
TECNICA_AUX_RD = TECNICA_AUX_CA
TECNICA_AUX_BONUS = TECNICA_AUX_CA

TECNICA_AUX_MOVIMENTO = {
    0: {"imediata": 4.5,  "duradoura": 3.0,  "sustentada": 3.0},
    1: {"imediata": 6.0,  "duradoura": 4.5,  "sustentada": 4.5},
    2: {"imediata": 9.0,  "duradoura": 7.5,  "sustentada": 6.0},
    3: {"imediata": 15.0, "duradoura": 13.5, "sustentada": 12.0},
    4: {"imediata": 18.0, "duradoura": 16.5, "sustentada": 15.0},
    5: {"imediata": 21.0, "duradoura": 19.5, "sustentada": 18.0},
}

TECNICA_AUX_DANO_ADD = {
    0: {"imediata": "1d8",  "sustentada": "1d6"},
    1: {"imediata": "2d6",  "sustentada": "1d10"},
    2: {"imediata": "3d8",  "sustentada": "2d8"},
    3: {"imediata": "3d12", "sustentada": "3d8"},
    4: {"imediata": "4d10", "sustentada": "3d12"},
    5: {"imediata": "5d12", "sustentada": "4d12"},
}

TECNICA_AUX_CURA_UNICO = {1: "3d6", 2: "6d6", 3: "5d12", 4: "8d12", 5: "16d10"}
TECNICA_AUX_CURA_AREA  = {1: "2d6", 2: "4d6", 3: "4d10", 4: "6d12", 5: "12d10"}

TECNICA_AUX_CD = {
    0: {"imediata": 3,  "duradoura": 2,  "sustentada": 2},
    1: {"imediata": 5,  "duradoura": 4,  "sustentada": 4},
    2: {"imediata": 8,  "duradoura": 6,  "sustentada": 5},
    3: {"imediata": 11, "duradoura": 8,  "sustentada": 7},
    4: {"imediata": 14, "duradoura": 10, "sustentada": 8},
    5: {"imediata": 18, "duradoura": 13, "sustentada": 11},
}

# Técnica Máxima (nível 6) – referência
TECNICA_MAXIMA_REF = {
    "dano_alvo_tr":    "26d12 (média 169)",
    "dano_alvo_atq":   "28d12 (média 182)",
    "dano_area_tr":    "22d10 (média 120)",
    "cura_unico":      "24d10 (média 132)",
    "cura_area":       "20d10 (média 99)",
    "custo_pe":        25,
}

# Redução de PE máximo por habilidade passiva: 2 × nível da habilidade
TECNICA_PASSIVA_RED_PE = {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# Tipos de habilidade de técnica
TECNICA_TIPOS = {
    "ofensiva_ataque":  "Ofensiva – Jogada de Ataque",
    "ofensiva_tr":      "Ofensiva – Teste de Resistência",
    "ofensiva_area_tr": "Ofensiva em Área – TR",
    "auxiliar":         "Auxiliar",
    "passiva":          "Passiva",
    "cura_unico":       "Cura – Alvo Único",
    "cura_area":        "Cura – Área",
}

TECNICA_CONJURACAO = {
    "acao_comum":    "Ação Comum",
    "acao_bonus":    "Ação Bônus",
    "acao_completa": "Ação Completa",
    "reacao":        "Reação",
    "passiva":       "Passiva",
}

TECNICA_DURACAO = {
    "imediata":    "Imediata",
    "sustentada":  "Sustentada",
    "duradoura":   "Duradoura (cenas/dias)",
    "concentracao": "Concentração",
}

# Condições por força
CONDICOES_FRACAS  = ["Abalado", "Caído", "Desorientado", "Desprevenido"]
CONDICOES_MEDIAS  = ["Agarrado", "Amedrontado", "Condenado", "Confuso",
                     "Enfeitiçado", "Enjoado", "Enredado", "Envenenado",
                     "Imóvel", "Lento", "Surdo"]
CONDICOES_FORTES  = ["Cego", "Exposto", "Fragilizado", "Incapacitado"]
CONDICOES_EXTREMAS = ["Atordoado", "Inconsciente", "Paralisado", "Desmembramento"]
CONDICOES_POR_FORCA = {
    "fraca":  CONDICOES_FRACAS,
    "media":  CONDICOES_MEDIAS,
    "forte":  CONDICOES_FORTES,
    "extrema": CONDICOES_EXTREMAS,
}
CONDICAO_CUSTO_DADOS = {"fraca": 1, "media": 3, "forte": 5, "extrema": 8}
CONDICAO_DURACAO_PADRAO = {
    1: {"fraca": "1 rodada"},
    2: {"fraca": "2 rodadas", "media": "1 rodada"},
    3: {"fraca": "3 rodadas", "media": "2 rodadas", "forte": "1 rodada"},
    4: {"fraca": "4 rodadas", "media": "3 rodadas", "forte": "2 rodadas", "extrema": "1 rodada"},
    5: {"fraca": "5 rodadas", "media": "4 rodadas", "forte": "3 rodadas", "extrema": "1 rodada"},
}

# Liberação Máxima – custo de PE por nível da habilidade base
LIBERACAO_MAXIMA_CUSTO = {1: 3, 2: 8, 3: 12, 4: 18, 5: 30}


# ─── APTIDÕES AMALDIÇOADAS ──────────────────────────────────────────────────────

APTIDOES_DOMINIO = [
    {
        "id": "dominio_1", "nivel_req": 4, "req": [],
        "nome": "Expansão de Domínio I",
        "descricao": "Você pode criar uma Expansão Incompleta: sem barreira, expande energia em raio 4,5m × BM. Permite amplificações de técnica e efeitos ambientais. Sem acerto garantido.",
    },
    {
        "id": "dominio_2", "nivel_req": 8, "req": ["dominio_1"],
        "nome": "Expansão de Domínio II",
        "descricao": "Sua expansão pode ser Completa. Barreira esférica de 9m de raio. PV da barreira = 6 × nível aptidão. Duração: 3 + nível aptidão rodadas.",
    },
    {
        "id": "dominio_3", "nivel_req": 12, "req": ["dominio_2"],
        "nome": "Expansão de Domínio III",
        "descricao": "Domínio Completo pode ser Letal (acerto garantido imbuído na barreira), ou Sem Barreira (acerto garantido, esfera até 9m × BM, destrói expansões de fora).",
    },
    {
        "id": "dominio_4", "nivel_req": 16, "req": ["dominio_3"],
        "nome": "Expansão de Domínio IV",
        "descricao": "Abrir/fechar domínio como Ação Bônus. Custo de manutenção reduzido à metade. Área do Sem Barreira pode ser dobrada com Domínio Completo.",
    },
]

APTIDOES_ADICIONAIS = [
    {
        "id": "energia_reversa", "nivel_req": 1, "req": [],
        "nome": "Energia Reversa",
        "descricao": "Inverte o fluxo de EA para criar energia de cura. Suas habilidades de cura agora restauram PV reais (sem esta aptidão, só PV temporários).",
    },
    {
        "id": "liberacao_energia_reversa", "nivel_req": 4, "req": ["energia_reversa"],
        "nome": "Liberação de Energia Reversa",
        "descricao": "Use EA reversa ofensivamente: dano adicional contra maldições e exorcismo com energia positiva.",
    },
    {
        "id": "leitura_controle", "nivel_req": 2, "req": [],
        "nome": "Leitura e Controle",
        "descricao": "Detecte usuários de EA a até 30m. +2 em testes relacionados a energia amaldiçoada.",
    },
    {
        "id": "leitura_controle_2", "nivel_req": 6, "req": ["leitura_controle"],
        "nome": "Leitura e Controle II",
        "descricao": "Vantagem em testes de Feitiçaria/Ocultismo sobre EA. Detecte EA dentro de 60m.",
    },
    {
        "id": "leitura_controle_3", "nivel_req": 10, "req": ["leitura_controle_2"],
        "nome": "Leitura e Controle III",
        "descricao": "Maestria de controle: habilidades custam 1 PE a menos (mínimo 1).",
    },
    {
        "id": "aura", "nivel_req": 1, "req": [],
        "nome": "Aptidão de Aura",
        "descricao": "Ação Bônus: ativa aura por 1 rodada, recebendo RD 2 contra todos os danos físicos.",
    },
    {
        "id": "aura_2", "nivel_req": 5, "req": ["aura"],
        "nome": "Aptidão de Aura II",
        "descricao": "Aura aprimorada: RD 4 contra todos os tipos de dano. Sustentável por 1 PE/rodada.",
    },
    {
        "id": "reforco", "nivel_req": 2, "req": [],
        "nome": "Reforço",
        "descricao": "Ação Bônus: +BM em ataques ou +BM em CA por 1 rodada. Canaliza EA no corpo/arma.",
    },
    {
        "id": "reforco_2", "nivel_req": 6, "req": ["reforco"],
        "nome": "Reforço II",
        "descricao": "+1 permanente em ataques e CA (aumenta para +2 no nível 14).",
    },
    {
        "id": "tecnica_maxima", "nivel_req": 15, "req": ["dominio_2"],
        "nome": "Técnica Máxima",
        "descricao": "Desencadeie uma versão maximizada de habilidade nível 5 (equivale a nível 6). Custo: 25 PE. Uma vez por cena.",
    },
    {
        "id": "quebra_limite", "nivel_req": 6, "req": [],
        "nome": "Quebra de Limite",
        "descricao": "Transcende limites de gasto de EA por turno. Máximo de PE gasto por turno +BM.",
    },
    {
        "id": "cesta_oca_vime", "nivel_req": 4, "req": [],
        "nome": "Cesta Oca de Vime",
        "descricao": "Reação ao ativar Domínio: gaste 6 PE para criar cesta protetora. Nega efeitos de acerto garantido de expansões, mas não outros efeitos. +2 PE/rodada para sustentar.",
    },
    {
        "id": "emocao_petala_decadente", "nivel_req": 6, "req": ["aura", "leitura_controle_2"],
        "nome": "Emoção da Pétala Decadente",
        "descricao": "Cobre-se de EA reativa. Ao receber acerto garantido de domínio, gaste PE = 2 × nível aptidão para negar o ataque. Requer concentração.",
    },
    {
        "id": "cobrir_se", "nivel_req": 3, "req": [],
        "nome": "Cobrir-se",
        "descricao": "Como Reação, cubra-se de EA para absorver parte de um dano. Reduza o dano em BM × 2.",
    },
]

# ─── EXPANSÃO DE DOMÍNIO – TIPOS ───────────────────────────────────────────────

DOMINIO_TIPOS = {
    "incompleta": {
        "nome": "Expansão Incompleta",
        "descricao": "Sem barreira física. Expande energia em raio 4,5m × BM. Pode usar estruturas como barreira improvisada. Sem acerto garantido. Foco em amplificações e efeitos ambientais.",
        "req_aptidao": "dominio_1",
        "tem_acerto_garantido": False,
        "tem_barreira": False,
    },
    "completa_nao_letal": {
        "nome": "Expansão Completa (Não-Letal)",
        "descricao": "Barreira esférica de 9m de raio. Inimigos ficam presos até barreira ser destruída. Foca em efeitos especiais, sem acerto garantido.",
        "req_aptidao": "dominio_2",
        "tem_acerto_garantido": False,
        "tem_barreira": True,
    },
    "completa_letal": {
        "nome": "Expansão Completa (Letal)",
        "descricao": "Barreira esférica de 9m com técnica imbuída. Garante acerto em todos os ataques contra inimigos dentro da barreira.",
        "req_aptidao": "dominio_3",
        "tem_acerto_garantido": True,
        "tem_barreira": True,
    },
    "sem_barreira": {
        "nome": "Expansão Sem Barreira",
        "descricao": "Acerto garantido sem barreira física. Grande alcance (esfera até 9m × BM). Pode destruir expansões inimigas de fora. Não aprisiona inimigos.",
        "req_aptidao": "dominio_3",
        "tem_acerto_garantido": True,
        "tem_barreira": False,
    },
}

# ─── INVOCAÇÃO – AÇÕES E CARACTERÍSTICAS EXPANDIDAS ──────────────────────────

INVOCACAO_ACOES_LISTA = [
    {"id": "atacar",          "nome": "Atacar",             "tipo": "complexa",
     "desc": "Realiza jogada de ataque com dano baseado no grau e atributo configurado."},
    {"id": "acompanhar_golpe","nome": "Acompanhar Golpe",   "tipo": "complexa",
     "desc": "Aliado a 3m: próximo ataque do aliado +2 para acertar e +1d6 de dano."},
    {"id": "empurrar_cortar", "nome": "Empurrar e Cortar",  "tipo": "complexa",
     "desc": "Alvo a 1,5m: teste Atletismo vs Atletismo. Falha: alvo cai. Depois: ataque corpo-a-corpo 1d8+mod cortante."},
    {"id": "focar_precisao",  "nome": "Focar em Precisão",  "tipo": "simples",
     "desc": "Todos os ataques da invocação ganham +2 para acertar por uma rodada."},
    {"id": "levantar_guarda", "nome": "Levantar Guarda",    "tipo": "simples",
     "desc": "Invocação recebe RD 2 por uma rodada."},
    {"id": "mordida",         "nome": "Mordida",             "tipo": "complexa",
     "desc": "Corpo-a-corpo: Luta. Acerto: 2d8+mod perfurante."},
    {"id": "preparar_ataque", "nome": "Preparar Ataque",    "tipo": "simples",
     "desc": "Próximo ataque causa +1d6 de dano adicional."},
    {"id": "provocacao",      "nome": "Provocação",          "tipo": "simples",
     "desc": "Alvo 9m: TR Vontade vs Intimidação. Falha: vantagem para atacar invocação, desvantagem para atacar outros (1 rodada)."},
    {"id": "defender_aliado", "nome": "Defender Aliado",    "tipo": "complexa",
     "desc": "Aliado adjacente atacado: intervém absorvendo dano (RD = BM do controlador)."},
    {"id": "varredura",       "nome": "Varredura",           "tipo": "complexa",
     "desc": "Cone de 3m: TR de Reflexos ou dano de área do grau."},
    {"id": "pular_investir",  "nome": "Pular e Investir",   "tipo": "complexa",
     "desc": "Salta até 9m e ataca. Se mover 4,5m+: TR Fortitude ou alvo cai."},
    {"id": "curar_aliado",    "nome": "Curar Aliado",        "tipo": "complexa",
     "desc": "Cura aliado adjacente em PV igual à cura do grau."},
]

INVOCACAO_CARAC_LISTA = [
    {"id": "alado",            "nome": "Alado",              "escalas": False,
     "desc": "Deslocamento vira voo."},
    {"id": "atento",           "nome": "Atento",             "escalas": True,
     "valores": {"4": "+2", "3": "+4", "2": "+6", "1": "+8", "especial": "+10"},
     "desc": "Criaturas a 3m têm Atenção +valor."},
    {"id": "carapaca",         "nome": "Carapaça/Armadura",  "escalas": True,
     "valores": {"4": "2", "3": "4", "2": "6", "1": "8", "especial": "12"},
     "desc": "RD valor contra danos físicos."},
    {"id": "curandeira",       "nome": "Curandeira",         "escalas": False,
     "desc": "Curas aumentam +1 por dado rolado."},
    {"id": "defensor",         "nome": "Defensor",           "escalas": True,
     "valores": {"4": "+2", "3": "+4", "2": "+6", "1": "+8", "especial": "+12"},
     "desc": "Criaturas a 3m ganham CA +valor."},
    {"id": "defesa_alternativa","nome":"Defesa Alternativa", "escalas": False,
     "desc": "Troca atributo de cálculo de CA."},
    {"id": "destruidor",       "nome": "Destruidor",         "escalas": False,
     "desc": "Críticos causam 1 dado adicional de dano."},
    {"id": "furtivo",          "nome": "Furtivo",            "escalas": True,
     "valores": {"4": "+2", "3": "+4", "2": "+6", "1": "+8", "especial": "+10"},
     "desc": "+valor em Furtividade."},
    {"id": "grande",           "nome": "Grande",             "escalas": False,
     "desc": "Conta como criatura Grande."},
    {"id": "imparavel",        "nome": "Imparável",          "escalas": False,
     "desc": "Ignora terreno difícil, deslocamento não pode ser reduzido."},
    {"id": "investida",        "nome": "Investida",          "escalas": False,
     "desc": "Mover 4,5m+ antes de atacar: TR Fortitude ou alvo cai, +1 dado dano."},
    {"id": "montaria",         "nome": "Montaria",           "escalas": False,
     "desc": "Pode servir como montaria (tamanho Médio+)."},
    {"id": "movel",            "nome": "Móvel",              "escalas": True,
     "valores": {"4": "3m", "3": "4,5m", "2": "6m", "1": "7,5m", "especial": "9m"},
     "desc": "Deslocamento +valor."},
    {"id": "pequeno",          "nome": "Pequeno",            "escalas": False,
     "desc": "Conta como criatura Pequena."},
    {"id": "perito",           "nome": "Perito",             "escalas": False,
     "desc": "+2 perícias treinadas adicionais."},
    {"id": "perturbador",      "nome": "Perturbador",        "escalas": True,
     "valores": {"4": "-2", "3": "-4", "2": "-6", "1": "-8", "especial": "-10"},
     "desc": "Criaturas hostis a 3m recebem valor em testes de perícia."},
    {"id": "robustez",         "nome": "Robustez",           "escalas": True,
     "valores": {"4": "+5", "3": "+10", "2": "+15", "1": "+25", "especial": "+40"},
     "desc": "PV máximo +valor."},
    {"id": "sangue_acido",     "nome": "Sangue Ácido",       "escalas": False,
     "desc": "1×/rodada ao receber golpe: criaturas adjacentes sofrem 1d6 de dano ácido."},
    {"id": "aumento_vida",     "nome": "Aumento de Vida",    "escalas": True,
     "valores": {"4": "+5", "3": "+10", "2": "+15", "1": "+20", "especial": "+30"},
     "desc": "PV máximo +valor."},
]
