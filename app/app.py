import json
import sys
import os

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

# Garante que o diretório app/ está no path para imports relativos
sys.path.insert(0, os.path.dirname(__file__))

from database import get_db, init_db, login_required, usuario_logado, gerar_codigo_mesa
from sistemas.jujutsu.routes import calcular_ficha as jujutsu_calcular_ficha
from sistemas.jujutsu.game_data import ESPECIALIZACOES as JJ_ESPECIALIZACOES, calcular_grau as jujutsu_calcular_grau
from sistemas.old_dragon.routes import calcular_ficha as od_calcular_ficha
from sistemas.dnd.routes import calcular_ficha as dnd_calcular_ficha
from sistemas.cthulhu.routes import calcular_ficha as coc_calcular_ficha

app = Flask(__name__)
app.secret_key = "feiticeiros_maldicoes_2025"

# Registrar blueprints de cada sistema
from sistemas.jujutsu import bp as jujutsu_bp
from sistemas.old_dragon import bp as old_dragon_bp
from sistemas.dnd import bp as dnd_bp
from sistemas.cthulhu import bp as cthulhu_bp

app.register_blueprint(jujutsu_bp)
app.register_blueprint(old_dragon_bp)
app.register_blueprint(dnd_bp)
app.register_blueprint(cthulhu_bp)

init_db()


# ─── ROTAS COMPARTILHADAS ──────────────────────────────────────────────────────

@app.route("/")
def index():
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


# ─── AUTH ──────────────────────────────────────────────────────────────────────

@app.route("/login", methods=["GET", "POST"])
def login():
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with get_db() as conn:
            user = conn.execute("SELECT * FROM usuarios WHERE username=?", (username,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["usuario_id"] = user["id"]
            session["usuario_nome"] = user["username"]
            return redirect(url_for("dashboard"))
        flash("Usuário ou senha inválidos.", "error")
    return render_template("login.html")


@app.route("/registrar", methods=["GET", "POST"])
def registrar():
    if "usuario_id" in session:
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm  = request.form.get("confirm", "")
        if not username or not password:
            flash("Preencha todos os campos.", "error")
        elif password != confirm:
            flash("As senhas não conferem.", "error")
        elif len(password) < 4:
            flash("Senha deve ter ao menos 4 caracteres.", "error")
        else:
            try:
                with get_db() as conn:
                    conn.execute(
                        "INSERT INTO usuarios (username, password_hash) VALUES (?, ?)",
                        (username, generate_password_hash(password))
                    )
                    conn.commit()
                flash("Conta criada! Faça login.", "success")
                return redirect(url_for("login"))
            except sqlite3.IntegrityError:
                flash("Esse nome de usuário já existe.", "error")
    return render_template("registrar.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ─── DASHBOARD ──────────────────────────────────────────────────────────────────

@app.route("/dashboard")
@login_required
def dashboard():
    uid = session["usuario_id"]
    with get_db() as conn:
        mesas_mestre = conn.execute(
            "SELECT * FROM mesas WHERE mestre_id=? ORDER BY criado_em DESC", (uid,)
        ).fetchall()
        mesas_player = conn.execute("""
            SELECT m.*, p.nome as nome_personagem, p.id as pid
            FROM mesas m
            JOIN personagens p ON p.mesa_id = m.id AND p.usuario_id = ?
            WHERE m.mestre_id != ?
        """, (uid, uid)).fetchall()
    return render_template("dashboard.html",
                           mesas_mestre=mesas_mestre,
                           mesas_player=mesas_player,
                           usuario=usuario_logado())


# ─── MESAS ──────────────────────────────────────────────────────────────────────

@app.route("/mesa/criar", methods=["GET", "POST"])
@login_required
def criar_mesa():
    uid = session["usuario_id"]
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        sistema = request.form.get("sistema", "jujutsu")
        if not nome:
            flash("Nome da mesa é obrigatório.", "error")
        else:
            codigo = gerar_codigo_mesa()
            with get_db() as conn:
                conn.execute(
                    "INSERT INTO mesas (codigo, nome, sistema, mestre_id) VALUES (?, ?, ?, ?)",
                    (codigo, nome, sistema, uid)
                )
                conn.commit()
            return redirect(url_for("ver_mesa", codigo=codigo))
    return render_template("criar_mesa.html", usuario=usuario_logado())


@app.route("/mesa/entrar", methods=["GET", "POST"])
@login_required
def entrar_mesa():
    if request.method == "POST":
        codigo = request.form.get("codigo", "").strip().upper()
        with get_db() as conn:
            mesa = conn.execute("SELECT * FROM mesas WHERE codigo=?", (codigo,)).fetchone()
        if not mesa:
            flash("Mesa não encontrada. Verifique o código.", "error")
        else:
            return redirect(url_for("ver_mesa", codigo=codigo))
    return render_template("entrar_mesa.html", usuario=usuario_logado())


_ROTAS_PERSONAGEM = {
    "jujutsu":    "jujutsu.ver_personagem",
    "old_dragon": "old_dragon.ver_personagem",
    "dnd":        "dnd.ver_personagem",
    "cthulhu":    "cthulhu.ver_personagem",
}

_ROTAS_CRIAR = {
    "jujutsu":    "jujutsu.criar",
    "old_dragon": "old_dragon.criar",
    "dnd":        "dnd.criar",
    "cthulhu":    "cthulhu.criar",
}


def _url_personagem(sistema, pid):
    rota = _ROTAS_PERSONAGEM.get(sistema, "jujutsu.ver_personagem")
    return url_for(rota, pid=pid)


def _url_criar(sistema):
    return url_for(_ROTAS_CRIAR.get(sistema, "jujutsu.criar"))


_CALCULAR_FICHA = {
    "jujutsu":    jujutsu_calcular_ficha,
    "old_dragon": od_calcular_ficha,
    "dnd":        dnd_calcular_ficha,
    "cthulhu":    coc_calcular_ficha,
}


def _resumo_personagem_mesa(sistema, dados):
    """Extrai campos de resumo para exibição na mesa, por sistema."""
    calc_fn = _CALCULAR_FICHA.get(sistema, jujutsu_calcular_ficha)
    dados = calc_fn(dict(dados))
    calc = dados.get("calculado", {})

    if sistema == "jujutsu":
        return {
            "nivel": dados.get("nivel", 1),
            "subtitulo": JJ_ESPECIALIZACOES.get(dados.get("especializacao", ""), {}).get("nome", "?"),
            "grau": jujutsu_calcular_grau(dados.get("nivel", 1)),
            "pv_max": calc.get("pv_max", "?"),
            "recurso_max": calc.get("pe_max", "?"),
            "recurso_label": calc.get("pe_label", "PE"),
        }
    elif sistema in ("old_dragon", "dnd"):
        from sistemas.old_dragon.game_data import CLASSES as OD_CLASSES
        from sistemas.dnd.game_data import CLASSES as DND_CLASSES
        classes = OD_CLASSES if sistema == "old_dragon" else DND_CLASSES
        return {
            "nivel": dados.get("nivel", 1),
            "subtitulo": classes.get(dados.get("classe", ""), {}).get("nome", "?"),
            "grau": f"Nv {dados.get('nivel', 1)}",
            "pv_max": calc.get("pv_max", "?"),
            "recurso_max": None,
            "recurso_label": None,
        }
    elif sistema == "cthulhu":
        return {
            "nivel": "—",
            "subtitulo": dados.get("ocupacao", "?"),
            "grau": "Investigador",
            "pv_max": calc.get("pv_max", "?"),
            "recurso_max": dados.get("san_atual", calc.get("san_inicial", "?")),
            "recurso_label": "SAN",
        }
    return {"nivel": "?", "subtitulo": "?", "grau": "?", "pv_max": "?", "recurso_max": None, "recurso_label": None}


@app.route("/mesa/<codigo>")
@login_required
def ver_mesa(codigo):
    uid = session["usuario_id"]
    with get_db() as conn:
        mesa = conn.execute("SELECT * FROM mesas WHERE codigo=?", (codigo,)).fetchone()
        if not mesa:
            flash("Mesa não encontrada.", "error")
            return redirect(url_for("dashboard"))
        personagens_mesa = conn.execute(
            "SELECT p.*, u.username FROM personagens p JOIN usuarios u ON p.usuario_id=u.id WHERE p.mesa_id=?",
            (mesa["id"],)
        ).fetchall()
        meus = conn.execute(
            "SELECT id, nome FROM personagens WHERE usuario_id=? AND sistema=? AND (mesa_id IS NULL OR mesa_id=?)",
            (uid, mesa["sistema"], mesa["id"])
        ).fetchall()
        mestre = conn.execute("SELECT username FROM usuarios WHERE id=?", (mesa["mestre_id"],)).fetchone()

    chars_lista = []
    for p in personagens_mesa:
        dados = json.loads(p["dados"])
        resumo = _resumo_personagem_mesa(p["sistema"], dados)
        chars_lista.append({
            "id": p["id"],
            "nome": p["nome"],
            "username": p["username"],
            "eh_meu": p["usuario_id"] == uid,
            "url_ficha": _url_personagem(p["sistema"], p["id"]),
            **resumo,
        })

    meu_char_na_mesa = next((c for c in chars_lista if c["eh_meu"]), None)

    return render_template("mesa.html",
                           mesa=mesa,
                           mestre=mestre,
                           chars_lista=chars_lista,
                           meus_personagens=meus,
                           meu_char_na_mesa=meu_char_na_mesa,
                           eh_mestre=mesa["mestre_id"] == uid,
                           url_criar=_url_criar(mesa["sistema"]),
                           usuario=usuario_logado())


@app.route("/mesa/<codigo>/vincular/<int:pid>", methods=["POST"])
@login_required
def vincular_personagem(codigo, pid):
    uid = session["usuario_id"]
    with get_db() as conn:
        mesa = conn.execute("SELECT * FROM mesas WHERE codigo=?", (codigo,)).fetchone()
        if not mesa:
            return redirect(url_for("dashboard"))
        p = conn.execute("SELECT * FROM personagens WHERE id=? AND usuario_id=?", (pid, uid)).fetchone()
        if not p:
            flash("Personagem não encontrado.", "error")
            return redirect(url_for("ver_mesa", codigo=codigo))
        conn.execute(
            "UPDATE personagens SET mesa_id=NULL WHERE usuario_id=? AND mesa_id=?",
            (uid, mesa["id"])
        )
        conn.execute("UPDATE personagens SET mesa_id=? WHERE id=?", (mesa["id"], pid))
        conn.commit()
    return redirect(url_for("ver_mesa", codigo=codigo))


@app.route("/mesa/<codigo>/desvincular/<int:pid>", methods=["POST"])
@login_required
def desvincular_personagem(codigo, pid):
    uid = session["usuario_id"]
    with get_db() as conn:
        mesa = conn.execute("SELECT * FROM mesas WHERE codigo=?", (codigo,)).fetchone()
        if not mesa:
            return redirect(url_for("dashboard"))
        p = conn.execute("SELECT * FROM personagens WHERE id=? AND mesa_id=?", (pid, mesa["id"])).fetchone()
        if p and (p["usuario_id"] == uid or mesa["mestre_id"] == uid):
            conn.execute("UPDATE personagens SET mesa_id=NULL WHERE id=?", (pid,))
            conn.commit()
    return redirect(url_for("ver_mesa", codigo=codigo))


@app.route("/mesa/<codigo>/clonar/<int:pid>", methods=["POST"])
@login_required
def clonar_personagem(codigo, pid):
    uid = session["usuario_id"]
    with get_db() as conn:
        mesa = conn.execute("SELECT * FROM mesas WHERE codigo=?", (codigo,)).fetchone()
        if not mesa:
            return redirect(url_for("dashboard"))
        original = conn.execute("SELECT * FROM personagens WHERE id=? AND mesa_id=?", (pid, mesa["id"])).fetchone()
        if not original:
            flash("Personagem não encontrado na mesa.", "error")
            return redirect(url_for("ver_mesa", codigo=codigo))
        dados_clone = json.loads(original["dados"])
        nome_clone = dados_clone.get("nome", original["nome"]) + " (clone)"
        dados_clone["nome"] = nome_clone
        cursor = conn.execute(
            "INSERT INTO personagens (nome, dados, usuario_id, sistema, mesa_id) VALUES (?, ?, ?, ?, NULL)",
            (nome_clone, json.dumps(dados_clone, ensure_ascii=False), uid, mesa["sistema"])
        )
        clone_id = cursor.lastrowid
        conn.commit()
    return redirect(_url_personagem(mesa["sistema"], clone_id))


@app.route("/mesa/<codigo>/deletar", methods=["POST"])
@login_required
def deletar_mesa(codigo):
    uid = session["usuario_id"]
    with get_db() as conn:
        mesa = conn.execute("SELECT * FROM mesas WHERE codigo=? AND mestre_id=?", (codigo, uid)).fetchone()
        if mesa:
            conn.execute("UPDATE personagens SET mesa_id=NULL WHERE mesa_id=?", (mesa["id"],))
            conn.execute("DELETE FROM mesas WHERE id=?", (mesa["id"],))
            conn.commit()
    return redirect(url_for("dashboard"))


# ─── REDIRECT DE COMPATIBILIDADE ───────────────────────────────────────────────
# Mantém URLs antigas funcionando após a migração

@app.route("/sistema/jujutsu")
def sistema_jujutsu():
    return redirect(url_for("jujutsu.index"))

@app.route("/criar")
def criar_compat():
    return redirect(url_for("jujutsu.criar"))

@app.route("/personagem/<int:pid>")
def ver_personagem_compat(pid):
    with get_db() as conn:
        row = conn.execute("SELECT sistema FROM personagens WHERE id=?", (pid,)).fetchone()
    if not row:
        return redirect(url_for("dashboard"))
    return redirect(_url_personagem(row["sistema"], pid))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
