import sqlite3

def create_connection():
    return sqlite3.connect("students.db")

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        lastname TEXT NOT NULL,
                        age INTEGER,
                        grade REAL)''')
    conn.commit()
    conn.close()