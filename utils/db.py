import sqlite3
def init_db():
    conn=sqlite3.connect("fitness.db")
    c=conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS habits(date TEXT, workout INTEGER)")
    conn.commit()
    conn.close()
