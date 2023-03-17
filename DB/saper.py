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
    #cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)


with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users")
    result= cur.fetchall()
print(result)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE sex = 2")
    result= cur.fetchall()
print(result)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score<1000")
    result= cur.fetchall()
print(result)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score=(SELECT MAX(score) FROM users)")
    result= cur.fetchall()
print(result)

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE old BETWEEN 18 AND 20")
    result= cur.fetchall()
print(result)


with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE users SET old = 20 WHERE old = 19")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE users SET score=score+300 WHERE score < 1000")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE users SET score=score+100 WHERE old=20")

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE users SET score=score+1000 WHERE name LIKE 'Бася'")
