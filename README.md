# RPG Forger — Feiticeiros & Maldições

Aplicação web para criação e gerenciamento de fichas de personagem do sistema **Feiticeiros & Maldições** (F&M), um RPG de mesa baseado no universo de Jujutsu Kaisen.

---

## Objetivo

Substituir fichas de papel por uma ficha digital interativa que:

- Guia o jogador passo a passo na criação do personagem
- Calcula automaticamente todos os valores derivados (DEF, PV, PE, modificadores, bônus de treinamento)
- Permite gerenciar o personagem durante as sessões (level up, distribuição de atributos, notas)
- Suporta criação de invocações para personagens Controladores
- Exibe todas as informações de forma clara e organizada

---

## Stack

- **Backend:** Python 3 + Flask
- **Frontend:** HTML + CSS (tema escuro customizado) + JavaScript vanilla
- **Banco de dados:** SQLite (arquivo `personagens.db`)
- **Autenticação:** sessão Flask simples por login/senha

---

## Estrutura

```
app/
├── app.py              # Rotas Flask e lógica de negócio
├── game_data.py        # Toda a data do sistema (perícias, especializações, origens, armas, kits…)
├── personagens.db      # SQLite — criado automaticamente na primeira execução
├── static/
│   └── css/style.css   # Folha de estilos principal
└── templates/
    ├── base.html
    ├── index.html              # Login / home
    ├── criar_passo1.html       # Wizard passo 1: Identidade + atributos
    ├── criar_passo2.html       # Wizard passo 2: Origem / clã
    ├── criar_passo3.html       # Wizard passo 3: Especialização + perícias
    ├── criar_passo4.html       # Wizard passo 4: Equipamento (uniforme + kit)
    ├── criar_passo5.html       # Wizard passo 5: Revisão final
    ├── ficha.html              # Ficha completa do personagem
    ├── criar_invocacao.html    # Criação / edição de invocação
    └── invocacoes.html         # Lista de invocações do personagem
```

---

## Como rodar

```bash
cd app
pip install flask
python app.py
```

Acesse `http://localhost:5000`.

---

## Criação de Personagem (Wizard 5 passos)

| Passo | O que define |
|-------|-------------|
| 1 — Identidade | Nome, jogador, técnica inata, domínio, distribuição de atributos (point buy) |
| 2 — Origem | Clã/origem (inato, herdado, restringido, sem técnica…), bônus de atributos, perícias do clã |
| 3 — Especialização | Lutador, Especialista de Combate, Especialista em Técnica, Controlador, Suporte ou Restringido; atributo-chave, teste de resistência, perícias |
| 4 — Equipamento | Uniforme (Comum / Leve / Médio / Robusto / Sob Medida) + Kit de ferramentas |
| 5 — Revisão | Confirma tudo e salva o personagem |

---

## Mecânicas implementadas

### Atributos
6 atributos: **Força, Destreza, Constituição, Inteligência, Sabedoria, Presença**
Modificador = `(valor − 10) / 2` (arredondado p/ baixo)

### Perícias (lista oficial p.284)
20 perícias, cada uma vinculada a um atributo.
`*T` = requer treinamento para usar plenamente: **Feitiçaria, Medicina, Ofício, Prestidigitação**

Graus de treinamento: **Nenhum** → **Treinado (+BT)** → **Mestre (+2×BT)**

### Defesa
`DEF = 10 + mod.DES + nível/2 + bônus do uniforme`

### Uniformes (p.140)
| Uniforme | Bônus DEF | Penalidade DES |
|----------|-----------|----------------|
| Comum | 0 | 0 |
| Revestimento Leve | +2 | 0 |
| Revestimento Médio | +4 | −2 |
| Revestimento Robusto | +6 | −4 |
| Sob Medida | +1 | 0 (+2 Acrobacia/Furtividade) |

### Kits de Ferramentas (p.142–144)
7 kits: Alfaiate, Alquimia, Canalizador, Cozinheiro, Entalhador, Ferreiro, Farmacêutico
Cada kit habilita o Ofício correspondente e permite criar itens específicos.

### Level Up
Ao subir de nível o personagem ganha PV, PE recuperado e pode distribuir pontos de atributo.

---

## Referência
Sistema baseado no livro **Feiticeiros & Maldições** (feit1.pdf + feit-2.pdf).
