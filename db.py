import os
import sqlite3
from contextlib import contextmanager

DB_URL = os.getenv("DB_URL", "corelia.db")

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_URL)
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agent TEXT,
            action TEXT,
            details TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        conn.commit()

def log_event(agent, action, details):
    with get_db() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO logs (agent, action, details) VALUES (?, ?, ?)", (agent, action, details))
        conn.commit()
