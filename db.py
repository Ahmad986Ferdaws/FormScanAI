# app/db.py

import sqlite3

DB_FILE = \"forms.db\"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"\"\"
        CREATE TABLE IF NOT EXISTS forms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            raw_text TEXT,
            structured_json TEXT
        )
    \"\"\")
    conn.commit()
    conn.close()

def save_form(filename, raw_text, structured_json):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"INSERT INTO forms (filename, raw_text, structured_json) VALUES (?, ?, ?)\",
                   (filename, raw_text, structured_json))
    conn.commit()
    conn.close()

def get_form(form_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"SELECT * FROM forms WHERE id = ?\", (form_id,))
    row = cursor.fetchone()
    conn.close()
    return row

def get_all_forms():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(\"SELECT id, filename FROM forms\")
    rows = cursor.fetchall()
    conn.close()
    return rows
