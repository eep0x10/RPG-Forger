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
        "treinamentos": "Armas Simples, Armas Marciais e Escudo Leve. Fortitude ou Reflexos. 1 perícia de Ofício/Atletismo/Acrobacia + 3 perícias quaisquer.",
        "pericias_treinamento": {
            "lista": ["Ofício", "Atletismo", "Acrobacia"],
            "qtd_lista": 1,
            "qtd_livres": 3,
            "excluir": [],
        },
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Corpo Treinado",
                "desc": "Você treinou o seu corpo para que ele seja sua própria arma. Quando realizar um ataque desarmado ou com uma arma marcial, você pode realizar um ataque desarmado como uma ação bônus. O dano dos seus ataques desarmados se torna 1d8 (1d10 no nível 5, 1d12 no nível 9, 2d8 no nível 13, 2d12 no nível 17). Você pode usar Força ou Destreza nos ataques desarmados e com armas marciais."
            },
            {
                "nivel": 1,
                "nome": "Empolgação",
                "desc": "Você começa um combate com Nível de Empolgação 1 e, ao acertar pelo menos um ataque ou manobra durante seu turno, no começo do próximo turno sobe um nível (máx. 5). Passando uma rodada sem acertar, desce um nível. O Dado de Empolgação varia: Nível 2 = 1d4, Nível 3 = 1d6, Nível 4 = 2d4, Nível 5 = 2d6. Você aprende 2 manobras de Empolgação (Ajuste, Comando, Desarme, Esquiva ou Trabalho de Pés), aprendendo mais nos níveis 6, 12 e 18. Cada manobra pode ser realizada apenas uma vez por rodada."
            }
        ],
        "habilidades_nivel": {
            2: ["Reflexo Evasivo – Você desenvolve um reflexo para evitar danos. Recebe redução de dano a todo tipo, exceto alma, igual a metade do seu nível de Lutador."],
            4: ["Implemento Marcial – Você recebe +2 na CD de suas Habilidades de Especialização, Feitiços e Aptidões Amaldiçoadas. Esse bônus aumenta em 1 nos níveis 8° e 16° de Lutador."],
            5: ["Gosto pela Luta – Você passa a adicionar +2 em jogadas de ataque desarmadas ou com armas marciais e +1 em rolagens de Fortitude e de dano. Nos níveis 8, 12, 16 e 20 o bônus em acerto aumenta em +1; nos níveis 9, 13 e 17 o bônus em Fortitude e dano aumenta em +1."],
            9: ["Teste de Resistência Mestre – Você se torna treinado em um segundo teste de resistência e mestre no concedido pela sua especialização."],
            11: ["Empolgação Máxima – Seu potencial assume um patamar superior. Os seus dados de empolgação se tornam 2d4, 2d6, 2d8 e 3d6, respectivamente."],
            20: ["Lutador Superior – Seus ataques desarmados causam 1 dado de dano adicional e uma vez por rodada você pode realizar um ataque desarmado como ação livre gastando 2PE. Você inicia todo combate com um Nível de Empolgação a mais."]
        },
        "habilidades_catalogo": [
            # ── Nível 2 ──
            {"nivel": 2, "nome": "Aparar Ataque",            "desc": "Quando for alvo de um ataque corpo a corpo, você pode gastar 1 PE e sua reação para realizar uma jogada de ataque contra o atacante. Caso seu teste supere o do inimigo, você evita o ataque."},
            {"nivel": 2, "nome": "Aparar Projéteis",         "desc": "Quando receber um ataque à distância, você pode gastar 1 PE e sua reação para tentar aparar o projétil, reduzindo o dano recebido em 2d6 + modificador de atributo-chave + bônus de treinamento."},
            {"nivel": 2, "nome": "Ataque Inconsequente",     "desc": "Uma vez por rodada, ao realizar um ataque, você pode escolher receber vantagem na jogada de ataque e +5 na rolagem de dano dele. Porém, ao realizar um ataque inconsequente, você fica Desprevenido por 1 rodada."},
            {"nivel": 2, "nome": "Caminho da Mão Vazia",     "desc": "Todo ataque desarmado que você realizar causa dano adicional igual ao seu bônus de treinamento e você soma metade do seu bônus de treinamento em jogadas de ataque desarmados."},
            {"nivel": 2, "nome": "Complementação Marcial",   "desc": "Enquanto estiver desarmado ou empunhando uma arma marcial, você recebe um bônus de +2 em testes para Desarmar, Derrubar ou Empurrar, assim como para resistir a esses efeitos."},
            {"nivel": 2, "nome": "Deboche Desconcertante",   "desc": "Como uma Ação Bônus, escolha uma criatura que possa te ver ou ouvir: realize um teste de Intimidação contra Vontade dela com +2. Caso suceda, a criatura recebe uma penalidade igual ao seu bônus de treinamento em todos os testes que realizar até o começo do seu próximo turno.", "req": "Treinado em Intimidação"},
            {"nivel": 2, "nome": "Dedicação em Arma",        "desc": "Escolha três armas para serem suas Armas Dedicadas (sem Duas Mãos ou Pesada, exceto Marciais). Suas armas escolhidas passam a ser contadas como marciais e, enquanto empunhar uma Arma Dedicada, o dano dela aumenta em 1 nível."},
            {"nivel": 2, "nome": "Esquiva Rápida",           "desc": "Como uma Ação Bônus, realize um teste de Acrobacia contra a Atenção de um inimigo dentro do seu alcance corpo a corpo. Caso suceda, o alvo recebe metade do seu mod. de Destreza como penalidade em jogadas de ataque feitas contra você até o começo do seu próximo turno."},
            {"nivel": 2, "nome": "Finta Melhorada",          "desc": "Você pode utilizar Destreza ao invés de Presença em testes de Enganação para fintar. Além disso, acertar um inimigo desprevenido pela sua finta causa um dado de dano adicional."},
            {"nivel": 2, "nome": "Impacto Misto",            "desc": "Quando acertar uma criatura com um ataque com arma marcial, você recebe +2 em jogadas de ataque e dano desarmados até o começo do seu próximo turno. Nos níveis 5, 10, 15 e 20 o bônus em dano aumenta em +1; nos níveis 6, 12 e 18 o bônus em jogadas de ataque aumenta em +1."},
            {"nivel": 2, "nome": "Kiai Intimidador",         "desc": "Uma vez por rodada, quando conseguir um crítico em um ataque corpo a corpo você pode, como uma ação livre, realizar um teste de Intimidação contra Vontade do alvo e, caso suceda, ela fica Abalada por uma rodada. Se a criatura já estiver Abalada, ela fica Amedrontada."},
            {"nivel": 2, "nome": "Mãos Amaldiçoadas",        "desc": "Quando utilizar um Feitiço ofensivo com alcance de Toque, você pode substituir a jogada de ataque de técnica por uma jogada de ataque corpo a corpo e, também, somar seu modificador de Força ou Destreza no total."},
            {"nivel": 2, "nome": "Puxar um Ar",              "desc": "Como uma Ação Bônus, realize uma rolagem do seu dano desarmado e se cure nesse valor. Pode ser usada uma quantidade de vezes igual ao seu bônus de treinamento por descanso curto ou longo."},
            {"nivel": 2, "nome": "Quebrando Tudo",           "desc": "Como parte de um ataque, você pode agarrar um objeto pequeno ou menor adjacente. Objetos usados como arma improvisada recebem +1d no dano e são considerados armas marciais."},
            {"nivel": 2, "nome": "Resistir",                 "desc": "Quando realizar um teste de resistência de Fortitude ou Reflexos, você pode gastar até 2 PE para receber um bônus de +2 para cada PE gasto."},
            # ── Nível 4 ──
            {"nivel": 4, "nome": "Ação Ágil",               "desc": "Uma vez por rodada, você pode gastar 2 PE para receber uma Ação Ágil, a qual pode ser utilizada para Andar, Desengajar ou Esconder."},
            {"nivel": 4, "nome": "Acrobata",                 "desc": "Você passa a utilizar Destreza como atributo para calcular sua distância de pulo, assim como pode utilizar Acrobacia no lugar de Atletismo em testes para aumentar a sua distância de salto."},
            {"nivel": 4, "nome": "Atacar e Recuar",          "desc": "Uma vez por turno, quando acertar uma criatura com um ataque, você pode gastar 1 PE para se mover até 4,5 metros para longe da criatura acertada. Este movimento não causa ataques de oportunidade.", "req": "Esquiva Rápida"},
            {"nivel": 4, "nome": "Brutalidade",              "desc": "Como uma Ação Livre, você pode gastar 2 PE para adentrar no estado de Brutalidade: você recebe +2 em jogadas de ataque corpo a corpo e dano. Não pode manter concentração nem usar Feitiços ou Técnicas de Estilo. Nos níveis 8, 12, 16 e 20 gaste 2 PE a mais para aumentar o bônus em +1."},
            {"nivel": 4, "nome": "Defesa Marcial",           "desc": "Enquanto estiver desarmado ou empunhando uma arma marcial, você soma 1 + metade do seu Bônus de Treinamento à sua Defesa.", "req": "Complementação Marcial"},
            {"nivel": 4, "nome": "Devolver Projéteis",       "desc": "O dado de Aparar Projéteis se torna 3d10 e soma também o seu Nível de Lutador. Caso use Aparar Projéteis e o dano se torne nulo ou negativo, você pode devolver o projétil como parte da reação, causando no atacante o dano que você receberia.", "req": "Aparar Projéteis"},
            {"nivel": 4, "nome": "Fluxo",                    "desc": "A cada nível de empolgação que você subir, você recebe +1 em rolagens de dano e, no começo de toda rodada, recebe 4 PV temporários para cada nível de empolgação acima do primeiro."},
            {"nivel": 4, "nome": "Fúria da Vingança",        "desc": "Ao ver um aliado chegar a 0 PV e cair, durante uma rodada você recebe: ataques causam 4 de dano adicional; Defesa aumenta em 2; +2 em TRs de Fortitude e Vontade. Os benefícios se aplicam apenas contra o inimigo alvo da vingança."},
            {"nivel": 4, "nome": "Imprudência Motivadora",   "desc": "Ao iniciar uma cena de combate, escolha lutar com uma restrição auto imposta (senso ou membro). Se vencer o combate com a restrição, você recupera PE = nível de personagem; recebe +2 em rolagens de ataque e tem sua margem de crítico reduzida em 1 até o fim da missão."},
            {"nivel": 4, "nome": "Músculos Desenvolvidos",   "desc": "Você pode optar por somar seu Modificador de Força ao invés de Destreza em sua Defesa, modificando o cálculo padrão."},
            {"nivel": 4, "nome": "Redirecionar Força",       "desc": "Quando um inimigo errar um ataque corpo a corpo contra você, você pode gastar 2 PE e sua reação para redirecionar o ataque: escolha outra criatura dentro do alcance do golpe e, caso o resultado supere a Defesa do novo alvo, ele recebe o ataque."},
            {"nivel": 4, "nome": "Segura pra Mim",           "desc": "Quando for alvo de um ataque corpo a corpo ou habilidade com alvo único, você pode gastar 3 PE para colocar uma criatura que esteja agarrando na frente (teste de Atletismo vs. Atletismo/Acrobacia dela). Se bem sucedido, a criatura recebe os efeitos no seu lugar."},
            {"nivel": 4, "nome": "Sobrevivente",             "desc": "Enquanto estiver com menos da metade dos seus PV máximos, sempre que começar seu turno você recupera 1d6 + mod. de Constituição em PV. Não funciona se Inconsciente. Nos níveis 8, 12, 16 e 20 a cura aumenta em 1d6.", "req": "Constituição 16"},
            {"nivel": 4, "nome": "Voadora",                  "desc": "Quando realizar uma Investida estando desarmado, você pode gastar 3 PE para realizar uma Voadora. Você causa 1d8 de dano adicional para cada 3 metros deslocados até o alvo, limitado pelo seu mod. de Força ou Destreza."},
            # ── Nível 6 ──
            {"nivel": 6, "nome": "Aprimoramento Marcial",   "desc": "Você passa a somar metade do seu Bônus de Treinamento em sua CD de Especialização."},
            {"nivel": 6, "nome": "Ataque Extra",             "desc": "Ao realizar a ação Atacar, você pode gastar 2 PE para atacar duas vezes ao invés de uma."},
            {"nivel": 6, "nome": "Brutalidade Sanguinária",  "desc": "Enquanto no estado de Brutalidade, sempre que tiver um acerto crítico ou reduzir a vida de uma criatura a 0 ou menos, você aumenta o nível de dano dos seus ataques corpo a corpo em 1, acumulando até um limite igual ao seu bônus de treinamento.", "req": "Brutalidade"},
            {"nivel": 6, "nome": "Corpo Calejado",           "desc": "Você passa a adicionar metade do seu Modificador de Constituição na sua Defesa e recebe PV adicionais igual ao seu nível de Lutador."},
            {"nivel": 6, "nome": "Eliminar e Continuar",     "desc": "Sempre que um inimigo ao qual você causou dano cair ou morrer dentro de 9 metros, você recebe 2d6 + nível de personagem + mod. de atributo-chave em PV temporários, que acumulam. No nível 8 aumenta para 3d6, nível 12 para 4d6, nível 16 para 4d8, nível 20 para 4d12."},
            {"nivel": 6, "nome": "Foguete Sem Ré",           "desc": "Como uma ação completa, gaste 6 PE para se mover até o dobro do seu deslocamento. Toda criatura que você passar realiza um TR de Reflexos, sofrendo Xd10 + mod. de Força ou Destreza de dano de Impacto (X = BT). Ao terminar adjacente a uma criatura, você pode realizar um ataque contra ela."},
            {"nivel": 6, "nome": "Golpe da Mão Aberta",      "desc": "Como uma ação comum, você pode gastar 4 PE para realizar um golpe de mão aberta. Em um acerto, o alvo realiza um TR de Fortitude e, em um fracasso, fica Desorientado, Enjoado e Exposto até o início do seu próximo turno."},
            {"nivel": 6, "nome": "Ignorar Dor",              "desc": "Você recebe redução de danos contra todos os tipos, menos alma, igual ao seu nível de empolgação atual. Contra danos físicos, a redução de dano é dobrada."},
            {"nivel": 6, "nome": "Manobras Finalizadoras",   "desc": "Você libera acesso a novas manobras (Ataque Circular, Golpe Certeiro, Quebra Crânio). Para realizar uma manobra finalizadora, é necessário estar com nível de empolgação 5. Após utilizar uma, você retorna ao nível de empolgação 1."},
            {"nivel": 6, "nome": "Poder Corporal",           "desc": "O dano de seus ataques desarmados aumenta em 2 níveis e, uma vez por rodada, ao realizar um ataque desarmado, você pode escolher realizar uma Manobra como parte do ataque.", "req": "Caminho da Mão Vazia"},
            {"nivel": 6, "nome": "Potência Superior",        "desc": "Quando Derrubar um inimigo com sucesso, ele também recebe 2d6 + mod. de Força de dano de impacto; quando Empurrar, a distância padrão se torna 4,5 metros ao invés de 1,5 metros.", "req": "Complementação Marcial"},
            {"nivel": 6, "nome": "Sequência Inconsequente",  "desc": "Quando utilizar Ataque Inconsequente, você passa a receber o dano adicional em todos seus ataques realizados durante o turno.", "req": "Ataque Inconsequente"},
            {"nivel": 6, "nome": "Um com a Arma",            "desc": "Metade do seu nível de Lutador vezes por descanso curto, suas armas dedicadas conseguem superar resistência ao tipo de dano delas. Uma vez por rodada, ao ser desarmado de uma arma dedicada, você pode usar sua reação para evitar, mantendo-se em posse dela.", "req": "Dedicação em Arma"},
            # ── Nível 8 ──
            {"nivel": 8, "nome": "Aptidões de Luta",         "desc": "Ao obter esta habilidade, você pode aumentar o seu nível de aptidão em Aura ou Controle e Leitura em 1. Você pode pegar esta habilidade duas vezes, uma para cada aptidão."},
            {"nivel": 8, "nome": "Ataques Ressoantes",       "desc": "Ao realizar um ataque contra um inimigo, você pode gastar 2 PE para que todos os inimigos adjacentes ao alvo com Defesa inferior ao resultado do seu ataque recebam dano igual a metade do dano causado no alvo."},
            {"nivel": 8, "nome": "Brutalidade Aprimorada",   "desc": "Ao entrar em Brutalidade, você recebe PV temporários = nível + mod. de atributo-chave. O bônus inicial em dano se torna +4 e o aumento no dano por PE adicional se torna +2.", "req": "Brutalidade"},
            {"nivel": 8, "nome": "Feitiço e Punho",          "desc": "Uma vez por rodada, quando utilizar um Feitiço de dano com alvo único, você pode gastar 2 PE para realizar um ataque corpo a corpo contra o mesmo alvo, desde que ele esteja dentro do seu alcance.", "req": "Mãos Amaldiçoadas"},
            {"nivel": 8, "nome": "Golpear Brecha",           "desc": "Quando utilizar Aparar Ataque e conseguir aparar com sucesso, você pode gastar 2 PE adicionais para realizar um ataque contra o inimigo como parte da reação.", "req": "Aparar Ataque"},
            {"nivel": 8, "nome": "Oportunista",              "desc": "Quando conseguir um acerto crítico em um ataque corpo a corpo, você pode fazer com que o alvo receba desvantagem contra um TR à sua escolha, até o início do seu próximo turno."},
            {"nivel": 8, "nome": "Punhos Letais",            "desc": "Enquanto estiver desarmado, sua margem de crítico diminui em 1 e seus ataques ignoram RD igual ao seu bônus de treinamento.", "req": "Poder Corporal"},
            # ── Nível 10 ──
            {"nivel": 10, "nome": "Alma Quieta",             "desc": "Você recebe vantagem para resistir às seguintes condições: Condenado, Enfeitiçado e Fragilizado.", "req": "Treinado em Vontade"},
            {"nivel": 10, "nome": "Corpo Sincronizado",      "desc": "Você recebe vantagem para resistir às seguintes condições: Caído e Exposto.", "req": "Treinado em Fortitude"},
            {"nivel": 10, "nome": "Empolgar-se",             "desc": "Uma quantidade de vezes igual ao seu Bônus de Treinamento, por descanso longo, você pode escolher subir dois níveis de empolgação, ao invés de um, no começo de um turno em que ele aumentaria."},
            {"nivel": 10, "nome": "Impacto Demolidor",       "desc": "Como uma Ação Comum, realize um ataque corpo a corpo e, caso acerte, você causa o dano do ataque e realiza a ação Empurrar como parte dele: a distância é dobrada e o alvo quebra objetos e obstáculos em seu caminho, recebendo o Dano de Fontes Externas.", "req": "Potência Superior"},
            {"nivel": 10, "nome": "Insistência",             "desc": "Uma vez por cena, caso você fosse ter os seus PV reduzidos a 0, você pode escolher retornar ao nível de empolgação 1 para continuar de pé, curando-se em um valor igual a uma rolagem de dano do seu ataque desarmado.", "req": "Ignorar Dor"},
            {"nivel": 10, "nome": "Mente em Paz",            "desc": "Você recebe vantagem para resistir às seguintes condições: Amedrontado, Atordoado e Confuso.", "req": "Treinado em Astúcia"},
            # ── Nível 12 ──
            {"nivel": 12, "nome": "Armas Absolutas",         "desc": "Enquanto estiver empunhando uma Arma Dedicada, você pode gastar 2 PE para receber: escolha aumentar sua Defesa em 3 ou receber +3 em Jogadas de Ataque e, uma vez por ataque, ao errar, você pode rolar novamente o ataque ficando com o melhor resultado.", "req": "Um com a Arma"},
            {"nivel": 12, "nome": "Corpo Arsenal",           "desc": "Quando realizar um acerto crítico com um ataque desarmado, você pode optar por infligir o efeito de um grupo adicional entre Bastão, Haste ou Martelo.", "req": "Punhos Letais"},
            # ── Nível 16 ──
            {"nivel": 16, "nome": "Corpo Supremo",           "desc": "Você recebe +3 metros de movimento, +4 na Defesa e redução de dano = metade do nível de personagem contra dano cortante, perfurante e de impacto, mais um tipo à sua escolha (exceto alma). Contra os outros tipos, a redução é 1/4 do seu nível."},
            {"nivel": 16, "nome": "Duro na Queda",           "desc": "Quando estiver nas portas da morte, você pode receber uma falha garantida para fazer um TR de Vontade com CD X (X = 15 + 1 para cada 3 PV negativos). Se passar, você levanta com 1 de vida e recebe 1 ponto de exaustão.", "req": "Treinado em Vontade"},
            {"nivel": 16, "nome": "Seja Água",               "desc": "Seu Deslocamento aumenta em 3 metros, você ignora terreno difícil por fontes físicas e, uma vez por rodada, pode evitar ser agarrado sem a necessidade de teste."},
            {"nivel": 16, "nome": "Tempestade Sufocante",    "desc": "Para cada ataque corpo a corpo desarmado ou com arma marcial que você acertar em um mesmo alvo, ele recebe -1 na Defesa e em TRs contra você, acumulando até um máximo igual ao seu bônus de treinamento. O prejuízo dura até o começo do próximo turno da criatura."},
        ],
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
        "treinamentos": "Todas as armas e escudos. Fortitude ou Reflexos. 2 perícias de Ofício/Atletismo/Acrobacia + 3 outras quaisquer.",
        "pericias_treinamento": {
            "lista": ["Ofício", "Atletismo", "Acrobacia"],
            "qtd_lista": 2,
            "qtd_livres": 3,
            "excluir": [],
        },
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Repertório do Especialista",
                "desc": "Você escolhe um estilo de combate principal no 1° nível: Defensivo (+2 Defesa, escala nos níveis 4/8/12/16), Arremessador (+2 dano com arremesso, escala), Duelista (+1 acerto/+2 dano com uma arma, escala), Interceptador (reação para reduzir dano de aliado em 1d10+mod, escala), Protetor (reação para impor desvantagem em ataque a aliado), Distante (+1 acerto/+2 dano a distância, escala), Duplo (+mod de atributo no dano da segunda arma +1 escalonável) ou Massivo (rola novamente 1s e 2s em dano com armas pesadas/duas mãos, +1 dano escalonável). Recebe novo estilo nos níveis 6 e 12."
            },
            {
                "nivel": 1,
                "nome": "Artes do Combate",
                "desc": "Você recebe Pontos de Preparo = nível de Especialista em Combate + Modificador de Sabedoria, usados para artes especiais. Artes conhecidas: Arremesso Ágil (1PP: ataque extra com arma de arremesso), Distração Letal (1PP: acerto reduz Defesa do alvo em ½ mod. Sab.), Execução Silenciosa (1PP: +1d6 dano extra em alvo desprevenido, escala), Golpe Descendente (1PP: aumenta sua Defesa em ½ mod. Sab. até próximo turno) e Investida Imediata (2PP: mova-se mod. Sab. ×1,5m e ataque sem provocar ataque de oportunidade). Recupera 1PP ao eliminar inimigo, 2PP ao analisar (ação comum), metade em descanso curto, tudo em descanso longo."
            }
        ],
        "habilidades_nivel": {
            4: ["Golpe Especial – Ao atacar, você pode montar um ataque especial: Amplo (atinge +1 criatura, +2PE), Atroz (+1 dado de dano, +1PE), Impactante (empurra 1,5m por 15 pts de dano, +1PE), Letal (−1 na margem de crítico, +2PE), Longo (+1,5m corpo/+9m distância, +1PE), Penetrante (ignora RD = ½ nível, +2PE) ou Preciso (vantagem no ataque, +1PE/+2PE após primeiro uso). Custo a mais em PE pago além do custo original da ação.",
                 "Implemento Marcial – Você recebe +2 na CD de suas Habilidades de Especialização, Feitiços e Aptidões Amaldiçoadas. Esse bônus aumenta em 1 nos níveis 8° e 16°."],
            6: ["Renovação pelo Sangue – Sempre que conseguir um acerto crítico ou reduzir um inimigo a 0 Pontos de Vida, você recupera 1 Ponto de Energia Amaldiçoada."],
            9: ["Teste de Resistência Mestre – Você se torna treinado em um segundo teste de resistência e mestre no concedido pela sua especialização."],
            20: ["Autossuficiente – Toda vez que utilizar um Golpe Especial, você recebe 3 PE temporários. Além disso, todos seus ataques causam +1 dado de dano."]
        },
        "habilidades_catalogo": [
            # ── Nível 2 ──
            {"nivel": 2, "nome": "Arremessos Potentes",       "desc": "Seus ataques com armas de arremesso contam como um nível de dano acima. No começo do seu turno, você pode gastar 1 PE para fazer com que seus ataques com armas de arremesso ignorem RD igual ao seu bônus de treinamento."},
            {"nivel": 2, "nome": "Arsenal Cíclico",           "desc": "Uma vez por rodada, você pode sacar ou trocar um item como ação livre. Ao realizar um golpe com um grupo de armas e trocar para outra arma de outro grupo na mesma rodada ou na próxima, você recebe +1d até o fim do seu próximo turno com a arma trocada."},
            {"nivel": 2, "nome": "Assumir Postura",           "desc": "Você recebe acesso às posturas de combate (Sol, Lua, Terra, Dragão, Fortuna, Devastação, Tempestade, Céu). Entrar em uma postura é uma ação bônus e ela dura 1 minuto ou até ser derrubado, incapacitado ou trocar de postura. Pode usar BT vezes."},
            {"nivel": 2, "nome": "Disparos Sincronizados",    "desc": "Caso esteja manejando duas armas a distância ou de fogo, você pode usar suas ações de ataque juntas para sincronizar os dois tiros. Caso ambos acertem, você combina o dano em uma única instância, adicionando efeitos de ambas as armas e aplicando resistências apenas uma vez."},
            {"nivel": 2, "nome": "Escudeiro Agressivo",       "desc": "Uma vez por rodada, ao realizar uma ação de ataque empunhando um escudo, você pode gastar 1 PE para fazer um ataque adicional com o escudo."},
            {"nivel": 2, "nome": "Extensão do Corpo",         "desc": "Seu alcance em ataques corpo a corpo aumenta em 1,5 metros e você recebe +2 em jogadas de ataque e em testes para evitar ser desarmado."},
            {"nivel": 2, "nome": "Flanqueador Superior",      "desc": "Enquanto estiver flanqueando uma criatura, ela recebe -2 em testes de resistência."},
            {"nivel": 2, "nome": "Golpe Falso",               "desc": "Como reação a um aliado atacando um inimigo dentro do seu alcance, você realiza o golpe falso. O inimigo deve realizar um TR de Astúcia e, caso falhe, o seu aliado recebe vantagem no teste de ataque."},
            {"nivel": 2, "nome": "Golpes Potentes",           "desc": "Sempre que estiver usando uma arma com a qual seja treinado, o dano dela aumenta em um nível e suas rolagens de dano recebem um bônus de +2."},
            {"nivel": 2, "nome": "Indomável",                 "desc": "Uma quantidade de vezes por descanso curto ou longo igual a metade do seu nível de personagem, você pode gastar 1 PE para rolar novamente um TR em que você falhar, ficando com o melhor resultado."},
            {"nivel": 2, "nome": "Pistoleiro Iniciado",       "desc": "Quando for realizar um ataque com uma arma de fogo, você pode escolher aumentar a margem de Emperrar em 2 e, em troca, você causa 1 dado de dano adicional caso acerte."},
            {"nivel": 2, "nome": "Posicionamento Ameaçador",  "desc": "A menos que esteja furtivo, você pode conceder os benefícios de Flanco para aliados mesmo utilizando armas a distância ou de fogo, desde que o alvo do flanco esteja dentro do primeiro alcance da sua arma."},
            {"nivel": 2, "nome": "Precisão Definitiva",       "desc": "Quando faz um ataque, você pode gastar 1 PE para receber +2 na rolagem para acertar. A cada quatro níveis, gaste 1 PE a mais para aumentar o bônus em +2. Pode optar por adicionar esse bônus na rolagem de dano ao invés da de acerto, com bônus de +4."},
            {"nivel": 2, "nome": "Presença Suprimida",        "desc": "Você recebe um bônus de +2 em rolagens de Furtividade. Sua penalidade em furtividade por atacar e fazer outras ações chamativas é reduzida para -5."},
            {"nivel": 2, "nome": "Revigorar",                 "desc": "Uma quantidade de vezes igual ao seu bônus de treinamento, você pode usar sua ação bônus para se curar em 1d10 + 2× mod. de Constituição + BT, aumentando em um dado a cada 4 níveis."},
            {"nivel": 2, "nome": "Tiro Falso",                "desc": "Como reação a um aliado atacando um inimigo dentro do seu alcance, estando com arma a distância ou de fogo, você realiza um tiro falso. O inimigo deve realizar um TR de Astúcia e, caso falhe, o seu aliado recebe vantagem no teste de ataque."},
            {"nivel": 2, "nome": "Zona de Risco",             "desc": "Uma vez por rodada, se estiver empunhando uma arma corpo a corpo com a propriedade Estendida e um inimigo entrar no seu alcance de ataque, você pode gastar 2 PE para realizar um ataque contra ele."},
            # ── Nível 4 ──
            {"nivel": 4, "nome": "Aprender Postura",          "desc": "Você aprende uma postura adicional à sua escolha. No 10° nível você aprende outra postura.", "req": "Assumir Postura"},
            {"nivel": 4, "nome": "Armas Escolhidas",          "desc": "Escolha um grupo de arma: seus ataques com armas dele têm o nível de dano aumentado em 3."},
            {"nivel": 4, "nome": "Arremesso Rápido",          "desc": "Uma vez por rodada, ao realizar um ataque com uma arma de arremesso, você pode gastar 1 PE para realizar um ataque com arma de arremesso contra outro alvo."},
            {"nivel": 4, "nome": "Buscar Oportunidade",       "desc": "Como uma Ação Livre, realize um teste de Percepção com CD16 + 2 para cada inimigo em campo. Caso suceda, você pode utilizar Andar, Desengajar ou Esconder como Ação Livre."},
            {"nivel": 4, "nome": "Compensar Erro",            "desc": "Uma vez por rodada, quando errar um ataque com uma arma corpo a corpo, você pode gastar até PE = BT para causar dano no alvo. Para cada ponto gasto, o alvo recebe 1d10 de dano Energético + mod. de atributo-chave."},
            {"nivel": 4, "nome": "Especialista em Escudo",    "desc": "Você passa a somar o aumento base em RD do seu escudo em testes de resistência de Reflexos e Fortitude."},
            {"nivel": 4, "nome": "Espírito de Luta",          "desc": "Como uma Ação Livre, você pode gastar 1 PE para receber +2 em jogadas de ataque até o fim da cena. Ao utilizar esta habilidade, você ganha PV temporários igual ao seu nível de personagem."},
            {"nivel": 4, "nome": "Grupo Favorito",            "desc": "Escolha um grupo de armas: você recebe acesso ao efeito de crítico do grupo enquanto manejando uma arma que pertença a ele."},
            {"nivel": 4, "nome": "Guarda Estudada",           "desc": "Você passa a somar metade do seu mod. de Sabedoria na sua Defesa, limitado pelo seu nível. Além disso, você pode escolher um TR para receber um bônus de +2."},
            {"nivel": 4, "nome": "Mente Oculta",              "desc": "Você passa a adicionar também o seu bônus de sabedoria em rolagens de Furtividade."},
            {"nivel": 4, "nome": "Preparo Imediato",          "desc": "Durante uma rolagem de iniciativa, você pode gastar 3 pontos de preparo para utilizar Preparar, mas apenas para uma ação bônus. A partir do 10° nível, gaste 7 pontos de preparo para preparar uma ação comum."},
            {"nivel": 4, "nome": "Recarga Rápida",            "desc": "O custo em ações para recarregar armas a distância diminui em um nível: ação comum se torna ação bônus e ação bônus se torna ação livre."},
            {"nivel": 4, "nome": "Técnicas de Avanço",        "desc": "Você aprende duas artes de combate de avanço: Avanço Bumerangue (salte 6m em direção a um inimigo e retorne ao ponto de partida, podendo atacar no retorno) e Sombra Descendente (avance 6m, ataque o alvo, use-o como apoio para cair em outro inimigo a 6m)."},
            {"nivel": 4, "nome": "Uso Rápido",                "desc": "Ao utilizar uma ação para usar um item, você pode pagar 1 PE para usar um item adicional."},
            # ── Nível 6 ──
            {"nivel": 6, "nome": "Acervo Amplo",              "desc": "Você aprende mais um Estilo de Combate. Após meditar por 1 hora, você pode trocar quais estilos de combate você possui."},
            {"nivel": 6, "nome": "Aprimoramento Especializado","desc": "Você passa a somar metade do modificador do seu atributo chave em sua CD de Especialização."},
            {"nivel": 6, "nome": "Ataque Extra",              "desc": "Ao realizar a ação Atacar, você pode gastar 2 PE para atacar duas vezes ao invés de uma."},
            {"nivel": 6, "nome": "Crítico Melhorado",         "desc": "A margem do seu acerto crítico reduz em um número."},
            {"nivel": 6, "nome": "Crítico Potente",           "desc": "Ao acertar um ataque crítico, ele causa 1 dado de dano adicional."},
            {"nivel": 6, "nome": "Feitiçaria Implementada",   "desc": "Uma vez por rodada, quando utilizar um Feitiço de dano, você pode gastar 2 PE para realizar um ataque contra uma criatura afetada por ela, como Ação Livre.", "req": "Treinado em Feitiçaria"},
            {"nivel": 6, "nome": "Fluxo Perfeito",            "desc": "Caso você acerte todos os seus ataques no turno, no seu próximo turno você ganha 1 PE temporário. No 12° nível, esse valor se torna 2."},
            {"nivel": 6, "nome": "Manejo Especial",           "desc": "Você pode escolher uma propriedade de ferramenta amaldiçoada para ser aplicada em toda arma que você estiver manejando, se possível."},
            {"nivel": 6, "nome": "Marcar Inimigo",            "desc": "Quando acertar uma criatura com um ataque corpo a corpo, você pode marcá-la até o final do seu próximo turno: ela recebe -4 em jogadas de ataque e, caso cause dano em alguém além de você, você pode gastar 1 PE para realizar um ataque como Ação Bônus contra ela."},
            {"nivel": 6, "nome": "Mira Destrutiva",           "desc": "Quando utilizar a ação Mirar, você pode mirar em uma parte específica do corpo (Olho, Braço, Perna ou Ferida Interna) com -15 na jogada de ataque. Caso acerte, o alvo recebe a consequência do membro durante uma rodada.", "req": "Treinado em Percepção"},
            {"nivel": 6, "nome": "Olhos de Águia",            "desc": "Você pode gastar 1 PE para usar Mirar como uma ação livre."},
            {"nivel": 6, "nome": "Preparação Rápida",         "desc": "Entrar em uma postura se torna uma Ação Livre e elas não são canceladas caso você seja empurrado.", "req": "Assumir Postura"},
            # ── Nível 8 ──
            {"nivel": 8, "nome": "Aptidões de Combate",       "desc": "Ao obter esta habilidade, você pode aumentar o seu nível de aptidão em Aura ou Controle e Leitura em 1. Você pode pegar esta habilidade duas vezes, uma para cada aptidão."},
            {"nivel": 8, "nome": "Destruição Dupla",          "desc": "Enquanto estiver lutando com duas armas de grupos diferentes, seu ataque com a segunda arma causa 1 dado de dano adicional e, em um acerto crítico, você pode gastar 1 PE para aplicar o Efeito Crítico do grupo das duas armas."},
            {"nivel": 8, "nome": "Espírito Incansável",       "desc": "Quando utilizar Espírito de Luta, você pode optar por gastar 2 PE ao invés de 1, aumentando o bônus em ataques para +5 e fazendo com que os PV temporários ganhos se tornem o seu bônus de ataque.", "req": "Espírito de Luta"},
            {"nivel": 8, "nome": "Pistoleiro Avançado",       "desc": "Você pode aumentar o Emperrar em até 6, causando 1 dado de dano adicional para cada 2 a mais. Além disso, caso uma criatura tente se mover dentro do primeiro alcance da sua arma de fogo, você pode usar sua Reação para realizar um ataque contra ela.", "req": "Pistoleiro Iniciado"},
            {"nivel": 8, "nome": "Ricochete Constante",       "desc": "Quando for ativar Arremessos Potentes, você pode pagar 5 PE ao invés de 1 para que, até o final do turno, seus ataques com armas de arremesso possam acertar uma criatura à sua escolha dentro de 4,5 metros do alvo."},
            {"nivel": 8, "nome": "Sombra Viva",               "desc": "Uma vez por rodada, você pode utilizar Esgueirar e se mover todo o seu movimento, ao invés de apenas metade. Uma vez por rodada, caso fosse ser encontrado, você pode usar sua Reação para realizar outro teste de Furtividade.", "req": "Treinado em Furtividade"},
            {"nivel": 8, "nome": "Surto de Ação",             "desc": "Metade do BT vezes por descanso longo, você pode, uma vez por rodada, gastar 5 PE para realizar uma ação comum a mais no seu turno."},
            {"nivel": 8, "nome": "Técnicas da Força",         "desc": "Você aprende duas artes de combate da força: Nuvens Espirais (até três ataques com 2PP cada, empurrando o alvo 3m a cada acerto) e Onda do Dragão (5PP: vantagem no ataque, empurra o alvo 6m e causa 3d12 de dano Energético adicional)."},
            # ── Nível 10 ──
            {"nivel": 10, "nome": "Análise Acelerada",        "desc": "Utilizar a ação de Análise se torna uma ação bônus."},
            {"nivel": 10, "nome": "Armas Perfeitas",          "desc": "Seus ataques com uma arma do grupo escolhido em Armas Escolhidas ignoram 10 de RD ao tipo de dano dela.", "req": "Armas Escolhidas"},
            {"nivel": 10, "nome": "Assassinar",               "desc": "Durante a primeira rodada de um combate, ao atacar uma criatura desprevenida a partir da furtividade ou surpresa, seu primeiro ataque é um crítico garantido.", "req": "Mestre em Furtividade"},
            {"nivel": 10, "nome": "Ataque Concentrado",       "desc": "Ao utilizar a ação Atacar, você pode gastar PE = metade do custo de Ataque Extra e/ou Surto de Ação para adicionar metade dos dados de dano de um ataque à rolagem de dano do próximo ataque.", "req": "Ataque Extra"},
            {"nivel": 10, "nome": "Chuva de Arremessos",      "desc": "Como uma ação completa, você pode realizar uma quantidade de ataques com armas de arremesso igual ao seu BT. Para cada ataque após o primeiro, você gasta 1 PE.", "req": "Arremessos Potentes"},
            {"nivel": 10, "nome": "Potência Antes de Cair",   "desc": "Se você for cair para 0 de vida, você pode realizar um turno impedindo o turno atual. Ao ter 0 de vida neste turno, tomar dano resulta em falhas no teste de morte. Quando o turno acaba, você fica inconsciente e recebe 1 ponto de exaustão. Pode ser usada uma vez por descanso longo."},
            # ── Nível 12 ──
            {"nivel": 12, "nome": "Ciclagem Absoluta",        "desc": "Você pode, durante o seu turno, trocar a arma que esteja manejando toda vez que atacar. Além disso, sempre que trocar para outra arma de outro grupo, você recebe +2 na próxima jogada de ataque.", "req": "Arsenal Cíclico"},
            {"nivel": 12, "nome": "Manejo Único",             "desc": "Você escolhe mais uma propriedade para ser aplicada em toda arma que estiver manejando e, no começo de uma cena de combate, pode pagar 2 PE para receber uma propriedade única durante o resto da cena.", "req": "Manejo Especial"},
            {"nivel": 12, "nome": "Mestre Pistoleiro",        "desc": "Fazer uma arma emperrada funcionar novamente se torna uma ação de movimento e sua margem de crítico com armas de fogo aumenta em 1.", "req": "Pistoleiro Avançado"},
            {"nivel": 12, "nome": "Sincronia Perfeita",       "desc": "O alcance adicional concedido por Extensão do Corpo aumenta para 3 metros e você recebe vantagem em testes para evitar ser desarmado.", "req": "Extensão do Corpo"},
            {"nivel": 12, "nome": "Técnicas de Saque",        "desc": "Você aprende duas artes de combate de saque: Saque Devastador (prepare um saque; se atacado, use reação para contra-atacar e possivelmente anular o ataque) e Saque Trovão (ação completa: mova-se deslocamento e ataque todo inimigo dentro de 3m durante o movimento)."},
            # ── Nível 16 ──
            {"nivel": 16, "nome": "Crítico Aperfeiçoado",     "desc": "A margem do seu acerto crítico reduz em dois números, ao invés de um.", "req": "Crítico Melhorado"},
            {"nivel": 16, "nome": "Mestre da Postura",        "desc": "Quando entrar em postura, você pode assumir duas posturas ao mesmo tempo, recebendo os benefícios de ambas.", "req": "Assumir Postura"},
        ],
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
        "treinamentos": "Armas Simples e a Distância. Astúcia ou Vontade. 2 de Ofício/Feitiçaria/Ocultismo + 2 outras quaisquer.",
        "pericias_treinamento": {
            "lista": ["Ofício", "Feitiçaria", "Ocultismo"],
            "qtd_lista": 2,
            "qtd_livres": 2,
            "excluir": [],
        },
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Domínio dos Fundamentos",
                "desc": "Você aprende 2 Mudanças de Fundamento no 1° nível (mais 1 no nível 12): Feitiço Cruel (1-2PE: +2/+4 na CD do teste de resistência), Feitiço Distante (2PE: dobra alcance ou dá 9m a corpo-a-corpo), Feitiço Duplicado (2×nível em PE: adiciona segundo alvo), Feitiço Expansivo (3PE: aumenta área em 50%), Feitiço Potente (2PE: rola novamente dados de dano = mod. de atributo, usa os melhores), Feitiço Preciso (1-2PE: +2/+4 em rolagem de ataque) ou Feitiço Rápido (2×nível em PE: reduz custo de ação em 1, req. nível 6)."
            },
            {
                "nivel": 1,
                "nome": "Conjuração Aprimorada",
                "desc": "Sempre que utilizar um Feitiço que cause dano, você soma um bônus ao total baseado no nível do Feitiço: Nível 1-2 = mod. de Atributo; Nível 3 = 2× mod.; Nível 4 = 2× mod. + nível de personagem; Nível 5 = 2× mod. + 2× nível; Técnica Máxima = 3× mod. + 3× nível. Além disso, você passa a receber novos Feitiços em todo nível, ao invés de apenas nos níveis pares."
            }
        ],
        "habilidades_nivel": {
            4: ["Adiantar a Evolução – Ao invés do padrão, você acessa feitiços superiores mais cedo: nível 2 no 4°, nível 3 no 7°, nível 4 no 11°, nível 5 no 15°."],
            9: ["Teste de Resistência Mestre – Você se torna treinado em um segundo teste de resistência e mestre no concedido pela sua especialização."],
            10: ["Foco Amaldiçoado – Escolha um foco permanente: Destruição (todo Feitiço causa +1 dano/dado rolado + bônus de treinamento no dano), Economia (custo de todos os Feitiços −2, soma BT no PE máximo) ou Refino (recebe uma Aptidão ou Feitiço extra + soma ½ BT em todas as CDs e em rolagens de ataque amaldiçoado)."],
            20: ["O Honrado – Feitiços de nível 1, 2 e 3 têm custo reduzido pela metade; a CD de todos os Feitiços e Aptidões Amaldiçoadas aumenta em 5; você recebe +5 em rolagens de ataque para Feitiços e Aptidões Amaldiçoadas."]
        },
        "habilidades_catalogo": [
            # ── Nível 2 ──
            {"nivel": 2, "nome": "Abastecido pelo Sangue",    "desc": "Quando um inimigo morre dentro de 12 metros de você, você pode usar sua reação para recuperar PE = mod. de Int. ou Sab. Uma vez por descanso longo (duas vezes no nível 8, três vezes no nível 16)."},
            {"nivel": 2, "nome": "Conhecimento Aplicado",     "desc": "Sempre que for realizar um TR contra o efeito de um Feitiço, você pode gastar PE = metade do BT para receber +2 por ponto gasto no teste de resistência."},
            {"nivel": 2, "nome": "Conjuração Defensiva",      "desc": "Ao usar um Feitiço, você pode gastar 2 PE para, até o começo do seu próximo turno, receber um bônus em Defesa e um valor em RD igual ao nível do Feitiço usado."},
            {"nivel": 2, "nome": "Economia de Energia",       "desc": "Após um descanso curto, sua reserva é 1d4; após descanso longo, 1d6, aumentando em um dado a cada 5 níveis. Como uma ação comum, você pode adicionar a energia da reserva no seu valor atual."},
            {"nivel": 2, "nome": "Explosão Encadeada",        "desc": "Ao rolar o dano máximo em um dado de dano de um Feitiço de dano, você rola mais um dado de dano de mesmo valor, adicionando o resultado ao total. Funciona apenas uma vez por dado."},
            {"nivel": 2, "nome": "Finta Amaldiçoada",         "desc": "Você pode utilizar Fintar com seu atributo-chave ao invés de Presença e os efeitos de Desprevenido por fintar são aplicados na sua próxima conjuração de Feitiço."},
            {"nivel": 2, "nome": "Mente Plácida",             "desc": "Quando realizar um teste para manter concentração, você pode gastar 1 PE para receber +3 ou 2 PE para receber +5, e a CD é sempre reduzida em um valor igual ao seu mod. de Int. ou Sab."},
            {"nivel": 2, "nome": "Nova Habilidade",           "desc": "Ao obter esta habilidade, você pode imediatamente criar dois novos Feitiços ou três variações de liberação. Você pode pegar essa habilidade repetidas vezes."},
            {"nivel": 2, "nome": "Perturbação Amaldiçoada",   "desc": "Como uma ação comum, gaste 2 PE para perturbar uma criatura dentro de 9 metros (TR de Vontade). Em uma falha, ela recebe prejuízo em rolagens = mod. de Int. ou Sab. por uma quantidade de rolagens = BT."},
            {"nivel": 2, "nome": "Reação Rápida",             "desc": "Você passa a adicionar seu modificador de Inteligência ou Sabedoria no seu bônus de iniciativa."},
            {"nivel": 2, "nome": "Reforço Amaldiçoado",       "desc": "Sua CD de Especialização e Amaldiçoada aumenta em +2. No nível 10 esse aumento se torna +3 e no nível 20 se torna +4."},
            {"nivel": 2, "nome": "Sobrecarregar",             "desc": "Quando usar um Feitiço que força um TR, você pode gastar PE = BT para aumentar a dificuldade do teste. Para cada ponto gasto, a dificuldade aumenta em 1."},
            {"nivel": 2, "nome": "Técnicas de Combate",       "desc": "Você pode escolher duas armas quaisquer para se tornar treinado e para poder utilizar Inteligência ou Sabedoria nas jogadas de ataque e dano enquanto as manejando."},
            {"nivel": 2, "nome": "Zelo Recompensador",        "desc": "Sempre que suceder em um TR para evitar o efeito de um Feitiço, você recebe 1 PE temporário. A partir do nível 14 você passa a receber 2 pontos temporários."},
            # ── Nível 4 ──
            {"nivel": 4, "nome": "Até a Última Gota",         "desc": "Uma vez por descanso longo, caso esteja com menos da metade do seu máximo de PE, use uma ação comum para recuperar 1d4 + mod. de Int./Sab. em PE (aumentando em um dado a cada 5 níveis). Você recebe 1 ponto de exaustão após usar essa habilidade."},
            {"nivel": 4, "nome": "Ciclagem Maldita",          "desc": "Quando utilizar um Feitiço de dano diferente do último que você utilizou, ele causa dados de dano adicionais igual a metade do seu bônus de treinamento."},
            {"nivel": 4, "nome": "Determinação Energizada",   "desc": "Quando fizer um TR de Astúcia ou de Vontade, você pode pagar 1 PE para receber vantagem no teste, aumentando em +1 PE para cada teste após o primeiro na mesma rodada."},
            {"nivel": 4, "nome": "Energia Focalizada",        "desc": "Você escolhe uma perícia de TR (Fortitude, Reflexos, Astúcia ou Vontade) para ter metade do seu mod. de Sab. ou Int. somado a rolagens dela."},
            {"nivel": 4, "nome": "Energia Inacabável",        "desc": "Seu máximo de PE aumenta em um valor igual a metade do seu nível de Especialista em Técnicas."},
            {"nivel": 4, "nome": "Epifania Amaldiçoada",      "desc": "Ao obter essa habilidade, você aprende uma Aptidão Amaldiçoada. No nível 12 você recebe outra aptidão amaldiçoada."},
            {"nivel": 4, "nome": "Explosão Defensiva",        "desc": "Como uma Reação, quando for atingido por um ataque corpo a corpo, você pode gastar até PE = BT: para cada PE gasto, você reduz o dano em 5 e empurra o atacante em 3 metros para longe.", "req": "Aptidão Cobrir-se"},
            {"nivel": 4, "nome": "Feitiço Favorito",          "desc": "Escolha um Feitiço: ele recebe uma Melhoria de Ritual permanente, a qual não pode ser alterada após escolhida. A Melhoria não é contabilizada ao realizar um ritual."},
            {"nivel": 4, "nome": "Feitiços Refinados",        "desc": "Você passa a somar metade do seu bônus de treinamento no cálculo de CD dos seus Feitiços e Aptidões Amaldiçoadas."},
            {"nivel": 4, "nome": "Movimentos Imprevisíveis",  "desc": "Você pode adicionar seu modificador de Inteligência ou de Sabedoria na sua Defesa, limitado pelo seu nível."},
            {"nivel": 4, "nome": "Naturalidade com Rituais",  "desc": "Você pode utilizar Inteligência no lugar de Destreza em testes de Prestidigitação para realizar rituais.", "req": "Treinado em Prestidigitação"},
            {"nivel": 4, "nome": "Olhar Preciso",             "desc": "Você recebe um bônus de +2 em rolagens de ataque para Feitiços e aptidões amaldiçoadas. A cada 4 níveis, esse bônus aumenta em +1."},
            {"nivel": 4, "nome": "Preparação de Técnicas",    "desc": "Você pode preparar dois Feitiços por descanso longo para conjurar com custo reduzido pela metade na primeira vez que as usar. Nível mínimo do Feitiço: 1 (nível 2 no nível 5; nível 3 no nível 12; nível 4 no nível 16; nível 5 no nível 20)."},
            {"nivel": 4, "nome": "Sacrifício pela Energia",   "desc": "Você pode se infligir dano para recuperar PE. Para cada 6 de dano, você recupera 2 PE. Os PV perdidos não podem ser restaurados até o próximo descanso."},
            {"nivel": 4, "nome": "Versatilidade em Fundamentos","desc": "Durante um descanso curto, você pode alterar quais Mudanças de Fundamentos você possui, até um limite de trocas = metade do BT. Em um descanso longo, o limite se torna o BT inteiro."},
            # ── Nível 6 ──
            {"nivel": 6, "nome": "Bastião Interior",          "desc": "Você recebe vantagem para resistir às condições amedrontado, desorientado e enfeitiçado.", "req": "Treinado em Vontade"},
            {"nivel": 6, "nome": "Combate Amaldiçoado",       "desc": "Todo ataque feito com uma arma treinada por Técnicas de Combate causa dano adicional = BT. Você pode gastar 2 PE para que a arma cause dano como um nível acima durante todo o combate.", "req": "Técnicas de Combate"},
            {"nivel": 6, "nome": "Correção",                  "desc": "Uma vez por rodada, quando você for perder a concentração em um Feitiço, você pode gastar PE = nível do Feitiço para evitar perder a concentração."},
            {"nivel": 6, "nome": "Dominância em Feitiço",     "desc": "O custo de um Feitiço a sua escolha diminui em um valor igual a metade do nível dele, arredondado para cima."},
            {"nivel": 6, "nome": "Elevar Aptidão",            "desc": "Ao obter esta habilidade, você aumenta um dos seus Níveis de Aptidão em 1. Você pode pegar esta habilidade uma quantidade de vezes igual ao seu BT."},
            {"nivel": 6, "nome": "Especialização",            "desc": "Ao obter esta habilidade, você se torna mestre em 3 perícias nas quais você seja treinado, a sua escolha."},
            {"nivel": 6, "nome": "Incapaz de Falhar",         "desc": "Ao realizar uma rolagem de aptidão amaldiçoada (exceto Aptidões de Domínio), você pode gastar 2 PE para adicionar um valor = mod. de Int. ou Sab. no resultado. Apenas uma vez por Aptidão usada na rodada."},
            {"nivel": 6, "nome": "Mente Repartida",           "desc": "Você pode se manter concentrando em duas fontes diferentes simultaneamente."},
            {"nivel": 6, "nome": "Nível Perfeito",            "desc": "Todos os seus Feitiços de um nível a sua escolha têm a CD de resistência aumentada em 2. Nos níveis 12 e 18 você pode escolher outro nível de Feitiço."},
            {"nivel": 6, "nome": "Passo Rápido",              "desc": "Quando um inimigo se aproxima e você entra no alcance corpo a corpo dele, você pode, como uma reação, afastar-se em metade do seu movimento sem causar ataque de oportunidade."},
            {"nivel": 6, "nome": "Potência Concentrada",      "desc": "Uma vez por rodada, você pode gastar uma Ação de Movimento para fazer com que seu próximo Feitiço de dano com alvo único cause dano adicional = 5 × nível do Feitiço."},
            {"nivel": 6, "nome": "Ritualista",                "desc": "Você recebe +2 em testes para realizar Conjuração em Ritual e, metade do BT vezes por Descanso Longo, você pode colocar 1 melhoria adicional na Conjuração em Ritual."},
            # ── Nível 8 ──
            {"nivel": 8, "nome": "Expansão dos Fundamentos",  "desc": "Ao obter esta habilidade, você aprende mais uma Mudança de Fundamento. No nível 12 você aprende outro adicional."},
            {"nivel": 8, "nome": "Físico Amaldiçoado Defensivo","desc": "A quantidade de PEs que você pode gastar com a aptidão Cobrir-se aumenta em 2. Caso possua Cobertura Avançada, aumenta em +1.", "req": "Aptidão Cobrir-se"},
            {"nivel": 8, "nome": "Imbuir com Técnica",        "desc": "Quando for utilizar um Feitiço de dano (não especial ou em área), você pode, como uma Ação Bônus, gastar 2 PE adicionais para a imbuir em uma arma. Se acertar, além de causar dano, você causa o efeito do Feitiço.", "req": "Combate Amaldiçoado"},
            {"nivel": 8, "nome": "Liberações Expandidas",     "desc": "Ao obter esta habilidade, você recebe uma Liberação Máxima adicional. Nos níveis 12 e 16 você recebe mais uma liberação máxima."},
            {"nivel": 8, "nome": "Mira Aperfeiçoada",         "desc": "Você pode utilizar Mirar para jogadas de ataque amaldiçoado e recebe a Mudança de Fundamento Técnica Precisa. Caso já possua Técnica Precisa, o bônus conferido por ela aumenta em +1.", "req": "Olhar Preciso"},
            {"nivel": 8, "nome": "Primeiro Disparo",          "desc": "Durante a rolagem da iniciativa, você pode usar uma habilidade cujo custo de tempo seja Ação Bônus ou Ação Livre.", "req": "Treinado em Reflexos"},
            {"nivel": 8, "nome": "Revestimento Constante",    "desc": "Você recebe redução de dano contra todos os tipos, exceto na alma, igual ao seu bônus de treinamento.", "req": "Aptidão Cobrir-se"},
            {"nivel": 8, "nome": "Sustentação Avançada",      "desc": "Você pode manter um feitiço sustentado adicional e, no começo do combate, pode ativar um feitiço sustentado à sua escolha como Ação Livre, desde que possua custo de Ação Bônus ou inferior."},
            # ── Nível 10 ──
            {"nivel": 10, "nome": "Destruição Ampla",         "desc": "Quando utilizar um Feitiço em área, ela causa 5 de dano adicional para cada criatura além da primeira que estiver sendo afetada."},
            {"nivel": 10, "nome": "Destruição Focada",        "desc": "Quando utilizar um Feitiço de dano de alvo único, ela ignora RD = mod. de Int. ou Sab. e tem seu dano aumentado em dados = metade do BT."},
            # ── Nível 12 ──
            {"nivel": 12, "nome": "Economia de Energia Avançada","desc": "Os dados da energia colocada na economia aumentam para d6 em descanso curto e d8 em descanso longo. Colocar energia da economia no estoque atual agora é uma ação bônus.", "req": "Economia de Energia"},
            {"nivel": 12, "nome": "Esgrimista Jujutsu",       "desc": "Quando utilizar Combate Amaldiçoado, você pode também utilizar um Feitiço Auxiliar tendo você mesmo como alvo, desde que seu custo padrão seja uma Ação Bônus.", "req": "Combate Amaldiçoado"},
            {"nivel": 12, "nome": "Expansão Maestral",        "desc": "Você pode utilizar expansões de domínio possuindo apenas uma mão livre e ataques a distância não causam ataques de oportunidade contra você enquanto expandindo.", "req": "Aptidão Expansão de Domínio Completa"},
            {"nivel": 12, "nome": "Explosão Máxima",          "desc": "Para cada resultado máximo que conseguir, além de rolar um dado adicional, você soma +4 ao total de dano.", "req": "Explosão Encadeada"},
            {"nivel": 12, "nome": "Mestre das Aptidões",      "desc": "No começo de toda rodada, você recebe PE temporários = metade do BT, usados exclusivamente no uso de Aptidões Amaldiçoadas. Estes pontos não acumulam."},
            {"nivel": 12, "nome": "Sentidos Aguçados",        "desc": "Sua atenção aumenta em = metade do bônus de Int. ou Sab., e você adiciona o mesmo bônus a rolagens de Percepção. Além disso, você pode gastar 2 PE para se manter estável no ar.", "req": "Mestre em Percepção"},
            {"nivel": 12, "nome": "Versatilidade Ampliada",   "desc": "Todos seus Feitiços recebem 1 variação de liberação e você pode escolher um deles para ter uma variação de cada nível que você possua acesso."},
            # ── Nível 16 ──
            {"nivel": 16, "nome": "Manipulação Perfeita",     "desc": "Você pode escolher uma quantidade de Feitiços = BT para terem seu custo reduzido em metade do BT.", "req": "Dominância em Feitiço"},
            {"nivel": 16, "nome": "Sustentação Mestre",       "desc": "Você pode manter três feitiços sustentados ao invés de dois. Além disso, seu custo para sustentar feitiços é diminuído em 1, com um mínimo de 1.", "req": "Sustentação Avançada"},
        ],
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
        "treinamentos": "Armas Simples e a Distância. Astúcia ou Vontade. 1 de Ofício/Percepção/Persuasão + 2 outras quaisquer.",
        "pericias_treinamento": {
            "lista": ["Ofício", "Percepção", "Persuasão"],
            "qtd_lista": 1,
            "qtd_livres": 2,
            "excluir": [],
        },
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Treinamento em Controle",
                "desc": "Você é treinado para controlar Invocações com maior eficiência. Ao obter esta habilidade: recebe 2 Invocações iniciais (shikigamis ou corpos amaldiçoados); nos níveis 3, 6, 9, 10, 12, 15 e 18 recebe uma Invocação adicional. A quantidade de Invocações que pode manter ativas em campo aumenta em 1. Nos níveis 6, 12 e 18 a quantidade de comandos realizados com uma Ação Comum e Bônus aumenta em 1 (no nível 6, uma Ação Comum permite duas Invocações realizarem uma ação complexa, ou uma Invocação realizar duas)."
            }
        ],
        "habilidades_nivel": {
            4: ["Controle Aprimorado – Suas invocações recebem +2 em todos os testes que realizarem, aumentando em +1 para cada grau acima do quarto (+3 para terceiro grau, +4 para segundo etc.). Além disso, você pode utilizar Aptidões Amaldiçoadas das categorias Controle e Leitura a partir de suas Invocações (exceto Punho Divergente e Emoção da Pétala Decadente)."],
            6: ["Apogeu – Você encontra o caminho que deseja seguir como controlador. Escolha entre Controle Concentrado, Controle Disperso ou Controle Sintonizado (ver picker acima)."],
            9: ["Teste de Resistência Mestre – Você se torna treinado em um segundo teste de resistência e mestre no concedido pela sua especialização."],
            10: ["Reserva para Invocação – Uma vez por descanso curto, você pode usar a ação Invocar para trazer duas invocações com custo reduzido à metade ou uma invocação sem custo. Ao usar para Criar Horda, o custo total é reduzido pela metade."],
            20: ["Ápice do Controle – Suas invocações recebem duas ações/características adicionais sem influenciar no custo. Você pode invocar/ativar invocações como ação livre (se já podia como ação livre, custo reduzido em 2PE). Invocações de outras criaturas têm desvantagem em ações ofensivas contra você."]
        },
        "habilidades_catalogo": [
            # ── Nível 2 ──
            {"nivel": 2, "nome": "Aceleração",                  "desc": "Uma vez por rodada, você pode fazer com que uma Invocação se mova duas vezes ao invés de uma."},
            {"nivel": 2, "nome": "Camuflagem Aprimorada",       "desc": "Como Ação Comum, camufle-se em meio às suas invocações adjacentes: para cada Invocação adjacente, todo ataque contra você tem 10% de chance de errar (1 em 1d10). Dura enquanto houver invocações adjacentes."},
            {"nivel": 2, "nome": "Chamado Destruidor",          "desc": "Quando uma invocação sua conseguir acerto crítico, você pode, como Ação Livre, pagar 2PE para fazer com que uma invocação adjacente ataque o mesmo alvo."},
            {"nivel": 2, "nome": "Companheiro Amaldiçoado",     "desc": "Escolha uma invocação: ela se torna seu companheiro amaldiçoado e pode usar Apoiar como Ação Livre uma vez por rodada. Pode trocar o companheiro durante descanso ou interlúdio."},
            {"nivel": 2, "nome": "Dor Partilhada",              "desc": "Ao invocar, você pode criar um laço com uma invocação: quando ambos receberiam dano diferente de uma mesma área, os dois recebem o menor valor entre os dois."},
            {"nivel": 2, "nome": "Frenesi da Invocação",        "desc": "Uma vez por rodada, quando uma invocação realizar uma ação de ataque, você pode fazê-la repetir a ação (exceto Ações com Custo). Por uma rodada, ataques contra ela têm vantagem e ela perde 5 de Defesa e –5 em testes de resistência."},
            {"nivel": 2, "nome": "Guarda Viva",                 "desc": "Para cada Invocação dentro de 3 metros de você, sua Defesa aumenta em 1."},
            {"nivel": 2, "nome": "Invocações Móveis",           "desc": "O Deslocamento de todas suas Invocações aumenta em 1,5 metros. Nos níveis 6, 12 e 18 elas recebem +1,5m adicionais."},
            {"nivel": 2, "nome": "Invocações Resistentes",      "desc": "Os PV Máximos de todas suas Invocações aumentam em um valor igual ao seu Bônus de Treinamento × 5."},
            {"nivel": 2, "nome": "Invocações Treinadas",        "desc": "Todas suas Invocações se tornam treinadas em uma quantidade de Perícias adicional igual à metade do seu bônus de treinamento."},
            {"nivel": 2, "nome": "Melhoria de Controlador",     "desc": "Escolha uma das quatro melhorias para todas suas invocações: Agressividade (+1d6 dano, escala), Resistência (+2 Defesa + RD escalonável), Mobilidade (+1,5m de deslocamento, escala) ou Precisão (+2 em Jogadas de Ataque ou CD). Pode pegar até 4 vezes."},
            {"nivel": 2, "nome": "Otimização de Energia",       "desc": "Ao adquirir e em cada descanso, escolha uma habilidade com custo de cada invocação para ter seu custo reduzido em 1PE."},
            {"nivel": 2, "nome": "Técnicas de Combate",         "desc": "Escolha duas armas para se tornar treinado e poder usar Presença ou Sabedoria nas jogadas de ataque e dano com elas."},
            {"nivel": 2, "nome": "Visionário",                  "desc": "Ao criar uma invocação, a quantidade de ações e/ou características que ela pode receber aumenta em ½ bônus de treinamento (custo ainda aumenta normalmente)."},
            {"nivel": 2, "nome": "Proteger Invocação",          "desc": "Reação: quando uma invocação sua for receber dano suficiente para ser dissipada/exorcizada, outra invocação se move até ela e absorve o dano. Também pode gastar reação para reduzir dano de uma invocação atacada em Xd6 + mod. Presença/Sab (X = BT)."},
            {"nivel": 2, "nome": "Rede de Detecção",            "desc": "Para cada invocação dentro de 3 metros de você, você recebe +2 em rolagens de Percepção e +2 de atenção."},
            # ── Nível 4 ──
            {"nivel": 4, "nome": "Ação Corretiva",              "desc": "Quando uma invocação em 9 metros rolar uma perícia e tirar menos de 10 no dado, você pode gastar 2PE para transformar o resultado em 10."},
            {"nivel": 4, "nome": "Acompanhamento Amaldiçoado",  "desc": "Ao invocar, escolha uma invocação para acompanhá-lo. Quando você atacar uma criatura no alcance dela, ela pode usar uma Reação para atacar ou auxiliar o mesmo alvo."},
            {"nivel": 4, "nome": "Ataque em Conjunto",          "desc": "Ação Comum, uma vez por rodada: todas as invocações ativas atacam o mesmo alvo (2PE por invocação além da primeira). Cada invocação participante recebe +1 na jogada de ataque. Pode ser usado mod. Sab./Presença vezes por descanso longo."},
            {"nivel": 4, "nome": "Autonomia",                   "desc": "Ao ativar uma invocação, pague PE extra (2 por grau, 10 para grau especial) para ela ganhar turno próprio com uma ação + movimento sem precisar de comandos."},
            {"nivel": 4, "nome": "Companheiro Avançado",        "desc": "Seu companheiro amaldiçoado se torna também um aliado de um tipo a sua escolha (iniciante → veterano no nível 6 → mestre no nível 12). [Req: Companheiro Amaldiçoado]", "req": "Companheiro Amaldiçoado"},
            {"nivel": 4, "nome": "Crítico Brutal",              "desc": "Críticos de suas invocações causam +1 dado de dano. Ao crítico, você escolhe: reduzir Deslocamento do alvo em BT × 1,5m ou reduzir Defesa em ½ BT. Dura até seu próximo turno."},
            {"nivel": 4, "nome": "Domador de Maldições",        "desc": "No processo de domar uma maldição, você tem vantagem em todas as rolagens envolvidas e pode anular sua primeira falha."},
            {"nivel": 4, "nome": "Invocação Parcial",           "desc": "Você pode usar ações para realizar ações de uma invocação que não está ativa: Ação Comum = ação complexa; Ação Bônus = ação simples."},
            {"nivel": 4, "nome": "Potencial Superior",          "desc": "Todas suas invocações recebem 2 pontos de atributo adicionais por grau (2 para quarto grau, 10 para grau especial)."},
            {"nivel": 4, "nome": "Invocação Às",                "desc": "Seu companheiro amaldiçoado se torna sua Invocação Às, recebendo benefícios especiais detalhados na especialização. [Req: Companheiro Amaldiçoado]", "req": "Companheiro Amaldiçoado"},
            # ── Nível 6 ──
            {"nivel": 6, "nome": "Combate em Alcateia",         "desc": "Com uma arma de Técnicas de Combate, seu dano aumenta 1 nível para cada invocação no alcance de ataque do alvo. [Req: Técnicas de Combate + Apogeu Sintonizado]", "req": "Técnicas de Combate"},
            {"nivel": 6, "nome": "Concentrar Poder",            "desc": "Com apenas uma invocação em campo, você recebe benefícios crescentes por nível de personagem, descritos na especialização. [Req: Apogeu Concentrado]"},
            {"nivel": 6, "nome": "Hoste Amaldiçoada",           "desc": "Ao usar Criar Horda, reduza o limite de grau do Líder em 1 para criar duas hordas ao invés de uma (contam como uma para seu limite). [Req: Apogeu Disperso]"},
            {"nivel": 6, "nome": "Invocações Econômicas",       "desc": "Escolha 2 invocações para ter o custo de invocar/ativar reduzido em 2PE. No nível 12 escolhe mais uma, assim como no 18."},
            {"nivel": 6, "nome": "Proteção Avançada de Invocação", "desc": "Ao usar reação para absorver dano por uma invocação, você recebe apenas metade. A redução de dano normal aumenta para Xd8. Se adjacente, pode gastar 2PE para usar como Ação Livre. [Req: Proteger Invocação]", "req": "Proteger Invocação"},
            {"nivel": 6, "nome": "Táticas de Alcateia",         "desc": "Criaturas sendo flanqueadas por suas invocações têm a Defesa reduzida em ½ BT e penalidade igual em todos os testes de resistência."},
            # ── Nível 8 ──
            {"nivel": 8, "nome": "Aptidões de Controle",        "desc": "Aumente seu nível de aptidão em Aura, Controle e Leitura ou Barreira em 1. Pode pegar até 3 vezes, uma para cada categoria."},
            {"nivel": 8, "nome": "Atacar e Invocar",            "desc": "Quando usar a ação Atacar, gaste 2PE para trazer uma invocação ao campo simultaneamente, já contando para efeitos e habilidades como Acompanhamento Amaldiçoado."},
            # ── Nível 10 ──
            {"nivel": 10, "nome": "Buchas de Canhão",           "desc": "Você não precisa mais pagar PE adicionais para colocar invocações de quarto grau como membros de uma horda ou para invocá-las."},
            {"nivel": 10, "nome": "Crítico Aprimorado",         "desc": "19 também é crítico para suas invocações. Ao crítico, escolha dois efeitos: reduzir acerto do alvo em ½ BT ou reduzir todas as RDs dele em BT. [Req: Crítico Brutal]", "req": "Crítico Brutal"},
            {"nivel": 10, "nome": "Golpes Ágeis",               "desc": "Uma vez por rodada, quando uma invocação usar Acompanhamento Amaldiçoado, você pode gastar 2PE para realizar um ataque adicional. [Req: Acompanhamento Amaldiçoado]", "req": "Acompanhamento Amaldiçoado"},
            {"nivel": 10, "nome": "Técnicas de Oportunidade",   "desc": "Suas invocações passam a poder usar Ações de Ataque como reação, seguindo o mesmo gatilho de um ataque de oportunidade (exceto Ações com Custo)."},
            {"nivel": 10, "nome": "Flanco Avançado",            "desc": "Com uma criatura no alcance de ≥2 invocações, além dos efeitos de Táticas de Alcateia, ela recebe 1d8 de dano extra por ataque (+1d8 por invocação além das duas primeiras). [Req: Táticas de Alcateia]", "req": "Táticas de Alcateia"},
            {"nivel": 10, "nome": "Resistência Sobrecarregada", "desc": "Ao ativar/invocar uma invocação, gaste PE = ½ BT. Para cada ponto gasto, a invocação ganha +10 PV. [Req: Invocações Resistentes]", "req": "Invocações Resistentes"},
            # ── Nível 16 ──
            {"nivel": 16, "nome": "Fantoche Supremo",           "desc": "Durante descanso longo, escolha uma Invocação como Fantoche Supremo: +BT×5 PV, +2×BT Defesa, +4,5m movimento, uma ação complexa adicional por turno. Só pode ser invocada uma vez por descanso longo."},
            {"nivel": 16, "nome": "Mestre do Controle",         "desc": "Uma vez por rodada, como Ação Livre, gaste 2PE para fazer uma invocação se mover e realizar uma ação complexa adicional."},
        ],
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
        "treinamentos": "Armas Simples e Escudos. Astúcia ou Vontade. 2 de Ofício/Medicina/Prestidigitação + 3 outras quaisquer.",
        "pericias_treinamento": {
            "lista": ["Ofício", "Medicina", "Prestidigitação"],
            "qtd_lista": 2,
            "qtd_livres": 3,
            "excluir": [],
        },
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Suporte em Combate",
                "desc": "Você dispõe de um leque de capacidades para auxiliar em combate: pode usar Apoiar como uma ação bônus; pode curar uma criatura em alcance de toque como ação bônus em 2d6 + mod. de Presença ou Sabedoria, uma quantidade de vezes igual ao seu modificador de Presença ou Sabedoria por descanso. A cura escala: nível 4 = 2d12, nível 8 = 3d12, nível 12 = 6d8, nível 16 = 6d10."
            }
        ],
        "habilidades_nivel": {
            3: ["Presença Inspiradora – Você pode pagar 2PE para fazer com que, durante uma cena, todo aliado em 9 metros fique inspirado (+1 em toda rolagem de perícia). Pode gastar PE adicional = ½ mod. de Presença para aumentar o bônus em +1 por PE gasto."],
            5: ["Versatilidade – Sempre que realizar uma rolagem com uma perícia não treinada, você pode pagar 1PE para considerar como treinado. Pode usar uma quantidade de vezes igual ao seu mod. de Sabedoria por descanso."],
            6: ["Aptidão Automática: Energia Reversa – Você recebe a aptidão amaldiçoada Energia Reversa automaticamente."],
            8: ["Aptidão Automática: Liberação de Energia Reversa – Você recebe a aptidão amaldiçoada Liberação de Energia Reversa automaticamente."],
            9: ["Teste de Resistência Mestre – Você se torna treinado em um segundo teste de resistência e mestre no concedido pela sua especialização."],
            10: ["Medicina Infalível – Uma quantidade de vezes igual a ½ nível de Suporte + bônus de treinamento, você pode maximizar o valor de um dos dados de uma cura (vários usos para mais dados). Recupera os usos em descanso. Além disso, você soma seu bônus de treinamento no total de toda cura que realizar."],
            20: ["Suporte Absoluto – Uma vez por rodada, você pode usar Apoiar como Ação Livre. Sua quantidade de usos da habilidade Suporte em Combate é dobrada e você soma seu modificador de atributo de CD em toda cura que realizar."]
        },
        "habilidades_catalogo": [
            # ── Nível 2 ──
            {"nivel": 2, "nome": "Amizade Inquebrável",       "desc": "Escolha um Aliado Jogador como seu 'Amigo'. Ao terminar seu turno ao lado do Amigo, você pode como ação livre realizar a Ação 'Apoiar' no mesmo. Caso o Amigo morra, você só pode escolher outro amigo no próximo interlúdio."},
            {"nivel": 2, "nome": "Análise Profunda",          "desc": "Você pode gastar 1 PE para, como uma ação comum, analisar uma criatura realizando uma Percepção com CD 15 + ND dela. Caso suceda, você descobre uma característica dela. Para cada 5 pontos excedentes, descobre uma característica adicional. Pode ser usada uma vez por cena por criatura."},
            {"nivel": 2, "nome": "Apoio Avançado",            "desc": "Ao utilizar a ação de Apoiar, você pode fortalecer seu apoio com um efeito à sua escolha entre os apoios avançados disponíveis (Curativo, Defensivo, Focado, Ofensivo ou Estratégico)."},
            {"nivel": 2, "nome": "Comando Motivador",         "desc": "Como uma ação livre, você pode falar um comando para um aliado e gastar 2 PE para que, quando ele realizar a ação comandada, receba um bônus = BT na rolagem usada na ação."},
            {"nivel": 2, "nome": "Conceder Outra Chance",     "desc": "Ao ver um aliado dentro de 6 metros falhar em um teste, você pode gastar 3 PE para que ele role novamente, ficando com o melhor resultado. Pode ser usada BT vezes por descanso longo; descanso curto recupera metade dos usos."},
            {"nivel": 2, "nome": "Desvendar Terreno",         "desc": "Como uma Ação de Movimento, realize um teste de Percepção com CD definida pelo Narrador. Se suceder, você percebe pontos estratégicos (coberturas, terrenos difíceis) e, até o final da cena, recebe BT em testes de Percepção para encontrar coisas no terreno analisado."},
            {"nivel": 2, "nome": "Expandir Repertório",       "desc": "Você se torna treinado em uma quantidade de perícias = metade do seu BT. Você recebe também um bônus de +2 em uma perícia qualquer."},
            {"nivel": 2, "nome": "Mobilidade Avançada",       "desc": "Você recebe um bônus de +3 metros em seu movimento. Além disso, caso um aliado caia nas portas da morte, você pode, como uma reação, mover-se metade do seu movimento na direção dele."},
            {"nivel": 2, "nome": "Otimização de Espaço",      "desc": "Você recebe espaços de item adicionais no seu inventário, em um valor igual ao seu bônus de treinamento."},
            {"nivel": 2, "nome": "Pronto para Agir",          "desc": "Você adiciona seu modificador de Presença a Iniciativa. Além disso, seus aliados recebem um bônus igual a metade do modificador."},
            {"nivel": 2, "nome": "Protetor",                  "desc": "Quando um aliado dentro de 1,5m de você é atacado, você pode gastar 1 PE para, como uma Ação Livre, diminuir o dano causado em Xd10 + mod. de Presença ou Sabedoria (X = BT). É necessário estar com um escudo equipado."},
            {"nivel": 2, "nome": "Técnicas de Combate",       "desc": "Você pode escolher duas armas quaisquer para se tornar treinado e para poder utilizar Presença ou Sabedoria nas jogadas de ataque e dano enquanto as manejando."},
            {"nivel": 2, "nome": "Transmitir Conhecimento",   "desc": "Durante um descanso, você pode transmitir treinamento temporário em perícias para seus aliados: até metade do BT de perícias em descanso curto; até BT em descanso longo."},
            # ── Nível 4 ──
            {"nivel": 4, "nome": "Apoios Versáteis",          "desc": "Ao obter esta habilidade, você aprende um apoio avançado adicional. No 10° nível você recebe outro apoio avançado."},
            {"nivel": 4, "nome": "Guarda Sincronizada",       "desc": "Você pode utilizar uma Ação Bônus para sintonizar a guarda de todos os aliados dentro de 7,5 metros que possam te ver ou ouvir: para cada aliado dentro do alcance, todos os outros recebem +1 na Defesa."},
            {"nivel": 4, "nome": "Inspirar Aliados",          "desc": "Uma vez por cena, você pode gastar 1 PE e usar sua ação bônus para inspirar metade do BT de aliados. Uma quantidade de vezes = mod. de Presença ou Sab., dentro de 10 minutos, esses aliados podem adicionar 2d3 em uma jogada de ataque, teste de habilidade ou TR."},
            {"nivel": 4, "nome": "Intervenção",               "desc": "Como uma Ação Comum, você pode gastar 3 PE para encerrar uma condição fraca afetando um aliado dentro de alcance de toque. Nos níveis 6, 12 e 18 você se torna capaz de encerrar condições médias, fortes e extremas respectivamente, com o custo em PE aumentando em 3 para cada nível superior."},
            {"nivel": 4, "nome": "Negação Crítica",           "desc": "Uma quantidade de vezes igual a 1 + metade do BT, por cena, você pode pagar 3 PE para negar uma falha crítica que você possa ver dentro de 12 metros."},
            {"nivel": 4, "nome": "No Último Segundo",         "desc": "Ao iniciar uma rodada com um ou mais aliados com 2 fracassos nos testes da porta da morte, aumente sua iniciativa atual em +5. Caso aja primeiro por causa desse bônus, você anula terreno difícil, tem seu movimento aumentado em 4,5m e recebe +5 de Defesa contra Ataques de Oportunidade."},
            {"nivel": 4, "nome": "Pré-Análise",               "desc": "Você não pode ser surpreendido e seu valor de atenção recebe um bônus de +5. Você pode escolher um aliado para não ser surpreendido.", "req": "Treinado em Percepção"},
            {"nivel": 4, "nome": "Recompensa pelo Sucesso",   "desc": "Ao utilizar Comando Motivador, você pode reduzir o bônus fornecido pela metade e, caso o aliado motivado ainda assim suceda, ele ganha 2 PE.", "req": "Comando Motivador"},
            {"nivel": 4, "nome": "Sintonização Vital",        "desc": "Quando curar um aliado, você pode gastar 3 PE para que outra criatura dentro de 3 metros (incluindo você) recupere PV = metade da cura original."},
            # ── Nível 6 ──
            {"nivel": 6, "nome": "Contra-Ataque",             "desc": "Dobro do mod. de Presença ou Sab. vezes por descanso, como uma reação, gaste 1 PE para aumentar a Defesa de um aliado em BT. Se isso fizer com que um ataque erre, você ou o aliado podem gastar 1 PE para realizar um ataque como Ação Bônus no próximo turno."},
            {"nivel": 6, "nome": "Cura Avançada em Grupo",    "desc": "Você pode usar sua habilidade de cura em grupo: ao curar um alvo, você pode pagar 2 PE para curar mais um alvo, com um limite igual ao seu bônus de treinamento."},
            {"nivel": 6, "nome": "Devolver na Mesma Moeda",   "desc": "Quando um aliado que você possa ver é afetado por uma condição, você pode gastar 2 PE para, como uma Ação Livre, fazer com que o próximo TR de um inimigo para evitar uma condição do aliado possua desvantagem."},
            {"nivel": 6, "nome": "Disseminar Cura",           "desc": "Ao utilizar um Feitiço de cura, você pode escolher um alvo adicional, gastando uma quantidade de PE igual ao nível da técnica adicional."},
            {"nivel": 6, "nome": "Incitar Vigor",             "desc": "Como uma ação bônus, você pode gastar 3 PE para fazer com que uma criatura a alcance de toque possa gastar seus dados de vida para se curar."},
            {"nivel": 6, "nome": "Inimigo Comum",             "desc": "Como uma ação bônus, gaste 2 PE para escolher um inimigo comum entre mod. de Presença ou Sab. pessoas. Ao atacar o inimigo comum, cada pessoa adiciona metade do bônus de Presença ou Sab. no acerto e o modificador inteiro no dano."},
            {"nivel": 6, "nome": "Posicionamento Estratégico","desc": "Durante o seu turno, você pode reduzir seu movimento a 0 para permitir que um dos seus aliados se mova, como Ação Livre."},
            # ── Nível 8 ──
            {"nivel": 8, "nome": "Aptidões de Suporte",       "desc": "Ao obter esta habilidade, você pode aumentar o seu nível de aptidão em Aura, Controle e Leitura ou Energia Reversa em 1. Você pode pegar esta habilidade três vezes, uma para cada aptidão."},
            {"nivel": 8, "nome": "Contaminar com Determinação","desc": "Uma vez por cena, gaste 4 PE para, como uma ação comum, fazer com que você e dois aliados recebam vantagem em todo TR por duas rodadas. Cada aliado a mais aumenta o custo em 2 PE."},
            {"nivel": 8, "nome": "Criar Medicina",            "desc": "Durante um descanso curto, você pode recuperar 2 PE a menos para criar metade do BT de remédios; em um descanso longo, quantidade = BT com 4 PE a menos. Um remédio cura = sua cura de Suporte em Combate, dura 1 dia e consome uma ação comum para usar.", "req": "Treinado em Ferramentas de Médico"},
            {"nivel": 8, "nome": "Cura Aperfeiçoada",         "desc": "Caso você tire 1 ou 2 em um dado de cura, você pode escolher rolar novamente o dado, ficando com o melhor resultado."},
            {"nivel": 8, "nome": "Elevar Sucesso",            "desc": "Quando um aliado dentro de 4,5 metros suceder em um TR, você pode, como uma reação, gastar 2 PE para somar +5 ao resultado, com a possibilidade de se tornar um sucesso crítico."},
            {"nivel": 8, "nome": "Físico Controlado",         "desc": "Você passa a somar seu mod. de Presença ou Sabedoria ao invés de Constituição nos PV, com um limite de +4. Ao adquirir esta habilidade, você recalcula sua vida.", "req": "Treinado em Fortitude"},
            {"nivel": 8, "nome": "Motivação pelo Triunfo",    "desc": "Quando um inimigo é reduzido a 0 PV ou morto por você ou um aliado, você pode conceder PV temporários = 2× nível de Suporte para todos os aliados que causaram dano nesse inimigo. Lacaios concedem metade."},
            {"nivel": 8, "nome": "Pressão do Médico",         "desc": "Ao entrar nas portas da morte, você não fica inconsciente. Você pode tentar se estabilizar sozinho com CD +10, mas ao fazer isso você recebe uma falha nos testes de morte.", "req": "Mestre em Medicina"},
            {"nivel": 8, "nome": "Sustentação Avançada",      "desc": "Você pode manter um feitiço sustentado adicional e, no começo do combate, pode ativar um feitiço sustentado à sua escolha como Ação Livre, desde que possua custo de Ação Bônus ou inferior."},
            # ── Nível 10 ──
            {"nivel": 10, "nome": "Descarga Reanimadora",     "desc": "Como uma Ação Completa, gaste 10 PE para estabilizar imediatamente um aliado nas portas da morte ao alcance de toque, independente de quanta vida negativa ele tenha, e ele recupera PV = sua cura de Suporte em Combate.", "req": "Aptidão Cura Amplificada"},
            {"nivel": 10, "nome": "Necessidade de Continuar", "desc": "Quatro vezes por cena, se você estiver com menos da metade da vida máxima, você recebe PV temporários = bônus de Medicina + mod. de Presença ou Sab., no começo do seu turno.", "req": "Treinado em Vontade"},
            {"nivel": 10, "nome": "Olhar Aguçado",            "desc": "Você pode gastar 2 PE e usar sua ação bônus para analisar um inimigo, fazendo com que o primeiro ataque de todo aliado cause dano adicional = BT × 5. Pode ser usada duas vezes por criatura.", "req": "Treinado em Percepção"},
            {"nivel": 10, "nome": "Táticas Defensivas",       "desc": "Você pode escolher um tipo de dano Elemental para que você e dois aliados sejam resistentes. Em um descanso longo, você pode trocar esses tipos de dano e os aliados recebendo o benefício."},
            # ── Nível 12 ──
            {"nivel": 12, "nome": "Ajustes em Equipamento",   "desc": "Durante um descanso curto, você pode escolher BT equipamentos para receberem o efeito de um Encantamento que não possuam. Em um Descanso Longo, a quantidade se torna 2×BT. O efeito fica ativo até o próximo descanso.", "req": "Treinado em Ferramentas de Ferreiro"},
            {"nivel": 12, "nome": "Interferência",            "desc": "Como uma reação, gaste 2 PE para forçar um inimigo dentro de 9 metros a rolar novamente um teste, ficando com o menor resultado. Após usar essa habilidade você pode conceder a um aliado dentro de 4,5 metros vantagem na próxima rolagem."},
            {"nivel": 12, "nome": "Não Desista!",             "desc": "Ao ver um aliado atingir 0 ou menos de vida, você pode gastar 3 PE e fazer um teste de Persuasão contra a CD de estabilização. Se passar, o aliado continua de pé com 0 de vida durante uma rodada. Pode ser usada para negar efeitos negativos de habilidades metade do BT vezes."},
            {"nivel": 12, "nome": "Reação Necessária",        "desc": "Uma vez por rodada, caso não possua uma reação, você pode gastar 3 PE para realizar uma reação adicional."},
            {"nivel": 12, "nome": "Sobrecura",                "desc": "Ao curar um aliado que já está com o máximo de vida, ele recebe o dobro do excedente como vida temporária, com um limite = 2× nível de suporte. Você pode também conceder 5 × mod. de Presença ou Sab. de Vida Temporária a alguém já com vida completa."},
            # ── Nível 14 ──
            {"nivel": 14, "nome": "Apoio Abrangente",         "desc": "Quando utilizar Apoio Avançado, você pode colocar dois efeitos ao invés de um só.", "req": "Apoio Avançado"},
            # ── Nível 16 ──
            {"nivel": 16, "nome": "Purificação da Alma",      "desc": "Uma quantidade de vezes = mod. de Presença, você pode restaurar a integridade de alguém em 50%. Além disso, o seu Bônus de Treinamento é adicionado ao número de usos da sua cura."},
            {"nivel": 16, "nome": "Sustentação Mestre",       "desc": "Você pode manter três feitiços sustentados ao invés de dois. Além disso, seu custo para sustentar feitiços é diminuído em 1, com um mínimo de 1.", "req": "Sustentação Avançada"},
        ],
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
        "treinamentos": "Todas as armas e escudos. Fortitude e Reflexos (ambos). 1 de Ofício + 4 outras quaisquer (exceto Feitiçaria).",
        "pericias_treinamento": {
            "lista": ["Ofício"],
            "qtd_lista": 1,
            "qtd_livres": 4,
            "excluir": ["Feitiçaria"],
        },
        "habilidades_base": [
            {
                "nivel": 1,
                "nome": "Restrito pelos Céus",
                "desc": "Para compensar a falta de energia amaldiçoada, você recebe: pode adicionar seu mod. de Força ou Constituição na Defesa (limitado pelo nível); começa com uma ferramenta amaldiçoada de quarto grau e um meio de ver maldições; no 4° nível e a cada 4 níveis recebe uma Dádiva do Céu; possui Pontos de Estamina (4 por nível) no lugar de PE — recupera tudo em descanso longo ou metade em descanso curto. Além disso, possui um Estilo Marcial exclusivo."
            }
        ],
        "habilidades_nivel": {
            2: ["Ataque Furtivo – Uma vez por turno, ao realizar um ataque surpresa, contra alvo desprevenido ou flanqueando, adicione 1d8 ao dano. Escala: 2d8 no nível 3, 3d8 no 6, 4d8 no 9, 5d8 no 12, 6d8 no 15.",
                "Versatilidade – Você recebe +1 em todas as perícias. No 10° nível esse bônus se torna +2."],
            3: ["Esquiva Sobre-humana – Você recebe +1 em sua Defesa e em rolagens de Reflexos. Esse bônus aumenta em +1 no nível 9 e no nível 16. A partir do 10° nível, a margem de crítico em Reflexos reduz em ½ bônus de treinamento."],
            4: ["Implemento Celeste – Você recebe +2 na CD de suas habilidades de Restringido e técnicas marciais. Esse bônus aumenta em 1 nos níveis 8° e 16°."],
            9: ["Teste de Resistência Mestre – Você se torna mestre nos dois Testes de Resistência concedidos pela sua especialização."],
            10: ["Restrição Definitiva – Seu nível de EA alcançou o zero absoluto. Benefícios: vantagem em furtividade contra usuários de EA (eles têm desvantagem para te perceber); você vê o traçado da alma sem precisar de ferramenta; toda arma que manejar conta como um nível de dano acima; deslocamento +3m; se mestre em perícia/TR de Força, Destreza ou Constituição, soma BT inteiro ao invés de metade; imune a expansões de domínio."],
            20: ["Libertação do Destino – Subvertendo sua restrição celeste, você recebe resistência a todo dano físico (cortante, perfurante e impacto) mais um tipo a sua escolha (exceto alma); +5 em rolagens de ataque; soma metade do seu nível de personagem no total de dano."]
        },
        "habilidades_catalogo": [
            # ── Nível 2 ──
            {"nivel": 2, "nome": "Apropriar-se",              "desc": "Você recebe um bônus de +3 em testes para Desarmar ou evitar ser desarmado."},
            {"nivel": 2, "nome": "Aproximação Instintiva",    "desc": "Quando um inimigo termina o turno dentro de metade do seu deslocamento, você pode, como uma ação livre, se mover até metade do seu movimento para um espaço mais próximo. Esse movimento ignora terreno difícil e não causa ataques de oportunidade. Caso o inimigo acabe no seu alcance, você pode gastar 2 estamina para realizar uma manobra."},
            {"nivel": 2, "nome": "Ataque Inconsequente",      "desc": "Uma vez por rodada, ao realizar um ataque, você pode escolher atacar inconsequentemente: você recebe vantagem na jogada de ataque e +5 na rolagem de dano dele. Porém, ao realizar um golpe inconsequente, você fica Desprevenido por 1 rodada."},
            {"nivel": 2, "nome": "Existência Imperceptível",  "desc": "Você recebe um bônus de +2 em rolagens de Furtividade. Além disso, sua penalidade em Furtividade por atacar e fazer outras ações chamativas é reduzida para -4."},
            {"nivel": 2, "nome": "Finta Melhorada",           "desc": "Você passa a poder somar o seu Mod. de Destreza, ao invés de Presença, em rolagens de Enganação para fintar. Além disso, acertar um inimigo desprevenido pela sua finta causa um dado de dano adicional."},
            {"nivel": 2, "nome": "Golpe Impactante",          "desc": "Uma vez por rodada, ao realizar um ataque corpo a corpo, você pode também realizar a ação de Empurrar como parte do mesmo ataque. Caso tenha sucesso em empurrar, ele recebe Xd6 de dano adicional (X = metade do mod. de Força)."},
            {"nivel": 2, "nome": "Imitação",                  "desc": "Ao ver uma habilidade ativa de especialização marcial, manobra ou postura, você pode copiá-la como uma reação e deve usá-la no próximo turno. Pode tentar aprender a habilidade com TR de Percepção CD35 (diminui 2 a cada tentativa). Se aprender, não precisa mais ver para copiar."},
            {"nivel": 2, "nome": "Manejo Superior",           "desc": "O dano de toda arma que você manejar conta como um nível acima e suas rolagens de dano recebem um bônus igual ao seu bônus de treinamento."},
            {"nivel": 2, "nome": "Roubo de Habilidade",       "desc": "Você pode aprender uma habilidade de Especialista em Combate ou Lutador que não dependa de energia amaldiçoada. Pode pegar BT vezes, roubando habilidades diferentes."},
            {"nivel": 2, "nome": "Surto de Adrenalina",       "desc": "Como uma ação livre, gaste 3 estamina para entrar em surto de adrenalina: RD a todos os tipos = metade do nível; bônus de 1 + metade do BT em Fortitude e Reflexos; bônus em Percepção = BT. Dura uma rodada, gastando 1 estamina adicional por rodada extra."},
            {"nivel": 2, "nome": "Valorizar Invocação",       "desc": "Caso uma das suas invocações dentro de 3 metros vá ser exorcizada, você pode gastar 1 estamina e usar sua reação para receber o golpe letal em troca de manter a invocação viva. Ao defender uma invocação, você recebe PV temporários = nível de personagem."},
            # ── Nível 4 ──
            {"nivel": 4, "nome": "Ação Ágil",                 "desc": "Uma vez por turno você pode gastar 2 pontos de estamina para receber uma Ação Ágil, a qual pode ser utilizada para: Andar, Desengajar ou Esconder."},
            {"nivel": 4, "nome": "Adrenalina Intensificadora","desc": "Ao entrar em surto de adrenalina, você pode pagar 2 estamina adicionais para distribuir um bônus de +4 entre Atletismo e Acrobacia, além de poder pagar 1 estamina para vantagem em uma rolagem de cada, uma vez por cena."},
            {"nivel": 4, "nome": "Caçador de Feiticeiros",    "desc": "No começo de uma cena, gaste 2 estamina para receber 2 RD, +1 em TRs e ataques, e +1d6 de dano contra todos os feiticeiros presentes. A cada 5 níveis, gaste mais 2 para aumentar os bônus."},
            {"nivel": 4, "nome": "Desenvolver Ideias",        "desc": "Você recebe duas técnicas marciais adicionais ao obter essa habilidade."},
            {"nivel": 4, "nome": "Foco no Inimigo",           "desc": "Ao iniciar um combate, gaste 2 estamina e escolha um inimigo como foco. Ao atacá-lo, você recebe +2 para acertar e causa 1d6 de dano a mais (1d8 no nível 6, 1d10 no 12, 1d12 no 16) e +5 em Percepção e Atenção contra ele."},
            {"nivel": 4, "nome": "Ponto Cego",                "desc": "Se mover pelo espaço de um inimigo não conta como terreno difícil e, enquanto estiver no espaço de um inimigo, você recebe camuflagem leve (20% de chance de falha). A partir do 10° nível, pode realizar rolagem de furtividade para obter camuflagem total (40%)."},
            {"nivel": 4, "nome": "Resiliência pela Adrenalina","desc": "Durante um Surto de Adrenalina, você pode pagar 1 estamina para adicionar 2d3 ao resultado de um TR. Caso não seja treinado e falhe, você pode rolar novamente.", "req": "Surto de Adrenalina"},
            {"nivel": 4, "nome": "Técnicas de Memorização",   "desc": "Ao obter essa habilidade, você pode aprender uma habilidade adicional a partir da Imitação.", "req": "Imitação"},
            # ── Nível 6 ──
            {"nivel": 6, "nome": "Aprimoramento Celeste",     "desc": "Você passa a somar metade do modificador do seu atributo chave em sua CD de Especialização."},
            {"nivel": 6, "nome": "Ataque Extra",              "desc": "Ao realizar a ação Atacar, você pode gastar 2 pontos de estamina para atacar duas vezes ao invés de uma."},
            {"nivel": 6, "nome": "Ataque Inconsequente Aprimorado","desc": "O bônus em dano ao usar o ataque inconsequente aumenta para +10 e, ao utilizar a habilidade, você recebe 2d6+4 PV temporários.", "req": "Ataque Inconsequente"},
            {"nivel": 6, "nome": "Corpo de Aço",              "desc": "Seus PV máximos aumentam em um valor = seu valor de Constituição, e você pode pagar 2 estamina para, durante uma cena, se curar em 2d8 + mod. de Constituição no começo de todo turno. No nível 10 e 15, gaste 1 estamina adicional para aumentar a cura em 1d8."},
            {"nivel": 6, "nome": "Corredor Fantasma",         "desc": "Ao se mover, você pode andar em paredes, no entanto, não pode terminar seu turno em uma. Você recebe um bônus de +2 em testes para reduzir dano de queda. Caso possua Agilidade Exímia, você pode correr em tetos."},
            {"nivel": 6, "nome": "Disparada Trovejante",      "desc": "Ao receber um ataque corpo a corpo, você pode gastar 3 estamina para reduzir o dano a metade e se mover até 4,5 metros para longe do atacante."},
            {"nivel": 6, "nome": "Frenesi",                   "desc": "Durante o Surto de Adrenalina, sempre que realizar um ataque, ele causa +4 de dano adicional. No 12° nível, esse bônus se torna +8; no 16° nível, +12.", "req": "Surto de Adrenalina"},
            {"nivel": 6, "nome": "Movimento Reativo",         "desc": "Uma vez por rodada, quando um oponente dentro de um alcance igual ao seu movimento iniciar uma ação que permitiria Ataque de Oportunidade, você pode gastar 2 estamina para se locomover até ele como ação livre e executar o Ataque de Oportunidade."},
            # ── Nível 8 ──
            {"nivel": 8, "nome": "Ainda de Pé",               "desc": "Uma vez por descanso curto ou longo, quando você for chegar a 0 PV, você pode se manter de pé e curar em 3d10 + nível de personagem (aumentando em +1d10 nos níveis 12, 16 e 20). Caso o dano fosse suficiente para morte instantânea, você resiste e fica com 1 de vida."},
            {"nivel": 8, "nome": "Arremetida Encoberta",      "desc": "Ao realizar o Ataque Furtivo da rodada, você recebe vantagem no golpe. Caso o acerto já seja garantido, você recebe +1d no dano do Ataque Furtivo."},
            {"nivel": 8, "nome": "Barreira Inamovível",       "desc": "Sempre que fizer um TR de Fortitude e o resultado natural for menor que seu mod. de Constituição, você pode gastar 2 estamina para transformar o resultado natural no seu mod. de Constituição. Você não pode ser movido a força e tem vantagem para resistir a ser agarrado."},
            {"nivel": 8, "nome": "Força Imparável",           "desc": "Sempre que fizer um TR de Reflexos e o resultado natural for menor que seu mod. de Destreza, você pode gastar 2 estamina para transformar o resultado natural no seu mod. de Destreza. Você se torna treinado em um TR à sua escolha e mestre em outro TR no qual já seja treinado."},
            {"nivel": 8, "nome": "Imitação Perfeita",         "desc": "Você se torna capaz de copiar habilidades passivas de especializações marciais e estilos de combate (CD 40, diminui em 2 por tentativa). Pode também aprender uma habilidade passiva e um estilo de combate.", "req": "Imitação"},
            {"nivel": 8, "nome": "Presença Ameaçadora",       "desc": "Você pode gastar 1 estamina para fazer com que toda criatura que consiga te ver realize um TR de Vontade. Em uma falha, fica amedrontada por 2 rodadas; em um sucesso, fica abalada. Uma vez por cena por criatura."},
            {"nivel": 8, "nome": "Reação Rápida",             "desc": "Caso já tenha gasto a sua reação, você pode pagar 2 estamina para realizar uma reação adicional, uma vez por rodada."},
            {"nivel": 8, "nome": "Respeito Celeste",          "desc": "Ao obter essa habilidade, você recebe uma dádiva do céu adicional. A partir do nível 12, você pode pegar esta habilidade outra vez."},
            # ── Nível 10 ──
            {"nivel": 10, "nome": "Assassinar",               "desc": "Durante a primeira rodada de um combate, ao atacar uma criatura desprevenida a partir da furtividade ou surpresa, seu primeiro ataque é um crítico garantido."},
            {"nivel": 10, "nome": "Mente Limpa",              "desc": "Você recebe vantagem para resistir às seguintes condições: Amedrontado, Cego, Enfeitiçado e Surdo."},
            {"nivel": 10, "nome": "Perceber o Ar",            "desc": "Você é imune a danos de queda, conseguindo se apoiar no ar (altura máxima = dobro do deslocamento). Ao pular, pode realizar outro pulo em seguida (dois no nível 13, três no nível 17). Quando for alvo de um ataque, você pode gastar 2 estamina e sua reação para desviar com Acrobacia vs. Reflexos do atacante."},
            {"nivel": 10, "nome": "Precisão Forçada",         "desc": "Uma vez por rodada, quando você faz um ataque corpo a corpo, você pode pagar 3 estamina. Se acertar o ataque, causa dano máximo, sem necessidade de rolar danos."},
            {"nivel": 10, "nome": "Retaliação",               "desc": "Se você receber dano de um inimigo que esteja dentro de seu alcance, você pode gastar 2 estamina e usar sua reação para realizar um ataque contra ele."},
            # ── Nível 12 ──
            {"nivel": 12, "nome": "Adrenalina Absoluta",      "desc": "Ao iniciar um surto de adrenalina, você pode escolher pagar 4 estamina para ativar e 2 por rodada para manter. Enquanto ativo: ataque extra custa 1 estamina, +3 metros de Deslocamento, DEF aumenta em 2."},
            {"nivel": 12, "nome": "Pináculo Físico",          "desc": "Você recebe +4 pontos de estamina máximos e pode escolher aumentar o valor de dois atributos entre Força, Destreza e Constituição em 2. No nível 16, o valor de ambos os atributos escolhidos aumentam novamente em 2."},
            {"nivel": 12, "nome": "Rejeitar a Morte",         "desc": "Quando estiver nas portas da morte, você pode receber uma falha garantida para fazer um TR de Fortitude com CD 15 + 1 para cada 3 PV negativos. Se passar, você fica com 1 de vida e recebe 1 ponto de exaustão.", "req": "Ainda de Pé"},
            # ── Nível 16 ──
            {"nivel": 16, "nome": "Entre as Sombras",         "desc": "Agora o Ataque Furtivo aplica quando você está em camuflagem ou cobertura. Ao realizar um Ataque Furtivo, você pode acumular até uma vantagem adicional (totalizando 3d20). Caso seja acerto garantido, a margem de crítico é reduzida em 2.", "req": "Arremetida Encoberta"},
            {"nivel": 16, "nome": "Instintos Aguçados",       "desc": "Enquanto seus pontos de estamina e de vida excederem metade do máximo deles, você recebe uma reação adicional por rodada.", "req": "Reação Rápida"},
            {"nivel": 16, "nome": "Mesmo Morto",              "desc": "Ao cair para 0 de vida (sem uso de Ainda de Pé), ao invés de ir para as Portas da Morte você continua de pé normalmente. No final de todo turno, realize um TR de Fortitude CD25 + 1 para cada 5 PV negativos. Caso falhe, você cai imediatamente com 1 falha.", "req": "Rejeitar a Morte"},
        ],
    },
}

# Perícias: nome → atributo base  (lista oficial — p.284)
# Graus: nenhum (só atributo) | treinado (+BT) | mestre (+2×BT)
PERICIAS = {
    "Acrobacia":       "destreza",
    "Atletismo":       "forca",
    "Direção":         "sabedoria",
    "Enganação":       "presenca",
    "Feitiçaria":      "inteligencia",   # *T — requer treinamento
    "Furtividade":     "destreza",
    "História":        "inteligencia",
    "Intimidação":     "presenca",
    "Intuição":        "sabedoria",
    "Investigação":    "inteligencia",
    "Medicina":        "sabedoria",      # *T — requer treinamento
    "Ocultismo":       "sabedoria",
    "Ofício":          "inteligencia",   # *T — requer treinamento
    "Percepção":       "sabedoria",
    "Performance":     "presenca",
    "Persuasão":       "presenca",
    "Prestidigitação": "destreza",       # *T — requer treinamento
    "Sobrevivência":   "sabedoria",
    "Tecnologia":      "inteligencia",
    "Teologia":        "inteligencia",
}

# Perícias que só funcionam se o personagem for Treinado nelas
PERICIAS_TREINO = {"Feitiçaria", "Medicina", "Ofício", "Prestidigitação"}

ATTR_ABREV = {
    "forca": "FOR", "destreza": "DES", "constituicao": "CON",
    "inteligencia": "INT", "sabedoria": "SAB", "presenca": "PRE",
}

TESTES_RESISTENCIA = ["Fortitude", "Reflexos", "Vontade", "Astúcia"]

# ─── NÍVEIS DE APTIDÃO (Cap. 8, p. 173) ────────────────────────────────────────
NIVEIS_APTIDAO_CATEGORIAS = [
    {
        "id": "aura",
        "nome": "Aura (AU)",
        "icone": "💥",
        "desc": "Conhecimento e refinamento da própria energia amaldiçoada como aura.",
    },
    {
        "id": "controle_leitura",
        "nome": "Controle e Leitura (CL)",
        "icone": "👁",
        "desc": "Capacidade de liberar, controlar e ler fluxos de energia amaldiçoada.",
    },
    {
        "id": "barreira",
        "nome": "Barreira (BAR)",
        "icone": "🛡",
        "desc": "Uso de técnicas de barreira com excelência e versatilidade.",
    },
    {
        "id": "dominio",
        "nome": "Domínio (DOM)",
        "icone": "🌐",
        "desc": "Aptidão em técnicas de domínio e expansões de domínio.",
    },
    {
        "id": "energia_reversa",
        "nome": "Energia Reversa (ER)",
        "icone": "💚",
        "desc": "Proficiência no uso da energia reversa para cura e regeneração.",
    },
]

NIVEIS_APTIDAO_LABELS = {
    0: {"nome": "Nenhum",    "cor": "#6b7280"},
    1: {"nome": "Básico",    "cor": "#3b82f6"},
    2: {"nome": "Médio",     "cor": "#22c55e"},
    3: {"nome": "Avançado",  "cor": "#f59e0b"},
    4: {"nome": "Superior",  "cor": "#a78bfa"},
    5: {"nome": "Supremo",   "cor": "#ec4899"},
}

# ─── APOGEU DO CONTROLADOR ────────────────────────────────────────────────────
APOGEU_OPCOES = [
    {
        "id": "concentrado",
        "nome": "Controle Concentrado",
        "desc": (
            "Você opta por concentrar suas forças e foco em uma única invocação, a qual sozinha "
            "se torna uma arma absoluta. Ao invés de invocar/ativar duas invocações como uma ação "
            "bônus, você pode invocar apenas uma como ação livre."
        ),
    },
    {
        "id": "disperso",
        "nome": "Controle Disperso",
        "desc": (
            "Você prefere controlar diversas invocações, mantendo a quantidade sempre em número "
            "superior. O número de invocações que você pode manter ativas em campo aumenta em 1, "
            "assim como a quantidade que você pode invocar/ativar com uma ação aumenta em 1. "
            "Além disso, você recebe acesso à ação Criar Horda. A partir do nível 12, o número "
            "de invocações que você pode manter ativas e invocar/ativar com uma ação aumenta em 1, "
            "assim como você pode criar duas hordas como parte de uma mesma ação de Criar Horda."
        ),
    },
    {
        "id": "sintonizado",
        "nome": "Controle Sintonizado",
        "desc": (
            "Você prefere ficar em sintonia com suas invocações, não deixando que apenas elas "
            "lutem sozinhas. Uma vez por rodada, quando uma invocação em campo realizar um ataque "
            "contra um alvo dentro do seu alcance, você pode pagar 2PE para, como uma Ação Livre, "
            "realizar um ataque contra o mesmo alvo. Além disso, para cada invocação que possua "
            "em campo, você recebe +1 em acerto e dano, com elas te auxiliando."
        ),
    },
]

# ─── ESTILOS DE COMBATE (Repertório do Especialista) ──────────────────────────
ESTILOS_COMBATE = {
    "defensivo": {
        "nome": "Estilo Defensivo",
        "desc": "Foca em aprimorar a defesa. Defesa +2 no 1° nível, +1 nos níveis 4, 8, 12 e 16.",
        "efeito_nivel1": "Defesa +2",
        "progressao": "Defesa +1 nos níveis 4, 8, 12 e 16.",
    },
    "arremessador": {
        "nome": "Estilo do Arremessador",
        "desc": "Especializado em armas de arremesso. Pode sacar uma arma de arremesso como parte do ataque. +2 em rolagens de dano com armas de arremesso.",
        "efeito_nivel1": "Sacar arma de arremesso como parte do ataque; +2 dano com arremesso",
        "progressao": "Bônus de dano +1 nos níveis 4, 8, 12 e 16.",
    },
    "duelista": {
        "nome": "Estilo do Duelista",
        "desc": "Duelo com uma única arma enquanto a outra mão está livre. +1 em acerto e +2 em dano.",
        "efeito_nivel1": "+1 acerto, +2 dano (1 arma + mão livre)",
        "progressao": "Dano +1 nos níveis 4, 8, 12, 16; Acerto +1 nos níveis 8 e 16.",
    },
    "interceptador": {
        "nome": "Estilo do Interceptador",
        "desc": "Usa armas para interceptar ataques em aliados. Reação: reduz dano de aliado em 1d10 + modificador (FOR/DES/SAB).",
        "efeito_nivel1": "Reação: reduz dano de aliado em 1d10 + mod",
        "progressao": "+1 dado de redução nos níveis 4, 8, 12 e 16.",
    },
    "protetor": {
        "nome": "Estilo do Protetor",
        "desc": "Protege aliados a 1,5m. Reação: impõe desvantagem em ataque contra aliado adjacente. Pode conceder vantagem em TR de aliado a 1,5m.",
        "efeito_nivel1": "Reação: desvantagem em ataques contra aliados a 1,5m; vantagem em TR de aliado",
        "progressao": "Sem escalamento de nível.",
    },
    "distante": {
        "nome": "Estilo Distante",
        "desc": "Especializado em armas a distância. +1 em acerto e +2 em dano com armas a distância.",
        "efeito_nivel1": "+1 acerto, +2 dano (armas a distância)",
        "progressao": "Dano +1 nos níveis 4, 8, 12, 16; Acerto +1 nos níveis 8 e 16.",
    },
    "duplo": {
        "nome": "Estilo Duplo",
        "desc": "Manejar duas armas. Adiciona o bônus de atributo no dano da segunda arma, +1 dano adicional.",
        "efeito_nivel1": "+bônus de atributo no dano da 2ª arma; +1 dano",
        "progressao": "Dano +1 nos níveis 4, 8, 12 e 16.",
    },
    "massivo": {
        "nome": "Estilo Massivo",
        "desc": "Domínio de armas pesadas. Relança dados que resultam 1 ou 2 em armas de 2 mãos/pesadas. +1 dano.",
        "efeito_nivel1": "Relança 1s e 2s em armas de 2 mãos/pesadas; +1 dano",
        "progressao": "Dano +1 nos níveis 4, 8, 12 e 16.",
    },
}


# ─── TABELAS DE NÍVEL POR ESPECIALIZAÇÃO ──────────────────────────────────────
# Ganhos automáticos (além de: +1 Habilidade de Espec., +1 Aptidão por nível exceto restringido)
# Níveis 4,8,12,16,20 → +2 Pontos de Atributo | Níveis 5,9,13,17 → BT+1 | Nível 10 → Mestre em Perícia

TABELAS_NIVEIS = {
    "lutador": {
        1:  ["Corpo Treinado", "Empolgação"],
        2:  ["Reflexo Evasivo"],
        3:  [],
        4:  ["Implemento Marcial", "+2 Pontos de Atributo"],
        5:  ["Gosto pela Luta", "BT +1"],
        6:  [],
        7:  [],
        8:  ["+2 Pontos de Atributo"],
        9:  ["Teste de Resistência Mestre", "BT +1"],
        10: ["Mestre em uma Perícia"],
        11: ["Empolgação Máxima"],
        12: ["+2 Pontos de Atributo"],
        13: ["BT +1"],
        14: [],
        15: [],
        16: ["+2 Pontos de Atributo"],
        17: ["BT +1"],
        18: [],
        19: [],
        20: ["Lutador Superior", "+2 Pontos de Atributo"],
    },
    "especialista_combate": {
        1:  ["Repertório do Especialista (Estilo de Combate)", "Artes do Combate"],
        2:  [],
        3:  [],
        4:  ["Golpe Especial", "Implemento Marcial", "+2 Pontos de Atributo"],
        5:  ["BT +1"],
        6:  ["Renovação pelo Sangue", "+2° Estilo de Combate"],
        7:  [],
        8:  ["+2 Pontos de Atributo"],
        9:  ["Teste de Resistência Mestre", "BT +1"],
        10: ["Mestre em uma Perícia"],
        11: [],
        12: ["+2 Pontos de Atributo", "+3° Estilo de Combate"],
        13: ["BT +1"],
        14: [],
        15: [],
        16: ["+2 Pontos de Atributo"],
        17: ["BT +1"],
        18: [],
        19: [],
        20: ["Autossuficiente", "+2 Pontos de Atributo"],
    },
    "especialista_tecnica": {
        1:  ["Domínio dos Fundamentos (2 Mudanças)", "Conjuração Aprimorada"],
        2:  [],
        3:  [],
        4:  ["Adiantar a Evolução", "+2 Pontos de Atributo"],
        5:  ["BT +1"],
        6:  [],
        7:  [],
        8:  ["+2 Pontos de Atributo"],
        9:  ["Teste de Resistência Mestre", "BT +1"],
        10: ["Foco Amaldiçoado", "Mestre em uma Perícia"],
        11: [],
        12: ["+2 Pontos de Atributo", "Mudança de Fundamento adicional"],
        13: ["BT +1"],
        14: [],
        15: [],
        16: ["+2 Pontos de Atributo"],
        17: ["BT +1"],
        18: [],
        19: [],
        20: ["O Honrado", "+2 Pontos de Atributo"],
    },
    "controlador": {
        1:  ["Treinamento em Controle (2 Invocações iniciais)"],
        2:  [],
        3:  ["+1 Invocação"],
        4:  ["Controle Aprimorado", "+2 Pontos de Atributo"],
        5:  ["BT +1"],
        6:  ["Apogeu (Estilo de Controle)", "+1 Invocação", "+Comandos por Ação"],
        7:  [],
        8:  ["+2 Pontos de Atributo"],
        9:  ["Treinamento em Controle: +1 Invocação", "Teste de Resistência Mestre", "BT +1"],
        10: ["Reserva para Invocação", "+1 Invocação", "Mestre em uma Perícia"],
        11: [],
        12: ["+2 Pontos de Atributo", "+1 Invocação", "+Comandos por Ação"],
        13: ["BT +1"],
        14: [],
        15: ["+1 Invocação"],
        16: ["+2 Pontos de Atributo"],
        17: ["BT +1"],
        18: ["+1 Invocação", "+Comandos por Ação"],
        19: [],
        20: ["Ápice do Controle", "+2 Pontos de Atributo"],
    },
    "suporte": {
        1:  ["Suporte em Combate"],
        2:  [],
        3:  ["Presença Inspiradora"],
        4:  ["+2 Pontos de Atributo"],
        5:  ["Versatilidade", "BT +1"],
        6:  ["Aptidão: Energia Reversa (automático)"],
        7:  [],
        8:  ["+2 Pontos de Atributo", "Aptidão: Liberação de Energia Reversa (automático)"],
        9:  ["Teste de Resistência Mestre", "BT +1"],
        10: ["Medicina Infalível", "Mestre em uma Perícia"],
        11: [],
        12: ["+2 Pontos de Atributo"],
        13: ["BT +1"],
        14: [],
        15: [],
        16: ["+2 Pontos de Atributo"],
        17: ["BT +1"],
        18: [],
        19: [],
        20: ["Suporte Absoluto", "+2 Pontos de Atributo"],
    },
    "restringido": {
        1:  ["Restrito pelos Céus (Ferramenta Grau 4, Pontos de Estamina, Estilo Marcial)"],
        2:  ["Ataque Furtivo 1d8", "Versatilidade (+1 perícias)"],
        3:  ["Esquiva Sobre-humana (+1 DEF/Reflexos)", "Ataque Furtivo 2d8"],
        4:  ["Implemento Celeste", "Dádiva do Céu", "+2 Pontos de Atributo"],
        5:  ["BT +1"],
        6:  ["Ataque Furtivo 3d8"],
        7:  [],
        8:  ["+2 Pontos de Atributo", "Dádiva do Céu"],
        9:  ["Ataque Furtivo 4d8", "Esquiva Sobre-humana (+2)", "Teste de Resistência Mestre", "BT +1"],
        10: ["Restrição Definitiva", "Versatilidade (+2 perícias)", "Mestre em uma Perícia"],
        11: [],
        12: ["Ataque Furtivo 5d8", "+2 Pontos de Atributo", "Dádiva do Céu"],
        13: ["BT +1"],
        14: [],
        15: ["Ataque Furtivo 6d8"],
        16: ["Esquiva Sobre-humana (+3)", "+2 Pontos de Atributo", "Dádiva do Céu"],
        17: ["BT +1"],
        18: [],
        19: [],
        20: ["Libertação do Destino", "+2 Pontos de Atributo", "Dádiva do Céu"],
    },
}


def get_ganhos_nivel(spec_key, nivel):
    """Retorna lista de strings com tudo que se ganha ao atingir `nivel`."""
    tabela = TABELAS_NIVEIS.get(spec_key, {})
    ganhos = list(tabela.get(nivel, []))

    # Habilidade de especialização (escolha livre) em todo nível > 1
    if nivel > 1:
        nomes_spec = {
            "lutador": "Habilidade de Lutador",
            "especialista_combate": "Habilidade de Especialista em Combate",
            "especialista_tecnica": "Habilidade de Especialista em Técnica",
            "controlador": "Habilidade de Controlador",
            "suporte": "Habilidade de Suporte",
            "restringido": "Habilidade de Restringido",
        }
        ganhos.append(nomes_spec.get(spec_key, "Habilidade de Especialização") + " (escolha)")

    # Aptidão amaldiçoada em todo nível (exceto restringido)
    if spec_key != "restringido":
        ganhos.append("Aptidão Amaldiçoada (escolha)")

    return ganhos


def get_habilidades_catalogadas(spec_key):
    """Returns list of {id, nivel, nome, desc} for all choosable habilidades of a spec."""
    spec = ESPECIALIZACOES.get(spec_key, {})
    result = []
    catalogo = spec.get("habilidades_catalogo")
    if catalogo:
        for item in catalogo:
            nome = item["nome"]
            hab_id = ''.join(c if c.isalnum() else '_' for c in nome.lower().replace(" ", "_"))
            result.append({"id": hab_id, "nivel": item["nivel"], "nome": nome, "desc": item.get("desc", ""), "req": item.get("req", "")})
        return result
    for nivel_num, lista in sorted(spec.get("habilidades_nivel", {}).items()):
        for item in lista:
            if "–" in item:
                partes = item.split("–", 1)
                nome = partes[0].strip()
                desc = partes[1].strip()
            else:
                nome = item.strip()
                desc = ""
            hab_id = ''.join(c if c.isalnum() else '_' for c in nome.lower().replace(" ", "_"))
            result.append({"id": hab_id, "nivel": nivel_num, "nome": nome, "desc": desc})
    return result


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
    {
        "key": "comum",
        "nome": "Uniforme Comum",
        "desc": "O uniforme padrão de feiticeiro, sem modificações adicionais.",
        "bonus_defesa": 0,
        "penalidade": 0,
        "custo": 0,
        "bonus_especial": None,
    },
    {
        "key": "leve",
        "nome": "Revestimento Leve",
        "desc": "Um revestimento leve é colocado no uniforme, concedendo um leve reforço defensivo.",
        "bonus_defesa": 2,
        "penalidade": 0,
        "custo": 1,
        "bonus_especial": None,
    },
    {
        "key": "medio",
        "nome": "Revestimento Médio",
        "desc": "Placas e camadas adicionais dão uma proteção maior, mas com peso considerável.",
        "bonus_defesa": 4,
        "penalidade": -2,
        "custo": 2,
        "bonus_especial": None,
    },
    {
        "key": "robusto",
        "nome": "Revestimento Robusto",
        "desc": "Placas fortes e camadas densas que se assemelham a armaduras ou coletes.",
        "bonus_defesa": 6,
        "penalidade": -4,
        "custo": 3,
        "bonus_especial": None,
    },
    {
        "key": "sob_medida",
        "nome": "Sob Medida",
        "desc": "Feito sob medida para o feiticeiro, encaixando-se perfeitamente e destacando sua agilidade.",
        "bonus_defesa": 1,
        "penalidade": 0,
        "custo": 2,
        "bonus_especial": "+2 em testes de Acrobacia e Furtividade",
    },
]

KITS = {
    "Ferramentas de Alfaiate": {
        "oficio": "Alfaiate",
        "icone": "🧵",
        "tipo_item": "Acessórios e Uniformes",
        "desc_curta": "Cria acessórios especiais e uniformes com revestimentos usando habilidade manual e jujutsu.",
        "desc_longa": "O kit de ferramentas de alfaiate é focado na criação de acessórios especiais e uniformes, feitos sob medida com o uso de habilidade manual e jujutsu. Criar acessórios amaldiçoados é complexo e custoso. Do nível 1 ao 9, você só pode criar 1 acessório por interlúdio; a partir do nível 10 você pode criar 2 acessórios por interlúdio. Você pode criar um uniforme com revestimento por interlúdio.",
        "capacidades": [
            "Criar 1 acessório especial por interlúdio (nível 1–9) ou 2 (nível 10+)",
            "Criar um uniforme com revestimento por interlúdio",
            "Testes que envolvam o kit usam Ofício (Alfaiate)",
        ],
        "itens_criados": ["Acessórios amaldiçoados (Custo 1–4)", "Uniformes com revestimento"],
    },
    "Ferramentas de Alquimia": {
        "oficio": "Alquimia",
        "icone": "⚗️",
        "tipo_item": "Mistura",
        "desc_curta": "Mistura elementos e substâncias para criar venenos, óleos e misturas com efeitos especiais.",
        "desc_longa": "O kit de ferramentas de alquimia possibilita misturar elementos e substâncias para criar algo novo, podendo ser tanto venenos quanto misturas com efeitos diferenciados. Possuir treinamento em ferramentas de alquimia permite criar itens especiais do tipo Mistura; não há um limite de quantas misturas podem ser criadas por interlúdio.",
        "capacidades": [
            "Criar itens especiais do tipo Mistura (venenos, óleos, substâncias)",
            "Sem limite de Misturas criadas por interlúdio",
            "Venenos funcionam por Contato, Inalação ou Ingestão",
            "Testes que envolvam o kit usam Ofício (Alquimia)",
        ],
        "itens_criados": ["Veneno Debilitante", "Veneno Intenso", "Veneno Desnorteante", "Veneno Maldito", "Lágrima de Shinigami", "Óleo Amolador", "Óleo Flamejante", "Mistura Profana"],
    },
    "Ferramentas de Canalizador": {
        "oficio": "Canalizador",
        "icone": "🔮",
        "tipo_item": "Espiritual",
        "desc_curta": "Amuletos e pérolas que canalizam energia amaldiçoada e espíritos em itens espirituais.",
        "desc_longa": "O kit de ferramentas de canalizador é um conjunto de peculiares amuletos, pérolas e outros itens espirituais, que permitem canalizar energia amaldiçoada e alguns espíritos amaldiçoados menores em itens. Possuir treinamento em ferramentas de canalizador permite criar itens especiais do tipo Espiritual; não há um limite de quantos itens espirituais podem ser criados por interlúdio.",
        "capacidades": [
            "Criar itens especiais do tipo Espiritual",
            "Sem limite de itens Espirituais criados por interlúdio",
            "Canaliza espíritos amaldiçoados menores em itens funcionais",
            "Testes que envolvam o kit usam Ofício (Canalizador)",
        ],
        "itens_criados": ["Pérola Carregada", "Conjunto de Pérolas Carregadas", "Terço de Pérolas Carregadas", "Elixir da Vida"],
    },
    "Ferramentas de Cozinheiro": {
        "oficio": "Cozinheiro",
        "icone": "🍳",
        "tipo_item": "Refeições Especiais",
        "desc_curta": "Prepara refeições com propriedades especiais que conferem benefícios mecânicos a quem come.",
        "desc_longa": "O kit de ferramentas de cozinheiro dá a capacidade de extrair ao máximo habilidades culinárias, criando refeições de alta qualidade que conferem benefícios. Durante um descanso, um personagem treinado pode preparar uma refeição especial (teste de Ofício Cozinheiro CD 15, +5 por benefício adicional). Falhar implica que a comida foi estragada. Os benefícios duram até o próximo descanso longo e uma mesma refeição beneficia criaturas igual ao bônus de treinamento do cozinheiro.",
        "capacidades": [
            "Preparar refeição especial durante um descanso (CD 15, +5 por benefício extra)",
            "Beneficia criaturas igual ao bônus de treinamento do cozinheiro",
            "Refeição Energética: concede PE temporária igual ao BT",
            "Refeição Leve: +Deslocamento (3m por grau do cozinheiro)",
            "Refeição Nutritiva: +2 em TRs (metade do BT)",
            "Refeição Picante: +2 em jogadas de ataque",
            "Refeição Reforçada: +2 na Defesa",
            "Refeição Refrescante: vantagem em um teste à escolha",
            "Refeição Revigorante: +5 PV temporários por grau do cozinheiro",
        ],
        "itens_criados": ["Refeições com efeitos especiais (7 tipos disponíveis)"],
    },
    "Ferramentas de Entalhador": {
        "oficio": "Entalhador",
        "icone": "🪵",
        "tipo_item": "Talismã",
        "desc_curta": "Entalha símbolos amaldiçoados em madeira para criar talismãs com efeitos poderosos.",
        "desc_longa": "O kit de ferramentas de entalhador junta instrumentos e utensílios utilizados na arte de se entalhar e encravar, a qual quando unida à energia amaldiçoada permite criar amuletos e talismãs. Possuir treinamento em ferramentas de entalhador permite criar itens especiais do tipo Talismã; não há um limite de quantos talismãs podem ser criados por interlúdio. Por padrão, um talismã ocupa o espaço de uma mão para ser usado.",
        "capacidades": [
            "Criar itens especiais do tipo Talismã",
            "Sem limite de Talismãs criados por interlúdio",
            "Talismãs concedem efeitos temporários, imediatos ou duradouros",
            "Talismã ocupa o espaço de uma mão para ser usado",
            "Testes que envolvam o kit usam Ofício (Entalhador)",
        ],
        "itens_criados": ["Símbolo da Vida", "Símbolo da Vida Florescente", "Símbolo da Vida Absoluta", "Talismã de Barreira", "Talismã de Barreira Superior", "Domínio Simples Contido", "Talismã do Ápice"],
    },
    "Ferramentas de Ferreiro": {
        "oficio": "Ferreiro",
        "icone": "⚒️",
        "tipo_item": "Armas e Escudos Amaldiçoados",
        "desc_curta": "Forja e melhora armas e escudos, incluindo ferramentas amaldiçoadas. Essencial para manter equipamentos em campo.",
        "desc_longa": "O kit de ferramentas de ferreiro é utilizado na criação e melhoria de armas e escudos, eventualmente utilizando do jujutsu para transformá-los em ferramentas amaldiçoadas. Possuir treinamento nas ferramentas de ferreiro permite criar tanto armas e escudos comuns quanto ferramentas amaldiçoadas. É o principal kit para manter equipamentos em bom estado e otimizá-los ao máximo.",
        "capacidades": [
            "Criar armas e escudos comuns e ferramentas amaldiçoadas",
            "Descanso curto: melhora temporariamente metade do BT em equipamentos",
            "Descanso longo: melhora BT completo de equipamentos",
            "Arma melhorada: +2 em jogadas de ataque realizadas com ela",
            "Escudo melhorado: +metade do BT na RD concedida enquanto empunhado",
            "Melhorias temporárias duram até o próximo descanso",
            "Testes que envolvam o kit usam Ofício (Ferreiro)",
        ],
        "itens_criados": ["Armas comuns e amaldiçoadas", "Escudos comuns e amaldiçoados"],
    },
    "Ferramentas de Farmacêutico": {
        "oficio": "Farmacêutico",
        "icone": "💊",
        "tipo_item": "Fármacos",
        "desc_curta": "Sintetiza fármacos, antídotos, remédios e injeções a partir de substâncias medicinais refinadas.",
        "desc_longa": "O kit de ferramentas de farmacêutico permite cuidar efetivamente da saúde, além de sintetizar substâncias medicinais refinadas, criando antídotos ou remédios. Possuir treinamento nas ferramentas de farmacêutico permite criar itens especiais do tipo Fármacos; não há um limite de quantas medicinas podem ser criadas por interlúdio.",
        "capacidades": [
            "Criar itens especiais do tipo Fármaco",
            "Sem limite de Fármacos criados por interlúdio",
            "Cria antídotos, remédios, injeções e mixes energéticos",
            "Testes que envolvam o kit usam Ofício (Farmacêutico)",
        ],
        "itens_criados": ["Antídoto Simples/Intermediário/Superior/Absoluto", "Remédio Simples/Intermediário/Complexo", "Injeção Estimulante", "Injeção de Adrenalina", "Mix Energético Pequeno/Médio/Grande"],
    },
}

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


# Treinamento em Controle: 2 iniciais + 1 nos níveis 3, 6, 9, 10, 12, 15, 18
_INVOCACOES_GANHOS = [3, 6, 9, 10, 12, 15, 18]

def get_max_invocacoes(nivel):
    """Retorna o número máximo de invocações que um Controlador pode ter cadastradas."""
    return 2 + sum(1 for n in _INVOCACOES_GANHOS if nivel >= n)


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
# Organizadas conforme o livro (Cap. 8)

# p.174 — Aptidão de Aura
APTIDOES_AURA = [
    # nivel_req = Nível de Aptidão em Aura (AU) exigido, de 0 a 5
    # req_nivel = nível de personagem mínimo
    # req_atributos = {attr: valor} — TODOS devem ser atingidos
    # req_atributos_ou = [{attr: valor}, ...] — UM basta
    # req_pericias = [{"nome": str, "nivel": "treinado"|"mestre"}] — TODAS
    # req_apt_nivel = {cat_id: nivel} — nível de aptidão em outra categoria
    {
        "id": "afinidade_ampliada", "nivel_req": 0, "req": [],
        "nome": "Afinidade Ampliada",
        "descricao": "Sua aura tem maior afinidade com um tipo de dano elemental escolhido. Sempre que infligir dano desse tipo, causa dano adicional igual a 1 + Nível de Aptidão em Aura.",
    },
    {
        "id": "aura_anuladora", "nivel_req": 0, "req": [],
        "nome": "Aura Anuladora",
        "descricao": "Uma quantidade de vezes igual ao bônus de treinamento, ao sofrer uma condição, pague PE para ignorá-la: fraca 2PE, média 4PE, forte 6PE, extrema 10PE. Recupera usos em descanso longo.",
    },
    {
        "id": "aura_chamativa", "nivel_req": 0, "req": [],
        "req_nivel": 6, "req_atributos": {"presenca": 18},
        "nome": "Aura Chamativa",
        "descricao": "Criaturas não aliadas que comecem o turno a 4,5m devem passar em TR de Vontade ou ficam Enfeitiçadas, repetindo o teste no próximo turno. Cada falha concede +2 para resistir. [Pré-Requisito: Presença 18 e Nível 6]",
    },
    {
        "id": "aura_controlada", "nivel_req": 0, "req": [],
        "req_atributos": {"destreza": 16},
        "req_pericias": [{"nome": "Furtividade", "nivel": "treinado"}],
        "nome": "Aura Controlada",
        "descricao": "Soma metade do Nível de Aptidão em Aura em testes de Furtividade. Gastando 1PE, soma o nível completo. [Pré-Requisito: Treinado em Furtividade e Destreza 16]",
    },
    {
        "id": "aura_contencao", "nivel_req": 0, "req": [],
        "req_atributos_ou": [{"forca": 16}, {"constituicao": 16}],
        "nome": "Aura de Contenção",
        "descricao": "Adiciona metade do Nível de Aptidão em Aura em Atletismo para agarrar. Metade do nível de aptidão vezes por cena: gaste 1PE para vantagem ao agarrar ou desvantagem na fuga do alvo. [Pré-Requisito: Força ou Constituição 16]",
    },
    {
        "id": "aura_bastiao", "nivel_req": 0, "req": [],
        "nome": "Aura do Bastião",
        "descricao": "Todo aliado dentro de 4,5m recebe bônus na Defesa igual ao Nível de Aptidão em Aura.",
    },
    {
        "id": "aura_comandante", "nivel_req": 0, "req": [],
        "req_nivel": 8, "req_atributos": {"presenca": 16},
        "nome": "Aura do Comandante",
        "descricao": "Ação Bônus: expanda aura para cobrir aliados a 4,5m, concedendo 1 + metade do Nível de Aptidão em Aura em rolagens de dano e testes de perícia no combate. Custo: 2PE por rodada. [Pré-Requisito: Presença 16 e Nível 8]",
    },
    {
        "id": "aura_comandante_evoluida", "nivel_req": 0, "req": ["aura_comandante"],
        "req_nivel": 12,
        "nome": "Aura do Comandante Evoluída",
        "descricao": "Ao usar Aura do Comandante, some o Nível de Aptidão total (ao invés de 1 + metade) e conceda +2 em jogadas de ataque e TRs. Custo passa de 2 para 4PE. [Pré-Requisito: Aura do Comandante e Nível 12]",
    },
    {
        "id": "aura_drenadora", "nivel_req": 2, "req": [],
        "req_nivel": 6,
        "nome": "Aura Drenadora",
        "descricao": "Ao matar um inimigo, receba PV temporários igual a Xd8 + mod Constituição (X = Nível de Aptidão em Aura). Acumulam. [Pré-Requisito: Nível de Aptidão em Aura 2 e Nível 6]",
    },
    {
        "id": "aura_elemental", "nivel_req": 0, "req": [],
        "req_nivel": 6,
        "nome": "Aura Elemental",
        "descricao": "Converta o tipo de dano dos seus ataques para um elemento escolhido, causando 1d4 extra (AU 2 → 1d6, AU 3 → 1d8, AU 5 → 1d10). Pode desativar como ação livre em combate. [Pré-Requisito: Nível 6]",
    },
    {
        "id": "aura_elemental_reforcada", "nivel_req": 0, "req": ["aura_elemental", "aura_reforcada"],
        "nome": "Aura Elemental Reforçada",
        "descricao": "Receba RD ao tipo de dano da sua aura elemental igual à redução de Aura Reforçada + Nível de Aptidão em Aura. [Pré-Requisito: Aura Elemental e Aura Reforçada]",
    },
    {
        "id": "absorcao_elemental", "nivel_req": 0, "req": ["aura_elemental"],
        "nome": "Absorção Elemental",
        "descricao": "Reação ao receber dano elemental: absorva e libere no próximo ataque como Xd6 extra do mesmo tipo (X = AU; AU 3 → d8; AU 5 → d10). Não cumulativo. [Pré-Requisito: Aura Elemental]",
    },
    {
        "id": "aura_embacada", "nivel_req": 0, "req": [],
        "req_nivel": 6,
        "nome": "Aura Embaçada",
        "descricao": "Ação Bônus (2PE, +2PE/rodada para manter): todo ataque corpo a corpo ou a distância tem 20% de chance de falhar (1 ou 2 em 1d10). [Pré-Requisito: Nível 6]",
    },
    {
        "id": "aura_inofensiva", "nivel_req": 0, "req": [],
        "req_atributos": {"presenca": 16},
        "nome": "Aura Inofensiva",
        "descricao": "Ao iniciar combate, role Feitiçaria contra a Atenção dos inimigos. Fique automaticamente escondido de todos cuja Atenção seja superada pelo resultado do teste. [Pré-Requisito: Presença 16]",
    },
    {
        "id": "casulo_energia", "nivel_req": 5, "req": ["aura_impenetravel"],
        "req_nivel": 16,
        "nome": "Casulo de Energia",
        "descricao": "Ação Comum (6PE, 1 rodada): imunidade a dano cortante, perfurante e impacto de fontes mundanas. Contra técnicas, receba RD adicional igual ao dobro do Nível de Aptidão em Aura. [Pré-Requisito: Aura Impenetrável, Nível de Aptidão em Aura 5 e Nível 16]",
    },
    {
        "id": "enganacao_projetada", "nivel_req": 0, "req": [],
        "req_nivel": 4, "req_atributos": {"destreza": 18},
        "req_pericias": [{"nome": "Enganação", "nivel": "treinado"}],
        "nome": "Enganação Projetada",
        "descricao": "Ao atacar, o alvo deve passar em TR de Astúcia ou você tem vantagem nesse ataque. Para cada ataque após o primeiro no mesmo turno, pague 1PE. [Pré-Requisito: Treinado em Enganação, Destreza 18 e Nível 4]",
    },
    {
        "id": "golpe_com_aura", "nivel_req": 0, "req": [],
        "nome": "Golpe com Aura",
        "descricao": "Gaste 1PE para imbuir um golpe com uma aptidão de aura que force TR: a CD aumenta em Nível de Aptidão em Aura. Para aptidões de dano, o dano é aplicado após o ataque. Não funciona em Feitiços.",
    },
    {
        "id": "concentrar_aura", "nivel_req": 0, "req": [],
        "nome": "Concentrar Aura",
        "descricao": "Ação livre: desabilite aptidões de aura passivas por 1 rodada (até 1 + AU). Para cada desabilitada, ao acertar ataque desarmado ou com arma, o alvo recebe 1d8 de dano energético. Não se aplica em Feitiços.",
    },
    {
        "id": "transferencia_aura", "nivel_req": 0, "req": [],
        "nome": "Transferência de Aura",
        "descricao": "Ação Bônus (2PE): transfira uma Aptidão de Aura específica para criatura a 9m por 1 rodada. Mantenha por rodadas adicionais pagando 1PE cada.",
    },
    {
        "id": "aura_excessiva", "nivel_req": 0, "req": ["aura_reforcada"],
        "req_nivel": 8, "req_atributos": {"constituicao": 16},
        "nome": "Aura Excessiva",
        "descricao": "No início de cada rodada, pague 2PE para receber RD contra todos os tipos de dano (exceto na alma) igual à redução fornecida por Aura Reforçada. [Pré-Requisito: Aura Reforçada, Constituição 16 e Nível 8]",
    },
    {
        "id": "aura_lacerante", "nivel_req": 0, "req": [],
        "nome": "Aura Lacerante",
        "descricao": "Ação livre para ativar por 1 rodada. Criaturas que iniciem o turno a 3m devem passar em TR de Fortitude ou recebem Xd6 + mod atributo principal de dano energético (X = AU; AU 3 → d8; AU 5 → d10).",
    },
    {
        "id": "aura_macabra", "nivel_req": 0, "req": [],
        "nome": "Aura Macabra",
        "descricao": "Criaturas agressivas a 1,5m devem passar em TR de Vontade ou ficam Abaladas. Gaste 1PE para expandir para 4,5m por 1 rodada. AU 3: inflige Amedrontado ao invés de Abalado.",
    },
    {
        "id": "aura_macica", "nivel_req": 0, "req": [],
        "req_atributos": {"constituicao": 16},
        "nome": "Aura Maciça",
        "descricao": "Sua Defesa aumenta em valor igual ao Nível de Aptidão em Aura. [Pré-Requisito: Constituição 16]",
    },
    {
        "id": "aura_movedicca", "nivel_req": 0, "req": [],
        "nome": "Aura Movediça",
        "descricao": "Todo quadrado adjacente a você se torna terreno difícil. AU 2 → 3m; AU 4 → 4,5m; AU 5 → 6m. Não pode ser aumentada por Expandir Aura.",
    },
    {
        "id": "aura_redirecionadora", "nivel_req": 0, "req": [],
        "req_atributos": {"destreza": 16},
        "nome": "Aura Redirecionadora",
        "descricao": "Gaste 2PE ao imbuir projétil ou arma de arremesso: se errar, redirecione para criatura a 6m do alvo original com bônus de +1 + metade do AU para acertar. [Pré-Requisito: Destreza 16]",
    },
    {
        "id": "aura_reforcada", "nivel_req": 0, "req": [],
        "nome": "Aura Reforçada",
        "descricao": "Receba redução contra danos físicos (cortes, perfurações e impactos) igual ao dobro do Nível de Aptidão em Aura.",
    },
    {
        "id": "aura_impenetravel", "nivel_req": 3, "req": ["aura_reforcada"],
        "req_nivel": 10,
        "nome": "Aura Impenetrável",
        "descricao": "Ação Bônus (3PE, 1 rodada): resistência a dano cortante, perfurante e impacto. [Pré-Requisito: Aura Reforçada, Nível de Aptidão em Aura 3 e Nível 10]",
    },
]

# p.178 — Controle e Leitura
APTIDOES_CONTROLE_LEITURA = [
    # nivel_req = Nível de Aptidão em Controle e Leitura (CL) exigido, de 0 a 5
    {
        "id": "canalizar_em_golpe", "nivel_req": 0, "req": [],
        "nome": "Canalizar em Golpe",
        "descricao": "Ação de Movimento: gaste PE igual ao Nível de Aptidão em Controle e Leitura. Cada PE gasto adiciona 1d6 no próximo ataque. Não funciona em Feitiços. Errar não consome o uso.",
    },
    {
        "id": "cobrir_se", "nivel_req": 0, "req": [],
        "nome": "Cobrir-se",
        "descricao": "Reação ao receber dano: gaste 2 + (2 × CL) PE para receber 4PV temporários por PE gasto, até o final do turno da criatura atacante.",
    },
    {
        "id": "canalizacao_avancada", "nivel_req": 2, "req": ["canalizar_em_golpe"],
        "req_nivel": 8,
        "nome": "Canalização Avançada",
        "descricao": "Canalizar em Golpe pode ser feito como reação ao realizar um ataque, e o bônus por ponto passa de 1d6 para 1d8. [Pré-Requisito: Canalizar em Golpe, Nível de Aptidão em Controle e Leitura 2 e Nível 8]",
    },
    {
        "id": "cobertura_avancada", "nivel_req": 2, "req": ["cobrir_se"],
        "req_nivel": 10,
        "nome": "Cobertura Avançada",
        "descricao": "Ao usar Cobrir-se, cada PE gasto concede 8PV temporários (ao invés de 4). [Pré-Requisito: Cobrir-se, Nível de Aptidão em Controle e Leitura 2 e Nível 10]",
    },
    {
        "id": "canalizacao_maxima", "nivel_req": 4, "req": ["canalizacao_avancada"],
        "req_nivel": 16,
        "nome": "Canalização Máxima",
        "descricao": "Gaste 1PE adicional: bônus por ponto aumenta de 1d8 para 1d10, somando também o Nível de Aptidão em Aura ao total. [Pré-Requisito: Canalização Avançada, Nível de Aptidão em Controle e Leitura 4 e Nível 16]",
    },
    {
        "id": "estimulo_muscular", "nivel_req": 0, "req": [],
        "nome": "Estímulo Muscular",
        "descricao": "Ao agir (movimento/Acrobacia/Atletismo), use PE para estímulos (cada um uma vez por rodada): +deslocamento (1PE = +metade do deslocamento), +bônus em teste (1PE por CL = +1 por PE), arremessar/empurrar mais longe (2PE = CL × 1,5m), dobrar salto (1PE).",
    },
    {
        "id": "estimulo_muscular_avancado", "nivel_req": 3, "req": ["estimulo_muscular"],
        "req_nivel": 4,
        "nome": "Estímulo Muscular Avançado",
        "descricao": "Cada estímulo pode ser usado duas vezes por rodada: deslocamento dobrado (2PE), +2 por PE nos testes, distância de empurrar/arremessar = CL × 3m. [Pré-Requisito: Estímulo Muscular, Nível de Aptidão em Controle e Leitura 3 e Nível 4]",
    },
    {
        "id": "expandir_aura", "nivel_req": 0, "req": [],
        "req_nivel": 6,
        "nome": "Expandir Aura",
        "descricao": "Ação livre (2PE): dobre o alcance de todas as aptidões de aura passivas por 1 rodada. Cada rodada adicional custa +1PE. [Pré-Requisito: Nível 6]",
    },
    {
        "id": "leitura_de_aura", "nivel_req": 0, "req": [],
        "nome": "Leitura de Aura",
        "descricao": "Ao ver criatura com aura amaldiçoada, role Feitiçaria (CD = CD Amaldiçoada). Em sucesso, descubra as propriedades passivas e ativas da aura.",
    },
    {
        "id": "leitura_rapida_energia", "nivel_req": 0, "req": [],
        "nome": "Leitura Rápida de Energia",
        "descricao": "Ação de Movimento: role Percepção contra CD Amaldiçoada (+CL bônus). Em sucesso, ignore desvantagens e aumentos de Defesa causados por aura do inimigo até o final da cena.",
    },
    {
        "id": "projetar_energia", "nivel_req": 0, "req": [],
        "nome": "Projetar Energia",
        "descricao": "Ação Comum: gaste 1 + CL PE. Cada PE gasto causa 1d10 de dano energético + mod maior atributo. Alcance: 9m + 1,5m × bônus de treinamento. Ataque amaldiçoado ou TR de Reflexos (nega).",
    },
    {
        "id": "projecao_avancada", "nivel_req": 2, "req": ["projetar_energia"],
        "req_nivel": 8,
        "nome": "Projeção Avançada",
        "descricao": "Dano por ponto passa para 2d8 + dobro do mod. +2 para acertar (ataque) ou +2 na CD (TR). [Pré-Requisito: Projetar Energia, Nível de Aptidão em Controle e Leitura 2 e Nível 8]",
    },
    {
        "id": "projecao_dividida", "nivel_req": 3, "req": ["projecao_avancada"],
        "req_nivel": 12,
        "nome": "Projeção Dividida",
        "descricao": "Ao disparar, pague até metade da energia para duplicar o projétil como parte da mesma ação. O duplicado mira criatura a 4,5m do original e segue o método de TR. [Pré-Requisito: Projeção Avançada, Nível de Aptidão em Controle e Leitura 3 e Nível 12]",
    },
    {
        "id": "projecao_maxima", "nivel_req": 4, "req": ["projecao_avancada"],
        "req_nivel": 16,
        "nome": "Projeção Máxima",
        "descricao": "Dano por ponto: 3d8. Bônus para acertar: +6; CD do TR: +4. Em sucesso no TR, dano reduzido à metade (ao invés de anulado). [Pré-Requisito: Projeção Avançada, Nível de Aptidão em Controle e Leitura 4 e Nível 16]",
    },
    {
        "id": "punho_divergente", "nivel_req": 0, "req": [],
        "nome": "Punho Divergente",
        "descricao": "Ao acertar ataque desarmado, cause metade do dano e guarde a outra metade para o turno seguinte. O alvo faz TR de Fortitude: em falha, recebe o dano guardado com vulnerabilidade. CD +1 para cada 5 pontos na primeira metade. Não funciona com raio negro.",
    },
    {
        "id": "emocao_petala_decadente", "nivel_req": 3, "req": ["cobrir_se"],
        "req_nivel": 5,
        "nome": "Emoção da Pétala Decadente",
        "descricao": "Reação a domínio sendo ativado ou Ação Bônus: enquanto ativo, gaste PE = nível de DOM do oponente para anular um acerto garantido físico de expansão de domínio. Efeito de Concentração. [Pré-Requisito: Nível 5, aprender de um dos Três Grandes Clãs (Zenin, Gojo ou Kamo), Cobrir-se e Nível de Aptidão em Controle e Leitura 3]",
    },
    {
        "id": "rastreio_avancado", "nivel_req": 0, "req": [],
        "nome": "Rastreio Avançado",
        "descricao": "Em cenas onde EA foi usada, detecte vestígios imediatamente. Caso já conheça a origem, descubra na hora. Caso não, role Investigação ou Percepção (CD Amaldiçoada) para identificar características e seguir o rastro.",
    },
]

# p.182 — Domínio
APTIDOES_DOMINIO = [
    # nivel_req = Nível de Aptidão em Domínio (DOM) exigido, de 0 a 5
    {
        "id": "revestimento_dominio", "nivel_req": 1, "req": [],
        "req_nivel": 10, "req_apt_nivel": {"controle_leitura": 3},
        "nome": "Revestimento de Domínio",
        "descricao": "Ação Bônus ou Reação (5PE, +5PE/turno para manter): reduza dano de técnicas ofensivas em valor igual ao nível de personagem (irredutível). Técnicas de nível ≤ metade do DOM são anuladas. Golpes também anulam efeitos passivos/sustentados de Feitiços anuláveis. [Pré-Requisito: CL 3, DOM 1 e Nível 10]",
    },
    {
        "id": "anular_tecnica", "nivel_req": 3, "req": ["dominio_simples"],
        "req_nivel": 8,
        "nome": "Anular Técnica",
        "descricao": "Reação ao ser alvo de Feitiço: gaste a mesma quantidade de PE e role Feitiçaria contra o conjurador. Em sucesso, o Feitiço é anulado (em área: nenhum afetado). Usos por descanso longo = DOM. [Pré-Requisito: Domínio Simples, DOM 3 e Nível 8]",
    },
    {
        "id": "expansao_incompleta", "nivel_req": 1, "req": [],
        "req_nivel": 8,
        "nome": "Expansão de Domínio Incompleta",
        "descricao": "Ação Comum (15PE, duas mãos livres): expanda domínio incompleto em raio 4,5m × bônus de treinamento. Dura 1 + DOM rodadas. Configure efeitos conforme Guia de Criação. [Pré-Requisito: DOM 1 e Nível 8]",
    },
    {
        "id": "expansao_completa", "nivel_req": 3, "req": ["expansao_incompleta", "tecnicas_barreira"],
        "req_nivel": 10, "req_apt_nivel": {"barreira": 3},
        "nome": "Expansão de Domínio Completa",
        "descricao": "Ação Comum (20PE, duas mãos livres): esfera de 9m. Dura 3 + DOM rodadas. Configure efeitos conforme Guia de Criação. [Pré-Requisito: Técnicas de Barreira, Expansão Incompleta, BAR 3, DOM 3 e Nível 10]",
    },
    {
        "id": "acerto_garantido", "nivel_req": 4, "req": ["expansao_completa"],
        "req_nivel": 14, "req_apt_nivel": {"barreira": 4},
        "req_pericias": [{"nome": "Feitiçaria", "nivel": "treinado"}],
        "nome": "Acerto Garantido",
        "descricao": "Adicione o efeito Acerto Garantido à sua expansão de domínio, imbuindo a técnica nas barreiras. Não conta para o máximo de efeitos. Aumenta o custo da expansão completa em +5PE. [Pré-Requisito: Expansão Completa, Treinamento em Feitiçaria, BAR 4, DOM 4 e Nível 14]",
    },
    {
        "id": "expansao_sem_barreiras", "nivel_req": 5, "req": ["acerto_garantido"],
        "req_nivel": 20, "req_apt_nivel": {"barreira": 5},
        "req_pericias": [{"nome": "Feitiçaria", "nivel": "mestre"}],
        "nome": "Expansão de Domínio Sem Barreiras",
        "descricao": "Mesmos efeitos e custo da expansão completa com acerto garantido, mas sem barreiras. Alcance superior para o acerto garantido; pode superar barreiras de outras expansões. [Pré-Requisito: Acerto Garantido, Mestre em Feitiçaria, BAR 5, DOM 5 e Nível 20]",
    },
]

# p.188 — Barreira
APTIDOES_BARREIRA = [
    # nivel_req = Nível de Aptidão em Barreira (BAR) exigido, de 0 a 5
    {
        "id": "tecnicas_barreira", "nivel_req": 1, "req": [],
        "nome": "Técnicas de Barreira",
        "descricao": "Ação Comum: crie até 6 paredes (1PE cada, em lugares desocupados a 3m). Cada parede tem 1,5m e PV = 5 + BAR × metade do nível de personagem. Use como obstáculo ou prisão. Manipular/mover é outra ação comum. [Pré-Requisito: BAR 1]",
    },
    {
        "id": "paredes_resistentes", "nivel_req": 2, "req": ["tecnicas_barreira"],
        "req_nivel": 4,
        "nome": "Paredes Resistentes",
        "descricao": "PV de cada parede passa a ser 10 + BAR × nível de personagem. [Pré-Requisito: Técnicas de Barreira, BAR 2 e Nível 4]",
    },
    {
        "id": "barreira_rapida", "nivel_req": 3, "req": ["tecnicas_barreira"],
        "req_nivel": 6,
        "nome": "Barreira Rápida",
        "descricao": "Erguer ou manipular barreiras se torna uma ação bônus. [Pré-Requisito: Técnicas de Barreira, BAR 3 e Nível 6]",
    },
    {
        "id": "cesta_oca_vime", "nivel_req": 1, "req": [],
        "req_nivel": 5,
        "nome": "Cesta Oca de Vime",
        "descricao": "Ação Bônus ou Reação (3PE): enquanto ativa, acerto garantido de domínios não te afeta. Concentração; Durabilidade = BAR + 1. Manter o selo (2 mãos) impede perda de durabilidade exceto por falha de concentração. [Pré-Requisito: Época adequada ou Mestre em História, BAR 1 e Nível 5]",
    },
    {
        "id": "cortina", "nivel_req": 0, "req": ["tecnicas_barreira"],
        "nome": "Cortina",
        "descricao": "Crie uma cortina que isola uma área (1PE por 9m cobertos, sem custo de manutenção). Não-feiticeiros veem o ambiente normal; feiticeiros veem o domo negro. Pode adicionar condições ao criar. PV padrão = soma de três paredes de Técnicas de Barreira. [Pré-Requisito: Técnicas de Barreira]",
    },
]

# p.189 — Energia Reversa
APTIDOES_ENERGIA_REVERSA = [
    # nivel_req = Nível de Aptidão em Energia Reversa (ER) exigido, de 0 a 5
    {
        "id": "energia_reversa", "nivel_req": 0, "req": [],
        "req_nivel": 8, "req_apt_nivel": {"controle_leitura": 3},
        "req_pericias": [{"nome": "Feitiçaria", "nivel": "treinado"}],
        "nome": "Energia Reversa",
        "descricao": "Produza energia reversa (PER; 1PER = 2PE). Cura: gaste PER para curar 2d6 + mod Presença ou Sabedoria (aumenta 1d6 nos níveis 10, 15 e 20). Máx por vez: 1 + metade do ER. Em combate é ação comum. Não cura outros. [Pré-Requisito: Treinado em Feitiçaria, CL 3 e Nível 8]",
    },
    {
        "id": "cura_amplificada", "nivel_req": 3, "req": ["energia_reversa"],
        "req_nivel": 12,
        "nome": "Cura Amplificada",
        "descricao": "Dado de cura passa para d8 e some o dobro do mod de Presença ou Sabedoria. Máximo de pontos gastos por vez: 1 + ER. [Pré-Requisito: Energia Reversa, ER 3 e Nível 12]",
    },
    {
        "id": "regeneracao_aprimorada", "nivel_req": 4, "req": ["cura_amplificada"],
        "req_nivel": 15,
        "nome": "Regeneração Aprimorada",
        "descricao": "Ação Comum (8PER por ferimento): regenere Ferimentos Complexos ou desmembramentos perdidos há menos de 1 dia. Com o membro em mãos: Ação Bônus (3PER). Gaste Ação Bônus + 4PER para remover veneno. ER 5: pague 10PER para usar como ação livre. [Pré-Requisito: Cura Amplificada, ER 4 e Nível 15]",
    },
    {
        "id": "fluxo_constante", "nivel_req": 3, "req": ["energia_reversa"],
        "req_nivel": 12,
        "nome": "Fluxo Constante",
        "descricao": "Mantenha cura contínua: no início do turno, cure-se com energia reversa como ação livre. Ou cure-se como reação ao ter a vida reduzida. [Pré-Requisito: Energia Reversa, ER 3 e Nível 12]",
    },
    {
        "id": "liberacao_energia_reversa", "nivel_req": 0, "req": ["energia_reversa"],
        "req_nivel": 10,
        "nome": "Liberação de Energia Reversa",
        "descricao": "Cure outras criaturas dentro do alcance de toque usando a habilidade Energia Reversa. [Pré-Requisito: Energia Reversa e Nível 10]",
    },
    {
        "id": "canalizar_energia_reversa", "nivel_req": 0, "req": ["liberacao_energia_reversa", "canalizar_em_golpe"],
        "nome": "Canalizar Energia Reversa",
        "descricao": "Ação de Movimento: gaste PER igual ao bônus de treinamento para adicionar 2d6 de dano de energia reversa por PER gasto ao próximo ataque contra maldição. Não cumulativo com Canalizar em Golpe. [Pré-Requisito: Liberação de Energia Reversa e Canalizar em Golpe]",
    },
    {
        "id": "cura_em_grupo", "nivel_req": 0, "req": ["liberacao_energia_reversa"],
        "nome": "Cura em Grupo",
        "descricao": "Divida o total da rolagem de cura entre todas as criaturas em alcance 4,5m + 1,5m por ER. Máximo de pontos gastos aumenta em 2. [Pré-Requisito: Liberação de Energia Reversa]",
    },
]

# p.192 — Especiais
APTIDOES_ESPECIAIS = [
    # nivel_req = 0 para todas (sem categoria própria de aptidão; pré-requisitos são de outras categorias)
    {
        "id": "raio_negro", "nivel_req": 0, "req": [],
        "req_nivel": 10, "req_apt_nivel": {"controle_leitura": 3},
        "req_atributos_ou": [{"forca": 16}, {"destreza": 16}],
        "nome": "Raio Negro",
        "descricao": "Ao tirar 20 em ataque corpo a corpo, aplique o Kokusen: dano ×1,5 (ignora resistências). Após o primeiro uso: PE máx +nível e AU +1 (permanente). Estado de Consciência Absoluta: por 1 rodada após kokusen, o valor necessário reduz -1 (máx vezes = metade do CL). [Pré-Requisito: CL 3, Força ou Destreza 16 e Nível 10]",
    },
    {
        "id": "abencado_faiscas_negras", "nivel_req": 0, "req": ["raio_negro"],
        "req_nivel": 15, "req_apt_nivel": {"controle_leitura": 4, "aura": 3},
        "nome": "Abençoado pelas Faíscas Negras",
        "descricao": "Kokusen ocorre em 19 e 20. Durante Estado de Consciência Absoluta, pode reduzir o valor do kokusen 1 vez a mais. Após kokusen: +metade do CL em ataques e +CL total em dano pelo resto da cena. [Pré-Requisito: Raio Negro, CL 4, AU 3 e Nível 15]",
    },
    {
        "id": "dominio_simples", "nivel_req": 0, "req": [],
        "req_nivel": 5, "req_apt_nivel": {"barreira": 1},
        "nome": "Domínio Simples",
        "descricao": "Reação a expansão de domínio ou Ação Bônus (5PE): esfera de 1,5m + DOM × 1,5m de raio. Você e criaturas dentro não são afetados pelo Acerto Garantido e efeitos de ambiente. Concentração; Durabilidade = BAR + 1. Toda deterioração de durabilidade reduz a área em 1,5m. [Pré-Requisito: BAR 1 e Nível 5]",
    },
    {
        "id": "reversao_tecnica", "nivel_req": 0, "req": ["energia_reversa"],
        "req_nivel": 12,
        "nome": "Reversão de Técnica",
        "descricao": "Ao obter um novo Feitiço, pode criar uma Reversão de Técnica no lugar: custo +nível do Feitiço, efeito contrário ao conceito original. Ao obter esta aptidão, receba um Feitiço adicional (obrigatoriamente uma reversão). [Pré-Requisito: Energia Reversa e Nível 12]",
    },
    {
        "id": "tecnica_maxima", "nivel_req": 0, "req": [],
        "req_pericias": [{"nome": "Feitiçaria", "nivel": "mestre"}],
        "nome": "Técnica Máxima",
        "descricao": "Crie uma Técnica Máxima: novo Feitiço que usa valores de Nível 5 (se só tiver acesso ao Nível 4) ou Nível 5 próprio quando disponível. Custo: 25PE. Após usar, aguarde 6 − metade do bônus de treinamento rodadas. [Pré-Requisito: Mestre em Feitiçaria, Capacidade de Conjurar Feitiços Nível 4]",
    },
]

# Catálogo unificado (mantido para compatibilidade com código existente)
APTIDOES_ADICIONAIS = (
    APTIDOES_AURA +
    APTIDOES_CONTROLE_LEITURA +
    APTIDOES_BARREIRA +
    APTIDOES_ENERGIA_REVERSA +
    APTIDOES_ESPECIAIS
)

TODAS_APTIDOES = APTIDOES_DOMINIO + APTIDOES_ADICIONAIS

# Mapeamento de categorias para o template
APTIDOES_CATEGORIAS = [
    {
        "id": "aura",
        "nome": "Aptidão de Aura",
        "icone": "💥",
        "desc": "Uso de EA como aura protetora, reforço corporal e blindagem.",
        "pagina": 174,
        "lista": APTIDOES_AURA,
    },
    {
        "id": "controle_leitura",
        "nome": "Controle e Leitura",
        "icone": "👁",
        "desc": "Percepção, controle fino da EA e supressão de energia.",
        "pagina": 178,
        "lista": APTIDOES_CONTROLE_LEITURA,
    },
    {
        "id": "dominio",
        "nome": "Domínio",
        "icone": "🌐",
        "desc": "Criação e aprimoramento de Expansões de Domínio.",
        "pagina": 182,
        "lista": APTIDOES_DOMINIO,
    },
    {
        "id": "barreira",
        "nome": "Barreira",
        "icone": "🛡",
        "desc": "Criação de barreiras físicas e proteção contra domínios.",
        "pagina": 188,
        "lista": APTIDOES_BARREIRA,
    },
    {
        "id": "energia_reversa",
        "nome": "Energia Reversa",
        "icone": "💚",
        "desc": "Inversão do fluxo de EA para cura e ofensa positiva.",
        "pagina": 189,
        "lista": APTIDOES_ENERGIA_REVERSA,
    },
    {
        "id": "especiais",
        "nome": "Especiais",
        "icone": "⭐",
        "desc": "Aptidões raras que transcendem os limites da técnica.",
        "pagina": 192,
        "lista": APTIDOES_ESPECIAIS,
    },
]

# ─── EXPANSÃO DE DOMÍNIO – TIPOS ───────────────────────────────────────────────

DOMINIO_TIPOS = {
    "incompleta": {
        "nome": "Expansão Incompleta",
        "descricao": "Sem barreira física. Expande energia em raio 4,5m × BM. Pode usar estruturas como barreira improvisada. Sem acerto garantido. Foco em amplificações e efeitos ambientais.",
        "req_aptidao": "expansao_incompleta",
        "tem_acerto_garantido": False,
        "tem_barreira": False,
    },
    "completa_nao_letal": {
        "nome": "Expansão Completa (Não-Letal)",
        "descricao": "Barreira esférica de 9m de raio. Inimigos ficam presos até barreira ser destruída. Foca em efeitos especiais, sem acerto garantido.",
        "req_aptidao": "expansao_completa",
        "tem_acerto_garantido": False,
        "tem_barreira": True,
    },
    "completa_letal": {
        "nome": "Expansão Completa (Letal)",
        "descricao": "Barreira esférica de 9m com técnica imbuída. Garante acerto em todos os ataques contra inimigos dentro da barreira.",
        "req_aptidao": "acerto_garantido",
        "tem_acerto_garantido": True,
        "tem_barreira": True,
    },
    "sem_barreira": {
        "nome": "Expansão Sem Barreira",
        "descricao": "Acerto garantido sem barreira física. Grande alcance (esfera até 9m × BM). Pode destruir expansões inimigas de fora. Não aprisiona inimigos.",
        "req_aptidao": "expansao_sem_barreiras",
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

# ─── CATÁLOGO DE TÉCNICAS INATAS (feit2) ────────────────────────────────────────
# req_origem: None = qualquer origem; string = ID de origem obrigatória
# habilidades: lista completa de habilidades por nível técnico (0-5)
# Desbloqueio por nível de personagem: 0→L1, 1→L4, 2→L8, 3→L12, 4→L16, 5→L20
TECNICAS_INATAS_NIVEL_PERSONAGEM = {0: 1, 1: 4, 2: 8, 3: 12, 4: 16, 5: 20}

TECNICAS_INATAS_CATALOGO = {
    "boneco_palha": {
        "nome": "Boneco de Palha",
        "personagem": "Nobara Kugisaki",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Usa martelo, pregos e boneco de palha imbuídos de energia amaldiçoada para ataques à distância e dano por ligação com vestígios.",
        "funcionamento_basico": [
            "Maestria automática com Martelo. Pregos: BT × 5 por missão.",
            "Boneco de palha causa dano via ligação usando vestígios do alvo.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Disparo de Pregos", "desc": "Ação Comum | 9m | Dispara até BT pregos (+1PE por extra). Luta/Pontaria; acerto: 1d8 perfurante/prego. TR Fortitude: metade dos pregos ficam presos."},
            {"nivel": 0, "nome": "Redirecionamento Constante", "desc": "Passiva. Após Disparo de Pregos, redireciona BT pregos que erraram para objeto/lugar em 3m do alvo."},
            {"nivel": 1, "nome": "Grampo de Cabelo", "desc": "Ação Comum | 12m | Explode 1 prego; criaturas em 4,5m: TR Reflexos = 2d8 força (metade em sucesso). Preso a criatura: troca por Fortitude."},
            {"nivel": 1, "nome": "Ressonância", "desc": "Ação Comum | Infinito | Requer vestígio. Ataque na boneca: dano + 3d6 força no alvo real. Sem visão: desprevenido automático; com visão: TR Reflexos."},
            {"nivel": 2, "nome": "Explosão Repentina", "desc": "Reação | Infinito | Quando aliado ataca alvo do qual você tem vestígios: ressonância como reação. TR Astúcia: desprevenido contra ataque do aliado."},
            {"nivel": 3, "nome": "Decepar", "desc": "Ação Comum | 12m | Luta/Pontaria; acerto: 15d8 perfurante. TR Fortitude: falha = pedaço do corpo arrancado. Aliado em 4,5m pode pegar (ação livre)."},
        ],
        "criacao": {
            "info": "Maestria automática com Martelo concedida ao criar o personagem.",
            "tags": ["Proficiência Automática"],
        },
    },
    "boogie_woogie": {
        "nome": "Boogie Woogie",
        "personagem": "Aoi Todo",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Ao bater palmas, troca posições de objetos ou criaturas. Alvos precisam ter nível mínimo de energia amaldiçoada.",
        "funcionamento_basico": [
            "Troca posição com alvo ou troca dois alvos entre si ao bater palmas.",
            "Alvos sem energia amaldiçoada não são válidos.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Troca de Posição", "desc": "Ação Bônus | 9m | Troca posição de dois alvos (incluindo você). Sem ataque de oportunidade. Atacar criatura movida: TR Reflexos ou desprevenida."},
            {"nivel": 0, "nome": "Troca Emergencial", "desc": "Reação | 6m | Ao perceber ameaça a aliado: Reflexos vs resultado do ataque. Sucesso = troca aliado com outro alvo."},
            {"nivel": 1, "nome": "Ajuste de Alvo", "desc": "Reação | 12m | Se você é alvo de ataque de aliado: troca com alvo válido em 12m. Atacante recebe vantagem ou alvo tem desvantagem."},
            {"nivel": 1, "nome": "Combo Surpresa!", "desc": "Ação Comum | Variável | Ataque com arma de arremesso; ao acertar/aproximar, troca lugar com a arma. Reação: ataque corpo-a-corpo; alvo desprevenido em falha."},
            {"nivel": 2, "nome": "Troca com Objeto Imbuído", "desc": "Ação Comum | 12m | Joga objeto imbuído próximo a criatura; troca com ele; ataque com vantagem. Alvo desprevenido; margem de crítico -1."},
            {"nivel": 3, "nome": "Sequência Imprevisível", "desc": "Ação Completa | 12m | Você + 1 aliado (reação) avançam trocando posições; cada um faz 2 ataques. Criatura desprevenida para todos os ataques."},
        ],
    },
    "chamas_desastre": {
        "nome": "Chamas do Desastre",
        "personagem": "Jogo",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Forma e controla fogo e lava física ou telepaticamente com potencial devastador crescente.",
        "funcionamento_basico": [
            "Cria e controla fogo e lava física ou telepaticamente.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Criar Chama", "desc": "Ação Comum | 9m | Cria foco de chamas; criatura incendiada: TR Fortitude = 1d8 queimante/turno."},
            {"nivel": 0, "nome": "Disparo Ardente", "desc": "Ação Comum | 9m | Ataque; acerto: 1d10 queimante."},
            {"nivel": 0, "nome": "Revestimento Abrasador", "desc": "Passiva. Resistente a dano congelante."},
            {"nivel": 1, "nome": "Aura de Calor", "desc": "Passiva. Criaturas que iniciam turno em 3m: TR Fortitude = 2d8 queimante. Máximo PE -2."},
            {"nivel": 1, "nome": "Orbe de Fogo", "desc": "Ação Comum | 12m | TR Reflexos: 3d8 queimante (metade em sucesso)."},
            {"nivel": 1, "nome": "Toque Queimante", "desc": "Ação Bônus | Sustentada (1PE/rodada) | Mão/arma: +1d10 queimante em ataques corpo-a-corpo."},
            {"nivel": 2, "nome": "Combustão Imediata", "desc": "Ação Comum | 18m | TR Fortitude: 4d8 queimante; falha = incendiada (3d8/turno, -2 para resistir)."},
            {"nivel": 2, "nome": "Explosão Flamejante", "desc": "Ação Comum | Área 4,5m esférica | TR Fortitude: 4d8 queimante (metade)."},
            {"nivel": 2, "nome": "Fogo Verdadeiro", "desc": "Passiva. Dano queimante ignora RD = dobro do BT. Máximo PE -4."},
            {"nivel": 2, "nome": "Insetos de Brasa", "desc": "Variável | 9m | Ação completa: 6; comum: 4; bônus: 2. Por inseto: Pontaria = 1d8 perfurante + explosão (TR Reflexos = 2d8 queimante)."},
            {"nivel": 2, "nome": "Raio de Chamas", "desc": "Ação Comum | Cone 4,5m | TR Fortitude: 4d8 queimante; falha = incendiada (2d8/turno)."},
            {"nivel": 3, "nome": "Bola de Fogo", "desc": "Ação Comum | 24m | Área 9m esférica. TR Fortitude: 4d12 queimante; falha = incendiada (2d6/turno)."},
            {"nivel": 3, "nome": "Erupção Vulcânica", "desc": "Ação Comum | 18m | Vulcão; lava em linha 13,5m × 1,5m. TR Reflexos: 5d12 queimante (metade)."},
            {"nivel": 3, "nome": "Parede Incandescente", "desc": "Ação Comum | 12m | Concentração (5 turnos). Parede 9m; criação: TR Reflexos = 3d12; atravessar: terreno difícil + 2d12."},
            {"nivel": 4, "nome": "Explosão Atrasada", "desc": "Ação Comum | 30m | Concentração (1 min). Esfera; ao explodir: área 12m. TR Fortitude: 6d10 queimante (+1d10/turno mantida)."},
            {"nivel": 4, "nome": "Rio de Lava", "desc": "Ação Comum | Área 12m frontal | Terreno difícil de lava. TR Fortitude: 6d10 queimante; criaturas no início do turno: 4d10."},
            {"nivel": 5, "nome": "Devastação Escaldante", "desc": "Ação Comum | 30m | 3 vulcões em pontos distintos; cone 9m cada. TR Fortitude: 6d10 queimante (metade)."},
            {"nivel": 5, "nome": "Incinerar", "desc": "Ação Comum | 6m | TR Fortitude: 16d12 queimante; chamas duradouras (6d12/turno; sucesso crítico para se livrar)."},
            {"nivel": 5, "nome": "Técnica Máxima: Meteoro", "desc": "Ação Completa | Área 50m esférica | Meteoro cai em 1 rodada. TR Fortitude (desvantagem): 30d10 queimante (metade)."},
            {"nivel": 5, "nome": "Expansão de Domínio: Caixão da Montanha de Ferro", "desc": "Área 9m esférica. Ambiental: 1d10+5 queimante/turno. Amplificação: +1 dado +5 dano e -3 RD em habilidades de técnica. Acerto Garantido."},
        ],
    },
    "colera_estrelas": {
        "nome": "Cólera das Estrelas",
        "personagem": "Yuki Tsukumo",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Infunde massa imaginária para amplificar ataques corpo-a-corpo. Acompanhada do shikigami Garuda.",
        "funcionamento_basico": [
            "Concede massa imaginária (força proporcional à massa).",
            "Troca 1 habilidade inicial por invocação Garuda (4° Grau, 2PE; PV35 CA17).",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Punho Pesado", "desc": "Ação Bônus | Sustentada (1PE/turno) | +1 dado de dano em ataques corpo-a-corpo."},
            {"nivel": 0, "nome": "Transformar Garuda", "desc": "Ação Bônus | Toque | Garuda vira chicote (1d8, Estendida+Pesada). Reversível como ação livre."},
            {"nivel": 1, "nome": "Punho Pesado: Amplificação", "desc": "Ação Bônus | Sustentada (1PE/turno) | +1 dado +2 em ataques corpo-a-corpo."},
            {"nivel": 1, "nome": "Laço Pesado", "desc": "Ação Comum | 12m | Garuda laça alvo: TR Reflexos → falha = Agarrado + Caído. TR/turno para escapar."},
            {"nivel": 2, "nome": "Punho Pesado: Amplificação Dupla", "desc": "Ação Bônus | Sustentada (1PE/turno) | +2 dados em ataques corpo-a-corpo."},
            {"nivel": 2, "nome": "Esmagamento", "desc": "Ação Comum | 12m | Garuda como chicote; Luta: 8d8 impacto. TR Fortitude: falha = derrubada."},
            {"nivel": 2, "nome": "Punho Imparável", "desc": "Passiva. Ataques com Punho Pesado ativo ignoram RD = dobro BT. Máximo PE -4."},
            {"nivel": 3, "nome": "Punho Pesado: Amplificação Tripla", "desc": "Ação Bônus | Sustentada (2PE/turno) | +3 dados em ataques corpo-a-corpo."},
            {"nivel": 3, "nome": "Chute Devastador", "desc": "Ação Comum | 24m | Garuda como projétil; TR Reflexos: 12d8 impacto (metade)."},
            {"nivel": 4, "nome": "Punho Pesado: Amplificação Quadrupla", "desc": "Ação Bônus | Sustentada (2PE/turno) | +4 dados em ataques corpo-a-corpo."},
            {"nivel": 4, "nome": "Destruição Absoluta", "desc": "Ação Comum | Linha 18m | TR Reflexos: 10d10 impacto (metade). Pode tornar área em terreno difícil."},
            {"nivel": 5, "nome": "Buraco Negro", "desc": "Ação Completa | Área 18m esférica | 3 rodadas. TR Fortitude: Imóvel (falha) / Lento (sucesso). Início de rodada: criaturas puxadas 9m + 12d12 força."},
        ],
        "criacao": {
            "info": "Troca 1 habilidade inicial pelo shikigami Garuda (4° Grau, 2PE; PV35 CA17). Garuda pode ser transformada em chicote (1d8, Estendida+Pesada).",
            "tags": ["Invocação Inicial", "Troca de Habilidade"],
        },
    },
    "copia": {
        "nome": "Cópia",
        "personagem": "Yuta Okkotsu",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Shikigami Rika armazena técnicas e ferramentas. Permite copiar habilidades de outras técnicas após Rika acertar uma Mordida.",
        "funcionamento_basico": [
            "Troca 1 habilidade inicial por Rika. Rika tem turno próprio e cresce com o BT.",
            "Cópia: Rika acerta Mordida → copia habilidade (ação bônus). 1 cópia ativa; pode memorizar (slot de habilidade).",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Rika (Mestria +2)", "desc": "Invocação [2PE] PV30 CA17 | FOR16 DEX12 CON12. Mordida +5, 2d8+3 perfurante. Armazém (espaços = mod FOR). Perícias: Atletismo+5, Fortitude+3, Luta+5."},
            {"nivel": 1, "nome": "Rika (Mestria +3)", "desc": "Invocação [5PE] PV60 CA18 | FOR18 CON16. Mordida +9, 2d12+4. Disparo de Energia +9, 2d10+4 força. Perícias: Atletismo+9, Fortitude+8, Luta+9."},
            {"nivel": 2, "nome": "Rika (Mestria +4)", "desc": "Invocação [8PE] PV90 CA20 | FOR22 DEX14 CON18. Mordida +14 (alcance 3m), 3d10+6. Disparo +14, 3d8+6. Paixão Raivosa: <metade PV → +5 em tudo."},
            {"nivel": 3, "nome": "Rika (Mestria +5)", "desc": "Invocação [10PE] PV130 CA22 | FOR26 CON22. Mordida +18 (3m), 4d10+8. Disparo +18, 4d8+8. Repor Energia (1×/descanso longo). Paixão Raivosa: vantagem. Proteção Apaixonada: nega PV→0."},
            {"nivel": 4, "nome": "Rika (Mestria +6)", "desc": "Invocação [12PE] PV210 CA25 | FOR30 DEX20 CON30. Mordida +22 (4,5m), 4d12+20. Disparo +22, 4d10+20. Repor Energia: nível em PE. Proteção Apaixonada: nega completamente."},
            {"nivel": 5, "nome": "Expansão de Domínio: Puro Amor Mútuo", "desc": "Área 9m esférica. Infinitas Cópias — técnicas copiadas em katanas; pegar katana = ação livre; usar técnica = ação comum sem PE. Acerto Garantido disponível."},
        ],
        "criacao": {
            "info": "Troca 1 habilidade inicial pelo shikigami Rika (invocação especial com turno próprio que cresce com o Bônus de Treinamento).",
            "tags": ["Invocação Inicial", "Troca de Habilidade"],
        },
    },
    "criatura_ambar": {
        "nome": "Criatura Mística Âmbar",
        "personagem": "Hajime Kashimo",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Reconstrói o corpo convertendo energia para manifestar fenômenos elétricos. Aura com propriedades elétricas constantes.",
        "funcionamento_basico": [
            "Recebe aptidão Aura Elemental (Chocante) automaticamente.",
            "Ativação da Técnica (ação livre): escolhe fenômenos; 1 exaustão por fenômeno ao encerrar.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Acúmulo de Carga", "desc": "Passiva. Ao acertar ataque: criatura ganha 1 carga positiva. Início de combate: 2 cargas negativas + 2/rodada."},
            {"nivel": 1, "nome": "Liberação de Raio", "desc": "Ação Comum | 12m | Req: 2 cargas negativas + alvo com carga positiva. TR Fortitude: 2d8 chocante + 1d8/carga extra (máx 3 dados adicionais)."},
            {"nivel": 1, "nome": "Aprimoramento de Cargas", "desc": "Passiva. 1×/rodada: ao receber/implementar carga, recebe 1 adicional. Dobra dados máximos de Liberação. Máximo PE -2."},
            {"nivel": 2, "nome": "Destruição Inevitável", "desc": "Passiva. Golpes com dano chocante/força ignoram RD = dobro BT. Máximo PE -4."},
            {"nivel": 2, "nome": "Fenômeno: Garras Âmbar", "desc": "Ativação (4PE). Garras nos braços: punhos = armas marciais Leve+Fineza + 3d8 força ou chocante."},
            {"nivel": 2, "nome": "Fenômeno: Canhão Vocal", "desc": "Ativação (4PE). Ação comum: onda sonora 6m → TR Fortitude: 6d8 força (metade); falha = Surdo 1 rodada."},
            {"nivel": 3, "nome": "Fenômeno: Visão Raio-X", "desc": "Ativação (6PE). +10 Percepção, +4 Reflexos, +4 Rolagens de Ataque; visão em raio-X."},
            {"nivel": 3, "nome": "Fenômeno: Palmas Místicas", "desc": "Ativação (6PE). Ação comum: rajada linha 13,5m → TR Reflexos: 8d12 força (metade)."},
            {"nivel": 4, "nome": "Condenação Voltaica", "desc": "Ação Comum | 30m | Req: 4 cargas negativas + alvo com 4+ positivas. TR Fortitude: 8d10 chocante; falha = Paralisado 1 rodada."},
            {"nivel": 4, "nome": "Presa do Deus do Raio", "desc": "Ação Comum | 30m | Req: 4 neg + 4 pos. TR Fortitude: 8d10 chocante; sucesso: membro aleatório; falha: você escolhe a consequência."},
            {"nivel": 5, "nome": "Fenômeno: Ativação Intracerebral", "desc": "Ativação (10PE). Destreza +6; +1 ação de movimento/turno; vantagem em Reflexos e Acrobacia."},
        ],
        "criacao": {
            "info": "Recebe a aptidão Aura Elemental (Chocante) automaticamente ao criar o personagem, sem custo.",
            "tags": ["Aptidão Automática"],
        },
    },
    "dez_sombras": {
        "nome": "Dez Sombras",
        "personagem": "Megumi Fushiguro",
        "tipo": "Técnica Herdada",
        "req_origem": "herdado_zenin",
        "descricao": "Leque de 10 shikigamis obtidos via ritual. Poderes sobre sombras; começa com os 2 Cães Divinos.",
        "funcionamento_basico": [
            "Máximo de invocações = 10. Ritual de Exorcismo (ação comum, área 18m) para obter novos shikigamis.",
            "Começa com 2 Cães Divinos. Heranças das Sombras: shikigami exorcizado transfere poder.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Estoque das Sombras", "desc": "Passiva. Armazena até 5 espaços de item na sombra. Retirar: 1ª vez ação livre, depois ação bônus."},
            {"nivel": 0, "nome": "Cão Divino (×2)", "desc": "Invocação [4° Grau, 2PE] PV25 CA19 Mov10,5m | +5, 2d8+3 perfurante. Alcateia: +2 se aliado a 1,5m."},
            {"nivel": 1, "nome": "Ocultação Sombria", "desc": "Ação Bônus | 4,5m | Entra em sombra: indetectável e invisível. Ao sair e atacar: criatura desprevenida."},
            {"nivel": 1, "nome": "Passo Sombrio", "desc": "Ação Bônus | 9m | Teleporta para sombra de criatura não-hostil. Sem ataque de oportunidade."},
            {"nivel": 1, "nome": "Nue", "desc": "Invocação [4° Grau, 3PE] PV25 CA19 Voo | +5, 2d8+3 chocante. Alado, Montaria."},
            {"nivel": 1, "nome": "Sapo", "desc": "Invocação [4° Grau, 3PE] PV25 CA18 | Segurar (língua); Arremessar (2d6+3 impacto, TR→Caído); Fora de Risco (reação, nega ataque)."},
            {"nivel": 2, "nome": "Grande Serpente", "desc": "Invocação [4° Grau, 4PE] PV25 CA19 | Entrelaçar + Mordida +5 2d8+3. Grande, Flexível."},
            {"nivel": 2, "nome": "Elefante Máximo", "desc": "Invocação [3° Grau, 7PE] PV80 CA22 | Golpe Tromba 2d12+4. Torrente: TR Fortitude 2d10+4 + empurra 4,5m. Grande, Robustez."},
            {"nivel": 2, "nome": "Cervo Circular", "desc": "Invocação [2° Grau, 7PE] PV70 CA17 | Cura 3d10+5 (foco) / 2d12+5 (área 3m). Fluxo Reverso: +6 TR de técnicas."},
            {"nivel": 3, "nome": "Fuga do Coelho", "desc": "Reação | Ao ser alvo de ataque: invoca coelhos, nega o ataque. Move para ponto desocupado em 9m sem ataque de oportunidade."},
            {"nivel": 3, "nome": "Touro Perfurante", "desc": "Invocação [2° Grau, 6PE] PV85 CA17 Mov16,5m | Investida +9 2d10+7; +1d10 por 3m em linha reta. Grande."},
            {"nivel": 3, "nome": "Cão Divino: Totalidade", "desc": "Invocação [4° Grau, 3PE] PV35 CA22 Mov12m | +8, 3d8+6. Alcateia +4. Grande."},
            {"nivel": 4, "nome": "O Abismo Desconhecido do Poço", "desc": "Invocação [4° Grau, 6PE] Quimera Nue+Sapo. PV50 CA21 Voo | Grupo (3 sapos; +2 Reflexos+Luta/sapo)."},
            {"nivel": 4, "nome": "Tigre Fúnebre", "desc": "Invocação [2° Grau, 7PE] PV80 CA19 | Presas 3d10+5 necrótico; Garras 3d10+5 cortante. Arauto do Funeral: -metade da cura recebida por dano necrótico."},
            {"nivel": 4, "nome": "Agito", "desc": "Invocação [2° Grau, 7PE] PV120 CA27 Mov18m | Golpes +11 5d10+6 chocante. Cura Concentrada: 5d10+3. Regeneração Superior."},
            {"nivel": 5, "nome": "General Divino Mahoraga", "desc": "Invocação [Especial, 18PE] PV200 CA26 | Punho +9 4d12+7. Regeneração: 5d10+6. Adaptação Defensiva: resistente→imune. Adaptação Ofensiva: +5 acerto acumulativo. Burlar Defesas."},
            {"nivel": 5, "nome": "Expansão de Domínio: Jardim das Sombras Sobrepostas", "desc": "Incompleta. Área = 4,5m × BT. Invocações Persistentes (todas ativas sem custo). Clones (metade BT). Chão de Sombras (1PE/rodada ou cair)."},
        ],
        "criacao": {
            "info": "Começa com 2 Cães Divinos disponíveis (shikigami do 4° Grau). Requer origem Herdado Zenin.",
            "tags": ["Invocações Iniciais", "Requer Origem"],
        },
    },
    "fala_amaldicada": {
        "nome": "Fala Amaldiçoada",
        "personagem": "Toge Inumaki",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": "herdado_inumaki",
        "descricao": "Palavras imbuídas de energia tornam-se comandos compulsórios. Criaturas sem energia amaldiçoada falham automaticamente.",
        "funcionamento_basico": [
            "Criaturas sem energia amaldiçoada falham automaticamente (exceto Restringidos).",
            "4 níveis abaixo: falha auto; 4 níveis acima: vantagem para resistir.",
            "Nível 3+: TR Fortitude ao usar (perde PV = custo da habilidade em falha).",
        ],
        "habilidades": [
            {"nivel": 1, "nome": "Comando: Correr", "desc": "Ação Comum | 12m | Qualquer número de criaturas. Involuntárias: TR Vontade. Falha: movem-se distância de movimento."},
            {"nivel": 1, "nome": "Comando: Desorientar", "desc": "Ação Comum | 12m | 1 criatura. TR Astúcia: 2d8 psíquico; falha = Desorientado 1 rodada."},
            {"nivel": 1, "nome": "Comando: Torcer", "desc": "Ação Comum | 12m | 1 criatura. TR Fortitude: 3d8 força (metade)."},
            {"nivel": 2, "nome": "Comando: Explodir", "desc": "Ação Comum | 12m | TR Fortitude: 5d8 força; adjacentes ao alvo: TR Reflexos = metade do dano."},
            {"nivel": 2, "nome": "Comando: Focar", "desc": "Ação Bônus | 18m | +5 nas próximas 2 rolagens de perícia do alvo."},
            {"nivel": 2, "nome": "Comando: Sangrar", "desc": "Ação Comum | 18m | TR Fortitude: 4d8 cortante; falha = Sangramento Médio (3d8/turno)."},
            {"nivel": 2, "nome": "Comando: Resistir", "desc": "Ação Comum | 18m | 2 aliados. Sustentada (1PE/rodada). RD 6 contra todos tipos (exceto alma)."},
            {"nivel": 2, "nome": "Comando: Temer", "desc": "Ação Bônus | 18m | TR Vontade: 1d8 psíquico; falha = Amedrontado 1 rodada."},
            {"nivel": 3, "nome": "Comando: Levantar", "desc": "Ação Comum | 24m | Estabiliza criatura inconsciente; cura 4d12 PV."},
            {"nivel": 3, "nome": "Comando: Parar", "desc": "Ação Comum | 24m | TR Vontade: falha = Imóvel + Incapacitado 1 rodada; sucesso = Lento 1 rodada."},
            {"nivel": 4, "nome": "Comando: Apagar", "desc": "Ação Comum | 30m | Qualquer número de criaturas. TR Vontade: falha = Inconsciente até ser acordado."},
            {"nivel": 5, "nome": "Comando: Obedecer", "desc": "Ação Completa | 48m | 1 criatura. TR Vontade: falha = você controla a criatura no próximo turno dela."},
        ],
        "criacao": {
            "info": "Requer origem Herdado Inumaki. Criaturas sem energia amaldiçoada falham automaticamente nos testes contra seus comandos.",
            "tags": ["Requer Origem", "Poder Passivo"],
        },
    },
    "formacao_gelo": {
        "nome": "Formação de Gelo",
        "personagem": "Uraume",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Cria e manipula gelo mentalmente. Pode congelar criaturas progressivamente (Leve → Médio → Total).",
        "funcionamento_basico": [
            "Cria gelo físico ou mentalmente. Condição própria: Leve (Desprevenido+Lento), Médio (+desvantagem físicos), Total (Imóvel+Incapacitado, crítico auto).",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Criação de Gelo", "desc": "Variável | 9m | Cria formações, objetos, congela superfícies."},
            {"nivel": 0, "nome": "Espeto de Gelo", "desc": "Ação Comum | 9m | Ataque (Feitiçaria/Pontaria): 1d10 perfurante."},
            {"nivel": 1, "nome": "Brisa Gelada", "desc": "Ação Comum | 12m | TR Fortitude: 3d8 congelante; falha = desvantagem no próximo teste físico."},
            {"nivel": 1, "nome": "Revestimento de Gelo", "desc": "Ação Bônus | Sustentada (1PE/rodada) | Arma: +1d10 congelante; armadura: +4 RD (exceto queimante/alma)."},
            {"nivel": 2, "nome": "Congelamento", "desc": "Ação Comum | 6m | TR Fortitude: 4d8 congelante; falha = Congelamento ou +1 passo (máx Médio)."},
            {"nivel": 2, "nome": "Estaca Explosiva", "desc": "Ação Comum | 18m | Ataque: 4d8 perfurante. Explode: criaturas em 3m → TR Reflexos: 4d8 congelante (metade)."},
            {"nivel": 3, "nome": "Avalanche", "desc": "Ação Comum | 24m | Área 4,5m esférica. TR Fortitude: 1 nível Congelamento; depois TR Reflexos: 6d12 congelante (máx Médio)."},
            {"nivel": 4, "nome": "Calmaria da Geada", "desc": "Ação Comum | Cone 12m | TR Fortitude: falha = 2 níveis; sucesso = 1; crítico = 0 (máx Total)."},
            {"nivel": 4, "nome": "Empalamento Devastador", "desc": "Ação Comum | 18m | Ataque +2: 10d10 perfurante. TR Fortitude: falha = Ferida Interna."},
            {"nivel": 4, "nome": "Toque Congelante", "desc": "Ação Comum | Toque | TR Fortitude: crítico = nada; sucesso = 2 níveis; falha = 3 níveis Congelamento (máx Total)."},
        ],
    },
    "ilimitado": {
        "nome": "Ilimitado",
        "personagem": "Satoru Gojo",
        "tipo": "Técnica Herdada",
        "req_origem": "herdado_gojo",
        "descricao": "Traz o conceito de Infinito para a realidade, manipulando e distorcendo espaço. Complementado pelos Seis Olhos.",
        "funcionamento_basico": [
            "BT × por descanso: anula completamente 1 ataque/habilidade.",
            "Imune a dano de criaturas com ND ≤ metade do nível. CA +2 e RD 2 contra todos (exceto alma); aumenta nos níveis 5, 9, 13 e 17.",
        ],
        "habilidades": [
            {"nivel": 1, "nome": "Azul: Atração", "desc": "Ação Comum | 12m | TR Fortitude: 2d10 força; falha = puxada 6m na sua direção."},
            {"nivel": 1, "nome": "Movimento Imediato", "desc": "Ação Bônus | 9m | Teleporta para espaço desocupado. Sem ataque de oportunidade."},
            {"nivel": 1, "nome": "Azul: Atração Constante", "desc": "Ação Bônus | Sustentada (1PE/turno) | Punhos atraem no impacto: +1d10 força em ataques desarmados."},
            {"nivel": 1, "nome": "Amplificação do Infinito", "desc": "Reação | Dobra bônus de CA e RD do Infinito até fim do turno. Custo aumenta em 2PE cada vez que os bônus aumentaram."},
            {"nivel": 1, "nome": "Voar", "desc": "Passiva. +9m movimento de voo; pode se manter estático no ar. Máximo PE -2."},
            {"nivel": 2, "nome": "Azul: Compressão", "desc": "Ação Comum | 18m | TR Fortitude: 7d8 força (metade)."},
            {"nivel": 2, "nome": "Azul: Colisão", "desc": "Ação Completa | 18m | 2 criaturas. TR Fortitude: 2d8 força + puxadas para colisão. Colisão: +1d8/categoria acima de minúsculo."},
            {"nivel": 2, "nome": "Desvio Imediato", "desc": "Reação | Ao receber ataque corpo-a-corpo: Reflexos vs resultado. Sucesso: nega + move 3m; falha: metade do dano."},
            {"nivel": 3, "nome": "Ponto de Atração", "desc": "Ação Comum | 24m | Sustentada (2PE/rodada). Área 6m. TR Fortitude: 4d12 força; falha = Imóvel + puxada. Dentro: Lento + terreno difícil."},
            {"nivel": 3, "nome": "Teleporte de Longa Distância", "desc": "Ação Comum | Teleporta a longa distância (lugar conhecido); leva criaturas/objetos em contato."},
            {"nivel": 3, "nome": "Vermelho: Repulsão", "desc": "[Req: Reversão de Técnica] Ação Comum | 24m | TR Fortitude: 10d8 força; falha = empurrada 12m."},
            {"nivel": 4, "nome": "Azul: Implosão Absoluta", "desc": "Ação Completa | 6m | TR Fortitude: 3d10; falha = perde braços ou pernas (à sua escolha)."},
            {"nivel": 4, "nome": "Disparo Carmesim", "desc": "[Req: Reversão] Ação Comum | 30m | TR Reflexos: 12d10 força; falha = empurrada 18m."},
            {"nivel": 4, "nome": "Vermelho Controlado", "desc": "[Req: Reversão] Ação Comum | 18m | TR Fortitude: 12d10 força; pode mover e explodir. Criatura no alcance: reação p/ ataque vantagem + crítico."},
            {"nivel": 5, "nome": "Vazio Roxo", "desc": "[Req: Reversão] Ação Completa | Linha 27m × 4,5m | Tudo apagado. Criaturas: TR Fortitude: 17d12 força. PV→0 = apagada da existência. Ignora imunidade/RD."},
            {"nivel": 5, "nome": "Técnica Máxima: Vazio Roxo Irrestrito", "desc": "[Req: Reversão] Ação Completa | 9m | Área 50m. TR Fortitude (desvantagem): 26d10 força. Ignora tudo. Você recebe 1/4 do dano."},
            {"nivel": 5, "nome": "Expansão de Domínio: Vazio Imensurável", "desc": "[Req: Seis Olhos] Área 9m. Acerto Garantido (Descarga de Informações): TR Astúcia → falha = atributos mentais a 0."},
        ],
        "criacao": {
            "info": "Requer origem Herdado Gojo. Concede passivamente CA +2 e RD 2 contra todos os tipos (exceto alma). BT × usos por descanso para anular 1 ataque/habilidade completamente.",
            "tags": ["Requer Origem", "Defesa Passiva"],
        },
    },
    "love_redenzvous": {
        "nome": "Love Redenzvous",
        "personagem": "Kirara Hoshi",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Marca energia com estrelas do Cruzeiro do Sul. Marcados devem seguir ordem sequencial para se aproximar uns dos outros.",
        "funcionamento_basico": [
            "Estrelas em ordem: Imai → Acrux → Mimosa → Ginan → Gracrux.",
            "Mover fora da ordem: impossibilitado + alvo com mesma estrela é atraído de volta.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Marcar Energia", "desc": "Variável | Ação comum: até 2 energias; bônus: 1. Remoção: ação livre. Dura até desativar."},
            {"nivel": 0, "nome": "Imbuir Objeto", "desc": "Variável | Toque | Ação comum: 3 objetos; bônus: 2; livre: 1. Herdam estrela da sua energia."},
            {"nivel": 0, "nome": "Marcação Rápida", "desc": "Passiva. Pode usar Marcar Energia como reação."},
            {"nivel": 1, "nome": "Agilidade com Estrelas", "desc": "Passiva. Marcar: 3 criaturas (comum) / 2 (bônus). Máximo PE -2."},
            {"nivel": 1, "nome": "Marcas Ocultas", "desc": "Passiva. Marcado precisa de ação bônus para descobrir qual estrela tem. Máximo PE -2."},
        ],
    },
    "manipulacao_fantoches": {
        "nome": "Manipulação de Fantoches",
        "personagem": "Kokichi Muta",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Controla remotamente corpos amaldiçoados. Restrição congênita: atributos físicos limitados a 4; mentais +4; PE máximo × 1,5.",
        "funcionamento_basico": [
            "Restrição Congênita: FOR/DEX/CON ≤ 4; INT/SAB +4; PE máximo × 1,5.",
            "Controla Fantoche Definitivo remotamente (sem limite de alcance). Fantoche usa ficha própria.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Modo de Lâmina", "desc": "Ação Bônus | Ilimitada | Ataques desarmados do fantoche: 1d6 cortante."},
            {"nivel": 1, "nome": "Escudo Definitivo", "desc": "Ação Bônus | Sustentada (1PE/rodada) | CA +2; reação ao ataque corpo-a-corpo: 2d6 perfurante no atacante."},
            {"nivel": 1, "nome": "Giro Definitivo", "desc": "Ação Comum | 12m | Req: Modo de Lâmina. TR Reflexos: 3d8 perfurante (metade)."},
            {"nivel": 1, "nome": "Impulso", "desc": "Ação Bônus | Move até 7,5m sem ataque de oportunidade."},
            {"nivel": 2, "nome": "Ultra Canhão: Disperso", "desc": "Ação Comum | Linha 9m | TR Reflexos: 4d8 força (metade)."},
            {"nivel": 2, "nome": "Ultra Canhão: Focado", "desc": "Ação Comum | 18m | TR Reflexos: 7d8 força (metade)."},
            {"nivel": 3, "nome": "Modo: Albatroz", "desc": "Ação Bônus | Sustentada (2PE/rodada) | Cabeça vira canhão: ataques +2 níveis de dano. Pontaria ou Feitiçaria."},
            {"nivel": 4, "nome": "Canhão Definitivo", "desc": "Ação Comum | 30m | Req: Modo Albatroz. TR Reflexos: 13d10 força (metade); +Desorientado 4 rodadas."},
        ],
        "criacao": {
            "info": "Restrição Congênita: FOR, DES e CON ficam limitados ao valor máximo 4. Em compensação, INT e SAB recebem +4 automático e o PE máximo é multiplicado por 1,5.",
            "atrib_max": {"forca": 4, "destreza": 4, "constituicao": 4},
            "atrib_bonus": {"inteligencia": 4, "sabedoria": 4},
            "pe_multiplicador": 1.5,
            "tags": ["Restrição Congênita", "Bônus Mental"],
        },
    },
    "manipulacao_maldicoes": {
        "nome": "Manipulação de Maldições",
        "personagem": "Suguru Geto",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Absorve maldições derrotadas e as controla como invocações. Pode usar as técnicas das maldições absorvidas.",
        "funcionamento_basico": [
            "Maldição derrotada (você causou dano) → esfera negra → absorver = invocação.",
            "Maldição absorvida com técnica: pode usar suas habilidades (custo em PE).",
            "Pode trocar habilidade de técnica por +1 no máximo de invocações.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Invocação Emergencial", "desc": "Reação | Ao ser alvo de dano: invoca maldição (metade do custo). Reduz dano em 5 × PE gasto."},
            {"nivel": 0, "nome": "Invocação Explosiva", "desc": "Ação Completa | Invoca 1 + metade BT maldições; cada uma realiza 1 ação complexa imediata."},
            {"nivel": 0, "nome": "Invocação Rápida", "desc": "Ação Comum | Invoca máximo de maldições possíveis de uma vez (dentro de 9m)."},
            {"nivel": 0, "nome": "Técnica Máxima: Uzumaki", "desc": "Ação Completa | 36m | Combina maldições em espiral. TR Reflexos. Dano: 2d12/maldição 4° grau; +2d12/grau superior."},
        ],
        "criacao": {
            "info": "Pode trocar 1 habilidade de técnica por +1 no máximo de invocações disponíveis.",
            "tags": ["Troca de Habilidade"],
        },
    },
    "manipulacao_passaros": {
        "nome": "Manipulação de Pássaros Negros",
        "personagem": "Mei Mei",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Imbui corvos com energia e os controla. Início de missão: pássaros = dobro do BT (CA 12, PV 5 cada).",
        "funcionamento_basico": [
            "Controla corvos imbuídos à vontade. Início de missão: pássaros = dobro do BT.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Conexão Telepática", "desc": "Ação Bônus | 9m | Conecta a qualquer número de pássaros em 9m. Fica Cego; vê pelos olhos dos corvos; controla movimento (máx 100m)."},
            {"nivel": 1, "nome": "Rasante Energético", "desc": "Ação Comum | 12m | 1 a 4 pássaros; 1d8 força/pássaro. TR Reflexos: metade."},
            {"nivel": 1, "nome": "Nuvem de Corvos", "desc": "Ação Comum | 12m | 1 aliado. Corvos circundam: CA +1/corvo. Cancela com ação livre."},
            {"nivel": 2, "nome": "Avanço Coletivo", "desc": "Ação Comum | 18m | 1 a 4 pássaros; 2d8 força/pássaro + Desprevenida. TR Reflexos: metade + evita condição."},
            {"nivel": 2, "nome": "Sacrifício Defensivo", "desc": "Reação | Sacrifica qualquer número de pássaros: -10 dano/pássaro."},
            {"nivel": 3, "nome": "Festim dos Corvos", "desc": "Ação Comum | 24m | 1 a 5 pássaros; 3d8 força/pássaro. TR Fortitude/início de turno. Dura até pássaros morrerem."},
            {"nivel": 4, "nome": "Descarga Devastadora", "desc": "Ação Comum | 30m | 1 a 6 pássaros; 3d10 força/pássaro + Desprevenida + Desorientada. 50% chance de morte/pássaro."},
            {"nivel": 5, "nome": "Ataque do Corvo Kamikaze", "desc": "Ação Comum | 48m | 1 a 6 pássaros; 3d12/pássaro. Todos os pássaros morrem. 6 usados + alvo falha: Atordoado 1 rodada."},
        ],
        "criacao": {
            "info": "No início de cada missão, o personagem começa com corvos = dobro do BT (CA 12, PV 5 cada).",
            "tags": ["Recurso de Missão"],
        },
    },
    "manipulacao_sanguinea_kamo": {
        "nome": "Manipulação Sanguínea",
        "personagem": "Noritoshi Kamo",
        "tipo": "Técnica Herdada",
        "req_origem": "herdado_kamo",
        "descricao": "Manipula o próprio sangue. Cada habilidade custa PV adicionais (0→1PV, 1→3PV, 2→5PV, 3→8PV, 4→12PV, 5→20PV).",
        "funcionamento_basico": [
            "Custo PV por nível da habilidade (ignora redução). Sangue tóxico para maldições.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Bolsas de Sangue", "desc": "Passiva. Início de missão: metade do BT em bolsas (BT × 5 PV cada; usáveis no lugar dos seus)."},
            {"nivel": 0, "nome": "Cobrir com Sangue", "desc": "Ação Bônus | Sustentada (1PE + custo PV/rodada) | +1d10 dano em arma ou projétil."},
            {"nivel": 0, "nome": "Fluxo Contido", "desc": "Passiva. Vantagem em testes de morte; imune a Sangramento."},
            {"nivel": 1, "nome": "Flecha de Sangue", "desc": "Reação | Em ataque à distância: +2d10 no acerto; se errar, rerola (melhor resultado)."},
            {"nivel": 1, "nome": "Restrição Carmesim", "desc": "Ação Comum | 12m | TR Reflexos (CD+2): falha = Imóvel; sucesso = Enredado. TR Atletismo/turno para escapar."},
            {"nivel": 2, "nome": "Bloqueio Rápido", "desc": "Reação | Gasta até BT × 5 PV: cada PV reduz dano em 2."},
            {"nivel": 2, "nome": "Sangue Perfurante", "desc": "Ação Comum | 24m | Ataque +2: 9d8 perfurante."},
            {"nivel": 2, "nome": "Ciclagem Sanguínea", "desc": "Passiva. Após usar habilidade: TR Fortitude = recupera metade dos PV gastos. Máximo PE -4."},
            {"nivel": 3, "nome": "Convergência", "desc": "Ação Comum | 30m | Ataque +4: 15d8 perfurante."},
            {"nivel": 3, "nome": "Exorcismo Cortante", "desc": "Ação Comum | 24m | TR Reflexos: 9d8 cortante; falha = Sangramento Forte (4d12/turno)."},
            {"nivel": 3, "nome": "Fluxo das Escamas Vermelhas", "desc": "Ação Bônus | Sustentada (2PE/turno) | FOR+2, DEX+2, movimento +3m, +4 Reflexos."},
        ],
        "criacao": {
            "info": "Requer origem Herdado Kamo. Cada habilidade custa PV adicionais além do PE (custos por nível: 0→1PV, 1→3PV, 2→5PV, 3→8PV, 4→12PV, 5→20PV). Esse custo ignora redução de dano.",
            "tags": ["Requer Origem", "Custo em PV"],
        },
    },
    "manipulacao_sanguinea_choso": {
        "nome": "Manipulação Sanguínea (Choso)",
        "personagem": "Choso",
        "tipo": "Técnica Herdada",
        "req_origem": "feto_amaldicado",
        "descricao": "Cria sangue a partir de energia (sem custo em PV). Exclusiva para Feto Amaldiçoado Híbrido.",
        "funcionamento_basico": [
            "Manipula sangue; cria orbes de energia. Sem custo em PV.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Convergência", "desc": "Variável | Cria orbes de sangue (ação completa: 3; comum: 2; bônus: 1). Ação livre: move orbes em 9m."},
            {"nivel": 0, "nome": "Conversão de Sangue", "desc": "Passiva. Imune a Sangramento; soma mod.CON em testes de morte."},
            {"nivel": 0, "nome": "Sangue Venenoso", "desc": "Passiva. Ao ser atingido corpo-a-corpo: atacante recebe dano venenoso = mod.CON. Resistente a veneno."},
            {"nivel": 1, "nome": "Corpo Livre", "desc": "Ação Bônus | Sustentada (1PE/rodada) | Alcance de ações e ataques +3m."},
            {"nivel": 1, "nome": "Correção de Trajetória", "desc": "Passiva. Ao errar ataque de habilidade: reação para rerolar (fica com o novo). Máximo PE -2."},
            {"nivel": 1, "nome": "Disparar Sangue", "desc": "Ação Comum | 12m | Usa 1 orbe. Ataque Pontaria: 4d8 perfurante."},
            {"nivel": 1, "nome": "Punhos Sangrentos", "desc": "Ação Bônus | Sustentada (1PE/rodada) | Ataques desarmados: +1 dado de dano."},
            {"nivel": 2, "nome": "Endurecer Sangue", "desc": "Reação | Ao receber dano físico: reduz à metade + RD 5 contra físico até fim da rodada."},
            {"nivel": 2, "nome": "Gume de Sangue", "desc": "Ação Bônus | Concentração | Adaga de sangue: Fineza+Leve+Marcial, crítico 18, 2d8 cortante."},
            {"nivel": 2, "nome": "Sangue Perfurante", "desc": "Ação Comum | 18m | Usa 1 orbe. Pontaria: 8d8 perfurante."},
            {"nivel": 3, "nome": "Exorcismo Cortante: Disco", "desc": "Ação Comum | 24m | TR Reflexos: 14d8 cortante (metade)."},
            {"nivel": 3, "nome": "Supernova", "desc": "Ação Comum | Detona 3 orbes (área 4,5m/orbe). Por orbe: TR Reflexos: 2d12 perfurante (metade)."},
            {"nivel": 3, "nome": "Fluxo das Escamas Vermelhas", "desc": "Ação Bônus | Sustentada (2PE/turno) | FOR+2, DEX+2, movimento +3m, +4 Reflexos."},
            {"nivel": 4, "nome": "Exorcismo Cortante: Correnteza", "desc": "Ação Comum | Linha 18m × 3m | TR Reflexos: 10d10 cortante (metade)."},
            {"nivel": 4, "nome": "Meteorito de Sangue", "desc": "Ação Comum | 6m | TR Fortitude: 10d10 perfurante; falha = Ferida Interna (CD 20)."},
            {"nivel": 4, "nome": "Fluxo das Escamas: Empilhar", "desc": "Ação Bônus | Sustentada (2PE/turno) | FOR+2, DEX+2, movimento +4,5m, +7 Reflexos."},
        ],
        "criacao": {
            "info": "Requer origem Feto Amaldiçoado (Híbrido). Ao contrário da versão do Clã Kamo, não há custo em PV — o personagem cria sangue a partir de energia amaldiçoada.",
            "tags": ["Requer Origem", "Sem Custo em PV"],
        },
    },
    "mares_desastre": {
        "nome": "Marés do Desastre",
        "personagem": "Dagon",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Cria e controla água a partir de energia. Pode arrastar criaturas puxando a água criada.",
        "funcionamento_basico": [
            "Cria água real a partir de energia. Puxar água (ação bônus): arrasta criaturas junto.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Bala Áquea", "desc": "Ação Comum | 9m | Ataque (Pontaria/Feitiçaria): 1d10 impacto."},
            {"nivel": 0, "nome": "Criar Água", "desc": "Variável | 9m | Ação completa: área 3m esférica; ação comum: 1,5m esférica."},
            {"nivel": 1, "nome": "Inundar", "desc": "Ação Comum | 9m | Área 4,5m. TR Fortitude: 2d8 impacto; área coberta de água."},
            {"nivel": 1, "nome": "Laços d'Água", "desc": "Ação Comum | 12m | TR Reflexos: falha = Agarrado. TR Atletismo/turno para escapar."},
            {"nivel": 2, "nome": "Chicote da Maré", "desc": "Ação Comum | 12m | TR Fortitude: 6d8 impacto; falha = derrubada."},
            {"nivel": 2, "nome": "Onda de Varredura", "desc": "Ação Comum | Cone 6m | TR Fortitude: 4d8 força; área coberta de água."},
            {"nivel": 3, "nome": "Bolha Sufocante", "desc": "Ação Comum | 9m | Concentração. TR Reflexos (CD+4): presa na bolha, sufocação (mod.CON rodadas)."},
            {"nivel": 3, "nome": "Escudo de Água", "desc": "Ação Comum | Sustentada (2PE/rodada) | Apara ataque de criatura sozinha."},
            {"nivel": 4, "nome": "Compressão Total", "desc": "Ação Comum | 18m | TR Fortitude: 10d10 força; falha = Desorientado 4r + Confusa 3r."},
            {"nivel": 4, "nome": "Domo Aquoso", "desc": "Reação | Ao ser alvo de ataque: ergue domo (120 PV), nega dano. Domo permanece."},
            {"nivel": 5, "nome": "Maré do Desastre", "desc": "Ação Completa | Linha 24m × 4,5m | TR Fortitude: 9d12 força; falha = Atordoado 1 rodada. Área coberta de água em correnteza."},
            {"nivel": 5, "nome": "Expansão de Domínio: Horizonte Cativante", "desc": "Completa. Exterior 9m; interior ilha tropical 100m. Ambiental: movimento -3m para hostis no mar. Acerto Garantido: 6 criaturas marinhas/rodada."},
        ],
    },
    "milagres": {
        "nome": "Milagres",
        "personagem": "Haruta Shigemo",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Armazena pequenos milagres do cotidiano e os libera como sorte. Milagres = 1 + BT; recuperados após descanso longo.",
        "funcionamento_basico": [
            "Milagres = 1 + BT; todos recuperados após descanso longo. Visíveis como marcas abaixo dos olhos.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Milagre da Sorte", "desc": "Passiva. Recebe o talento 'Favorecido pela Sorte'."},
            {"nivel": 1, "nome": "Por Pouco", "desc": "Reação | Nega 1 ataque. Custo: 1 milagre."},
            {"nivel": 2, "nome": "Sucesso Milagroso", "desc": "Reação | Próxima rolagem = valor máximo do dado (20 em 1d20, etc.). Custo: 2 milagres."},
            {"nivel": 3, "nome": "Coincidência Forçada", "desc": "Ação Completa | Recebe 2 milagres (descreve o milagre; personagem esquece depois)."},
            {"nivel": 4, "nome": "Milagre Inacreditável", "desc": "Reação | Ao ir morrer/ser gravemente debilitado: evita através de evento inacreditável. Custo: 5 milagres."},
            {"nivel": 5, "nome": "Milagroso", "desc": "Passiva. Máximo PE -10; mas +3 milagres por descanso longo."},
        ],
        "criacao": {
            "info": "Começa com o talento 'Favorecido pela Sorte' automaticamente. Milagres disponíveis = 1 + BT, recuperados após descanso longo.",
            "tags": ["Talento Automático"],
        },
    },
    "nulificacao_tecnicas": {
        "nome": "Nulificação de Técnicas",
        "personagem": "Anjo",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Anula o jujutsu. Passa livremente por barreiras e cortinas. Auréola e asas permitem voo.",
        "funcionamento_basico": [
            "Passa livremente por barreiras e cortinas. Recebe auréola e asas (voo).",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Criar Luz", "desc": "Variável | 9m | Duração 10 min. Cria luz forte; pode assumir formato de objetos pequenos ou orbes."},
            {"nivel": 0, "nome": "Flecha Radiante", "desc": "Ação Comum | 9m | 1 maldição. Ataque: 1d10 radiante."},
            {"nivel": 0, "nome": "Graciosidade Angelical", "desc": "Passiva. +3m voo; vantagem em Persuasão ou Performance (à escolha)."},
            {"nivel": 0, "nome": "Proteção Divina", "desc": "Ação Comum | 9m | 3 criaturas. Concentração (1PE/rodada). +1d4 em TR contra energia amaldiçoada."},
            {"nivel": 1, "nome": "Amarras Sagradas", "desc": "Ação Comum | 12m | 1 maldição. TR Fortitude: falha = Agarrado + 1d10 radiante/turno."},
            {"nivel": 1, "nome": "Arma Celeste", "desc": "Ação Bônus | Sustentada (1PE/rodada) | Arma: +1d10 radiante contra maldições."},
            {"nivel": 1, "nome": "Armadura Sacra", "desc": "Passiva. RD 4 contra dano de energia amaldiçoada. Máximo PE -2."},
            {"nivel": 1, "nome": "Rejeitar o Pecado", "desc": "Passiva. +2 em TR contra efeitos de energia amaldiçoada; +1 nos níveis 10 e 20. Máximo PE -2."},
            {"nivel": 1, "nome": "Véu Abençoado", "desc": "Ação Comum | 12m | 2 criaturas recebem 2d6 PV temporários."},
            {"nivel": 2, "nome": "Cruz Celeste", "desc": "Ação Comum | 18m | 1 maldição. TR Reflexos: 4d8 radiante; falha = Amedrontado 1 rodada."},
            {"nivel": 2, "nome": "Guarda de Querubins", "desc": "Ação Comum | Sustentada (1PE/rodada) | 3 querubins em aliados em 12m: +2 CA e +2 RD/querubim."},
            {"nivel": 2, "nome": "Purificar", "desc": "Ação Comum | Toque | Remove 1 condição causada por energia amaldiçoada."},
            {"nivel": 3, "nome": "Dissipar o Maldito", "desc": "Ação Completa | 24m | Área 6m. Dissipa barreiras, cortinas, habilidades concentradas/sustentadas. Expansão: vulnerável 1 rodada."},
            {"nivel": 3, "nome": "Explosão Luminosa", "desc": "Ação Comum | 24m | Área 9m. Maldições: TR Fortitude: 2d12 radiante; falha = Cego 1 rodada."},
            {"nivel": 3, "nome": "O Som da Salvação", "desc": "Ação Comum | Área 6m | Aliados: 4d10 PV temporários + mod. principal em 3 rolagens."},
            {"nivel": 4, "nome": "Melodia da Purificação", "desc": "Ação Comum | 24m | Área 9m. Maldições: TR Fortitude: 2d10 radiante; falha = Fragilizado + Exposto 2r."},
            {"nivel": 4, "nome": "O Peso Avassalador do Pecado", "desc": "Ação Comum | 30m | 1 maldição. TR Vontade: sucesso = Amedrontado + Desorientado; falha = + Fragilizado + Paralisado."},
            {"nivel": 5, "nome": "Escada de Jacó", "desc": "Ação Completa | 30m | Cilindro 18m. Dissipa toda estrutura de energia. Maldição: TR Fortitude: 4d12 radiante (ignora imunidade/RD)."},
            {"nivel": 5, "nome": "Jardim de Éden", "desc": "Ação Comum | 18m | Área 12m. Sustentada (2PE/rodada). Maldições não entram voluntariamente; energia amaldiçoada não funciona dentro."},
        ],
        "criacao": {
            "info": "Recebe auréola e asas passivas ao criar o personagem, concedendo voo (+3m movimento de voo). Passa livremente por barreiras e cortinas de energia amaldiçoada.",
            "tags": ["Voo Passivo", "Poder Passivo"],
        },
    },
    "plantas_desastre": {
        "nome": "Plantas do Desastre",
        "personagem": "Hanami",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Forma e controla flora amaldiçoada variada, física ou telepaticamente.",
        "funcionamento_basico": [
            "Cria e controla flora amaldiçoada; surge do corpo ou telepaticamente.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Absorção Vital", "desc": "Passiva. Descanso curto: metade BT em PE temporários. Descanso longo: BT PE temporários. 1×/descanso: absorve vida de plantas (+BT PE)."},
            {"nivel": 0, "nome": "Criar Plantas", "desc": "Variável | 9m | Cria plantas à vontade; tamanho/formato livre; controle telepático."},
            {"nivel": 1, "nome": "Disparo de Ramo", "desc": "Ação Comum | 12m | Ataque (Feitiçaria/Pontaria): 4d8 perfurante."},
            {"nivel": 1, "nome": "Revestimento de Espinhos", "desc": "Ação Comum | 3m | Sustentada (1PE/rodada). Arma: +1d10 perfurante; armadura: atacante recebe 2d6 perfurante."},
            {"nivel": 2, "nome": "Bolas de Madeira", "desc": "Variável | 12m | Ação completa: 3; comum: 2; bônus: 1. Por bola: TR Reflexos: 4d8 impacto (metade)."},
            {"nivel": 2, "nome": "Prisão de Raízes", "desc": "Ação Comum | 12m | TR Fortitude: 5d8 perfurante; falha = Agarrado (TR no fim do turno para escapar)."},
            {"nivel": 3, "nome": "Brotos Malditos", "desc": "Ação Comum | 12m | 2 criaturas. TR Reflexos: falha = broto fixo. Com broto: -1d8 PV/PE gasto; ação comum para remover."},
            {"nivel": 3, "nome": "Campo Florido", "desc": "Ação Comum | 18m | Área 9m. Sustentada (2PE/rodada). Criatura agressiva: TR Vontade → falha = pacificada (perde ação)."},
            {"nivel": 4, "nome": "Bonecos de Madeira", "desc": "Variável | 9m | Ação completa: 4; comum: 3; bônus: 2. PV80 CA16 | +14, 2d10+10 impacto. Agem autônomamente."},
            {"nivel": 4, "nome": "Emergência das Raízes", "desc": "Ação Comum | Cone 12m | TR Reflexos: 12d8 perfurante; falha = Imóvel (Acrobacia/Atletismo vs CD para escapar)."},
        ],
    },
    "projecao": {
        "nome": "Projeção",
        "personagem": "Naobito Zenin",
        "tipo": "Técnica Herdada",
        "req_origem": "herdado_zenin",
        "descricao": "Divide 1 segundo em 24 quadros; traça movimentos pré-determinados. Tudo tocado deve seguir a regra dos 24 quadros ou fica congelado.",
        "funcionamento_basico": [
            "Visão divide o mundo em 24 quadros; ao ativar, traça conjunto de movimentos imutável.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Movimento em 24 Quadros", "desc": "Passiva. Movimento +3m. Ao se mover: criatura tentando ataque de oportunidade deve TR Reflexos (falha = ataque cancelado)."},
            {"nivel": 0, "nome": "Reflexos Apurados", "desc": "Passiva. +2 em Reflexos."},
            {"nivel": 1, "nome": "Conjunto de Movimentos Rápidos", "desc": "Ação Completa | Move todo o movimento; ação comum e bônus disponíveis durante. Atacar: alvo desprevenido em falha. Reação inimiga: TR Reflexos ou perde."},
            {"nivel": 1, "nome": "Acúmulo de Velocidade", "desc": "Reação | Sustentada (1PE/turno) | 1×/rodada ao se mover: +3m; +1,5m/turno subsequente. Máx = mod.DEX acúmulos."},
            {"nivel": 2, "nome": "Movimentação Superior", "desc": "Passiva. 2 ações de movimento por turno. Máximo PE -4."},
            {"nivel": 2, "nome": "Congelamento Defensivo", "desc": "Reação | Ao ser atacado: Reflexos vs resultado. Sucesso: cancela + congela atacante; em área: Reflexos vs TR."},
            {"nivel": 3, "nome": "Movimento Ilegível", "desc": "Passiva. CD das habilidades de técnica +3. Máximo PE -6."},
            {"nivel": 3, "nome": "Tempo de Reação Acelerado", "desc": "Passiva. 2 reações por rodada. Máximo PE -6."},
            {"nivel": 3, "nome": "Congelamento Destrutivo", "desc": "Ação Bônus | Sustentada (2PE/turno) | Ao atacar: TR Reflexos; falha = acerto garantido + Paralisado durante o ataque."},
        ],
        "criacao": {
            "info": "Requer origem Herdado Zenin. Concede +2 em Reflexos e +3m de movimento passivos desde o 1° nível.",
            "tags": ["Requer Origem", "Bônus Passivo"],
        },
    },
    "proporcoes": {
        "nome": "Proporções",
        "personagem": "Kento Nanami",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Divide o alvo em linhas forçando um ponto fraco na proporção 7:3, aumentando o dano dos ataques nesse ponto.",
        "funcionamento_basico": [
            "Marca alvo com linhas divididas em 10; ponto fraco em 7:3 amplifica o dano.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Dividir Proporção", "desc": "Ação Bônus | 9m | 1 criatura (dura 1 ataque). -2 acerto → acerto: +1d8 +2 dano."},
            {"nivel": 1, "nome": "Proporção Destruidora", "desc": "Ação Bônus | 12m | Dura 2 ataques. -4 acerto → acerto: +2d6 +4 dano; crítico -1; some após 2 acertos."},
            {"nivel": 2, "nome": "Divisão Rápida", "desc": "Passiva. mod.técnica × /descanso longo: usa Proporção como ação livre. Máximo PE -4."},
            {"nivel": 2, "nome": "Proporção Letal", "desc": "Ação Bônus | 12m | Dura 2 ataques. -6 acerto → acerto: +3d8 +6 dano; crítico -1."},
            {"nivel": 2, "nome": "Letalidade Proporcional", "desc": "Passiva. Golpes em proporção ignoram RD = dobro BT. Máximo PE -4."},
            {"nivel": 3, "nome": "Proporção Específica", "desc": "Ação Bônus | 12m | 1 membro. -8 acerto → acerto: membro completamente destruído + +2d10 dano."},
            {"nivel": 3, "nome": "Colapso", "desc": "Ação Comum | Corpo-a-corpo | Área 9m. Golpe no ponto escolhido; área colapsada. TR Reflexos: 12d8 impacto; terreno difícil."},
        ],
    },
    "santuario": {
        "nome": "Santuário",
        "personagem": "Ryomen Sukuna",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Produz cortes invisíveis: Clivar (adapta-se à CON do alvo) e Desmantelar (projétil cortante à distância).",
        "funcionamento_basico": [
            "Dois tipos de corte: Clivar (toque, escala com CON do alvo) e Desmantelar (ataque de técnica à distância).",
            "Expansão de Domínio Sem Barreiras: raio 200m.",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Clivar (Nível 0)", "desc": "Ação Comum | Toque | TR Fortitude: 2d10 cortante (metade). Adapta-se à resistência."},
            {"nivel": 0, "nome": "Desmantelar (Nível 0)", "desc": "Ação Comum | 9m | Ataque (Pontaria/Feitiçaria): 1d10 cortante invisível."},
            {"nivel": 1, "nome": "Clivar (Nível 1)", "desc": "Ação Comum | Toque | TR Fortitude: 3d8 + 1d8/ponto mod.CON do alvo (máx 2 dados adicionais)."},
            {"nivel": 1, "nome": "Desmantelar (Nível 1)", "desc": "Ação Comum | 12m | Ataque: 4d8 cortante."},
            {"nivel": 1, "nome": "Destruição Máxima", "desc": "Passiva. Dano em estruturas/objetos = vulnerabilidade. Máximo PE -2."},
            {"nivel": 2, "nome": "Clivar (Nível 2)", "desc": "Ação Comum | Toque | TR Fortitude: 6d8 + 1d8/mod.CON (máx 4 dados adicionais)."},
            {"nivel": 2, "nome": "Desmantelar (Nível 2)", "desc": "Ação Comum | 18m | Ataque: 8d8 cortante."},
            {"nivel": 2, "nome": "Desmantelar Imperceptível", "desc": "Passiva. +3 acerto em Desmantelar. Máximo PE -4."},
            {"nivel": 3, "nome": "Clivar (Nível 3)", "desc": "Ação Comum | Toque | TR Fortitude: 10d8 + 1d8/mod.CON (máx 6 dados adicionais)."},
            {"nivel": 3, "nome": "Desmantelar (Nível 3)", "desc": "Ação Comum | 24m | Ataque: 14d8 cortante."},
            {"nivel": 3, "nome": "Teia de Aranha", "desc": "Ação Comum | Toque | Área 4,5m. Clivar no chão; área destruída + terreno difícil. Criaturas acima = dano de queda."},
            {"nivel": 3, "nome": "Corte Ampliado", "desc": "Passiva. Ao usar Desmantelar: reação para +2 alvos adjacentes (metade do custo cada). BT × /cena. Máximo PE -6."},
            {"nivel": 3, "nome": "Corte Rápido", "desc": "Passiva. Ao usar habilidade: reação (metade custo) para usar novamente no mesmo alvo. BT × /cena. Máximo PE -6."},
            {"nivel": 4, "nome": "Clivar (Nível 4)", "desc": "Ação Comum | Toque | TR Fortitude: 13d10 + 1d10/mod.CON (máx 6 dados adicionais)."},
            {"nivel": 4, "nome": "Desmantelar (Nível 4)", "desc": "Ação Comum | 30m | Ataque: 16d10 cortante."},
            {"nivel": 4, "nome": "Decepar", "desc": "Ação Comum | 15m | Ataque: 8d10 cortante. TR Fortitude: perde membro selecionado."},
            {"nivel": 4, "nome": "Cortes Verdadeiros", "desc": "Passiva. Habilidades de corte ignoram imunidade (reduz para resistência). Máximo PE -8."},
            {"nivel": 5, "nome": "Clivar (Nível 5)", "desc": "Ação Comum | Toque | TR Fortitude: 14d12 + 1d12/mod.CON (máx 10 dados adicionais)."},
            {"nivel": 5, "nome": "Desmantelar (Nível 5)", "desc": "Ação Comum | 48m | Ataque: 20d12 cortante."},
            {"nivel": 5, "nome": "Expansão de Domínio: Santuário Malevolente", "desc": "Sem Barreiras. Raio 200m. Cortes Incessantes (1×/rodada como ação livre). Amplificação: -3 RD. Acerto Garantido: alcance = toda a expansão."},
        ],
    },
    "sentenca_mortal": {
        "nome": "Sentença Mortal",
        "personagem": "Hiromi Higuruma",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Julgamento em expansão de domínio com sentenças criminais mecânicas. No nível 4 de personagem, recebe Expansão Completa.",
        "funcionamento_basico": [
            "No 1° nível: recebe Martelo da Justiça + invocação Juiz.",
            "No 4° nível: recebe Expansão de Domínio Completa (custo 10PE).",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Martelo da Justiça", "desc": "Ação Bônus | Até dissipar. Cria martelo de madeira. Ação bônus: muda para qualquer arma corpo-a-corpo custo 1."},
            {"nivel": 0, "nome": "Juiz (Invocação)", "desc": "Invocação [4° Grau, 2PE] PV15 CA14 Mov6m | INT12 SAB16. Conhecimento do Juiz: sabe tudo dentro do domínio. Perícias: Astúcia+5, Intuição+5, Percepção+5."},
            {"nivel": 1, "nome": "Laçar", "desc": "Ação Comum | 12m | Martelo fluído: TR Reflexos → falha = Agarrado (TR Atletismo para escapar)."},
            {"nivel": 2, "nome": "Esmagar", "desc": "Ação Comum | 3m | TR Reflexos: 4d8 impacto; falha = Caído + esmagado (TR Fortitude/turno = 3d8)."},
            {"nivel": 2, "nome": "Controle Superior", "desc": "Passiva. Invocar/trocar forma = ação livre; pode usar armas custo 2. Martelo = ferramenta amaldiçoada (máx 1° grau). Máximo PE -4."},
            {"nivel": 4, "nome": "Expansão de Domínio: Sentença de Morte", "desc": "Completa (10PE). Tribunal com guilhotinas. Juiz anuncia acusações → julgamento → sentença (Confisco de técnica, Pena de Morte, ou ambos)."},
        ],
        "criacao": {
            "info": "Ao 1° nível: recebe automaticamente o Martelo da Justiça e a invocação Juiz (4° Grau). Ao 4° nível de personagem: recebe Expansão de Domínio Completa (custo 10PE).",
            "tags": ["Invocação Inicial", "Arma Automática"],
        },
    },
    "transfiguracao_inerte": {
        "nome": "Transfiguração Inerte",
        "personagem": "Mahito",
        "tipo": "Técnica Inata",
        "req_origem": None,
        "descricao": "Distorce almas transfigurando corpos (próprio e alheio). Causa dano na alma.",
        "funcionamento_basico": [
            "Remodelação da alma reflete no corpo. Transformações duram até revertidas (ação livre).",
        ],
        "habilidades": [
            {"nivel": 0, "nome": "Braços de Espinho", "desc": "Ação Bônus | Ataques desarmados: 1d6 perfurante + alcance +1,5m."},
            {"nivel": 0, "nome": "Pernas de Animal", "desc": "Ação Bônus | Movimento +3m."},
            {"nivel": 0, "nome": "Toque Transfigurador", "desc": "Ação Comum | Toque | Civil: TR Integridade (falha = zero). Feiticeiro/maldição: 1d6 dano na alma. Requer ataque em combate."},
            {"nivel": 1, "nome": "Criar Asas", "desc": "Ação Bônus | Movimento padrão torna-se movimento de voo."},
            {"nivel": 1, "nome": "Lâminas Corporais", "desc": "Ação Bônus | Ataques desarmados: 2d6 cortante + alcance +1,5m."},
            {"nivel": 1, "nome": "Transfiguração Aprimorada", "desc": "Passiva. Toque Transfigurador: 1d6→1d10 + soma mod. atributo de técnica. Máximo PE -2."},
            {"nivel": 2, "nome": "Devastar", "desc": "Ação Comum | Cone 4,5m | TR Reflexos: 4d8 impacto (metade)."},
            {"nivel": 2, "nome": "Encolher e Fugir", "desc": "Reação | Ao ser atacado corpo-a-corpo: Reflexos vs ataque; sucesso = ignora ataque. Move metade do movimento para longe."},
            {"nivel": 2, "nome": "Restaurar Corpo", "desc": "Ação Comum | Recupera 6d6 PV."},
            {"nivel": 2, "nome": "Repelir Corpo: Liberação Caótica", "desc": "Ação Comum | 12m | Req: 4 humanos transfigurados. 2 alvos. TR Reflexos: 4d8 físico/alvo (metade)."},
            {"nivel": 3, "nome": "Restauração Avançada", "desc": "Ação Comum | Recupera 3d12 PV + restaura qualquer membro quebrado/decepado."},
            {"nivel": 3, "nome": "Repelir Corpo: Concentração", "desc": "Ação Comum | 18m | Req: 3 humanos transfigurados. TR Reflexos: 10d8 físico; +3d8 por extra (máx 2)."},
            {"nivel": 3, "nome": "Transfiguração Devastadora", "desc": "Passiva. Toque Transfigurador: 1d10→3d6. Máximo PE -6. Requer: Transfiguração Aprimorada."},
            {"nivel": 4, "nome": "Dividir-se", "desc": "Ação Completa | Cria clone com metade dos PV/PE gastos. Turno próprio; usa habilidades de técnica apenas em si mesmo."},
            {"nivel": 4, "nome": "Alma Polimórfica Isômera", "desc": "Variável | 9m | Req: 4 humanos transfigurados + 5PE/corpo. Ação completa: 3 corpos. PV50 CA24 | +21, 4d8+14 impacto."},
            {"nivel": 5, "nome": "Regeneração Absoluta", "desc": "Ação Comum | Sustentada (metade do custo/rodada) | Todo dano recebido reduzido à metade (exceto na alma)."},
            {"nivel": 5, "nome": "Transfiguração Máxima", "desc": "Passiva. Toque Transfigurador: 3d6→3d10 + dobro do mod. Máximo PE -10. Requer: Transfiguração Devastadora."},
            {"nivel": 5, "nome": "Expansão de Domínio: Auto-Personificação da Perfeição", "desc": "Completa. Área 9m. Mãos gigantes em forma de flor. Amplificação: CD transfiguração +2. Acerto Garantido: transfiguração afeta todas as criaturas."},
        ],
    },
    "trem_puro_amor": {
        "nome": "Trem do Puro Amor",
        "personagem": "Kinji Hakari",
        "tipo": "Técnica Amaldiçoada",
        "req_origem": None,
        "descricao": "Baseada em pachinko; a expansão de domínio é o núcleo. No Jackpot (3 iguais em 3d6), PE voltam ao máximo todo turno por 5 rodadas.",
        "funcionamento_basico": [
            "No 4° nível: recebe Expansão de Domínio Completa (10PE).",
            "Jackpot: PE ao máximo no início de cada turno por 5 rodadas. Regeneração e energia reversa disponíveis.",
        ],
        "habilidades": [
            {"nivel": 1, "nome": "Indicador: Bola", "desc": "Ação Comum | 12m | Pontaria: 4d8 impacto. Dentro da expansão: rola 1d20 para pontos de expectativa."},
            {"nivel": 1, "nome": "Indicador: Portas", "desc": "Ação Comum | 12m | TR Reflexos: falha = Agarrado (TR Atletismo vs CD para escapar). Gera expectativa."},
            {"nivel": 4, "nome": "Expansão de Domínio: Aposta Mortal Indolente", "desc": "Completa (10PE). Mecânica de Pachinko: indicadores geram expectativa → 1d20 → pontos → Evento Riichi (1d100) → 3d6 → JACKPOT (três iguais). Jackpot: PE máximo/turno por 5r."},
        ],
        "criacao": {
            "info": "Ao 4° nível de personagem, recebe automaticamente a Expansão de Domínio Completa (10PE). Ao atingir Jackpot (três resultados iguais em 3d6), PE voltam ao máximo a cada turno por 5 rodadas.",
            "tags": ["Expansão ao Nv.4"],
        },
    },
}
