import sqlite3 as sq
from data_users import info_users

with sq.connect('saper.db') as con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
    sex INTEGER NOT NULL DEFAULT 1, old INTEGER,
    score INTEGER
    )""")
    #cur.execute("INSERT INTO users VALUES (1, 'Один', 1, 43, 59494)")
    #cur.execute("INSERT INTO users VALUES (2, 'Версаче', 1, 61, 5554)")
    #cur.execute("INSERT INTO users VALUES (3, 'Кравильда', 2, 15, 765)")
    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)