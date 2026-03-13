import os
import sqlite3
from functools import wraps
import secrets
import string
from flask import session, redirect, url_for

DB_PATH = os.path.join(os.path.dirname(__file__), "personagens.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS mesas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE NOT NULL,
                nome TEXT NOT NULL,
                sistema TEXT NOT NULL DEFAULT 'jujutsu',
                mestre_id INTEGER NOT NULL,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS personagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                dados TEXT NOT NULL,
                usuario_id INTEGER,
                sistema TEXT DEFAULT 'jujutsu',
                mesa_id INTEGER,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        for col, definition in [
            ("usuario_id", "INTEGER"),
            ("sistema", "TEXT DEFAULT 'jujutsu'"),
            ("mesa_id", "INTEGER"),
        ]:
            try:
                conn.execute(f"ALTER TABLE personagens ADD COLUMN {col} {definition}")
            except Exception:
                pass
        conn.commit()


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "usuario_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated


def usuario_logado():
    return {"id": session.get("usuario_id"), "username": session.get("usuario_nome")}


def gerar_codigo_mesa():
    chars = string.ascii_uppercase + string.digits
    while True:
        code = "".join(secrets.choice(chars) for _ in range(6))
        with get_db() as conn:
            exists = conn.execute("SELECT id FROM mesas WHERE codigo=?", (code,)).fetchone()
        if not exists:
            return code
