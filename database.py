import sqlite3

conn = sqlite3.connect("data/prestadores.db", check_same_thread=False)
cursor = conn.cursor()

def criar_tabelas():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prestadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        cidade TEXT,
        categoria TEXT,
        descricao TEXT,
        plano TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        cidade TEXT,
        pedido TEXT
    )
    """)

    conn.commit()
