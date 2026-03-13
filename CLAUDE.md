# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the app
cd app && python3 app.py
# or
bash app/run.sh

# Install dependency (if Flask missing)
pip install flask --break-system-packages
```

Server runs at http://localhost:5000 with debug mode enabled.

There are no tests, linting configs, or build system yet.

## Architecture

**RPG-Forger** ("Feiticeiros & Maldições") is a Flask web app for managing digital character sheets in tabletop RPGs. Each RPG system is a self-contained Flask Blueprint under `app/sistemas/`.

### File Structure

```
app/
├── app.py                          # Thin core: auth, dashboard, mesas + blueprint registration
├── database.py                     # Shared: get_db, init_db, login_required, gerar_codigo_mesa
├── sistemas/
│   └── jujutsu/                    # Feiticeiros & Maldições system (Blueprint: /jujutsu)
│       ├── __init__.py             # Blueprint definition
│       ├── routes.py               # All jujutsu routes + calcular_ficha()
│       ├── game_data.py            # All game constants and calculation functions
│       └── templates/jujutsu/      # Jujutsu-specific templates (14 files)
├── templates/                      # Shared templates: base, login, dashboard, mesa
└── static/css/style.css            # Dark-theme CSS (shared)
```

> `app/game_data.py` and `app/templates/*.html` (jujutsu-specific) are legacy copies — they are no longer used and can be deleted.

### Adding a New RPG System

1. Create `app/sistemas/<nome>/` with `__init__.py` (Blueprint, `url_prefix="/<nome>"`), `routes.py`, `game_data.py`, and `templates/<nome>/`
2. Register the blueprint in `app/app.py`: `app.register_blueprint(nome_bp)`
3. Add the system to `_url_personagem()` and `_url_criar()` dicts in `app/app.py`

### Shared Core (`app/app.py`)

Routes: `/`, `/login`, `/registrar`, `/logout`, `/dashboard`, `/mesa/*`

`_url_personagem(sistema, pid)` and `_url_criar(sistema)` — dispatch character/creation URLs to the correct blueprint based on the `personagens.sistema` field.

Compatibility redirects: `/sistema/jujutsu`, `/criar`, `/personagem/<pid>` — keep old URLs working.

### Jujutsu Blueprint (`/jujutsu`)

| Route | Function |
|-------|----------|
| `GET /jujutsu/` | List characters |
| `GET /jujutsu/criar` → `POST /jujutsu/criar/passo2-5` → `POST /jujutsu/criar/salvar` | 5-step creation wizard |
| `GET /jujutsu/personagem/<pid>` | Character sheet |
| `GET/POST /jujutsu/personagem/<pid>/editar` | Edit |
| `POST /jujutsu/personagem/<pid>/subir_nivel` | Level up (JSON API) |
| `POST /jujutsu/personagem/<pid>/atualizar_pv` | HP/PE/XP update (JSON API) |
| `/jujutsu/personagem/<pid>/invocacoes/*` | Summons (controlador only) |
| `/jujutsu/personagem/<pid>/tecnicas/*` | Techniques |
| `/jujutsu/personagem/<pid>/aptidoes` | Abilities |
| `/jujutsu/personagem/<pid>/dominio` | Domain expansion |
| `POST /jujutsu/api/rolar_dados` | Dice roller |
| `GET /jujutsu/api/info_origem/<key>` | Origin data |
| `POST /jujutsu/api/invocacao_calc` | Summon stat calculator |

### Database Schema

Three tables: `usuarios`, `mesas` (game sessions), `personagens`.

Character data is stored entirely as JSON in `personagens.dados`. Key helpers in `routes.py`:
- `calcular_ficha(dados)` — recomputes all derived stats (DEF, PV, PE, modifiers); called after every edit
- `_get_personagem(pid)` / `_save_personagem(pid, dados)` — JSON deserialize/serialize helpers

### Game Data Layer (`sistemas/jujutsu/game_data.py`)

All constants: `ORIGENS`, `ESPECIALIZACOES`, `UNIFORMES`, `KITS`, `ARMAS_*`, `PERICIAS`, `ATRIBUTOS`, `INVOCACAO_*`, `TECNICA_*`, `APTIDOES_*`, `DOMINIO_TIPOS`

Calculation functions: `calcular_modificador()`, `calcular_pv()`, `calcular_pe()`, `calcular_invocacao()`

### Frontend

Minimal JavaScript (form prevention + textarea resize in `app.js`). Business logic is server-side. Templates use Jinja2 inheritance from `base.html`. JS `fetch()` calls in templates use `url_for()` to generate URLs rather than hardcoded paths.

## Known Issues

- Flask `secret_key` is hardcoded in `app.py` — do not commit a real secret
- Debug mode is on (`debug=True`) — disable for any production deployment
- No database migration system; schema changes are manual `ALTER TABLE` statements in `init_db()`
