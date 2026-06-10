import sqlite3

def init_db():
    conn = sqlite3.connect("support.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            query TEXT,
            response TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_data(query, response):
    conn = sqlite3.connect("support.db")
    c = conn.cursor()
    c.execute("INSERT INTO logs VALUES (?, ?)", (query, response))
    conn.commit()
    conn.close()