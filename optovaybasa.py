import sqlite3 as sq
from danye_bd import date_tovar, date_magaz, date_zayvka, date_kol, date_sostav

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS tovars")
    cur.execute("""CREATE TABLE IF NOT EXISTS tovars(
    id_tov INTEGER PRIMARY KEY AUTOINCREMENT,
    nazvanie TEXT,
    opisanie TEXT,
    ed_iz TEXT
)""")
    #cur.executemany("INSERT INTO tovars VALUES (?, ?, ?, ?)", date_tovar)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS magaz")
    cur.execute("""CREATE TABLE IF NOT EXISTS magaz(
    id_magaz INTEGER PRIMARY KEY AUTOINCREMENT,
    nazvanie TEXT,
    adres TEXT,
    tel TEXT
)""")
    #cur.executemany("INSERT INTO magaz VALUES (?, ?, ?, ?)", date_magaz)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS zayvka")
    cur.execute("""CREATE TABLE IF NOT EXISTS zayvka(
    id_zayvka INTEGER PRIMARY KEY AUTOINCREMENT,
    id_magaz INTEGER,
    data DATE,
    FOREIGN KEY (id_magaz) REFERENCES magaz (id_magaz)
)""")
    #cur.executemany("INSERT INTO zayvka VALUES (?, ?, ?)", date_zayvka)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS kolsclad")
    cur.execute("""CREATE TABLE IF NOT EXISTS kolsclad(
    id_sclad INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tov INTEGER,
    id_magaz INTEGER,
    kol INTEGER,
    FOREIGN KEY (id_tov) REFERENCES tovars (id_tov),
    FOREIGN KEY (id_magaz) REFERENCES magaz (id_magaz)
)""")
    #cur.executemany("INSERT INTO kolsclad VALUES (?, ?, ?, ?)", date_kol)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS sostav")
    cur.execute("""CREATE TABLE IF NOT EXISTS sostav(
    id_sostav INTEGER PRIMARY KEY AUTOINCREMENT,
    id_zayvka INTEGER,
    id_tov INTEGER,
    koli INTEGER,
    FOREIGN KEY (id_tov) REFERENCES tovars (id_tov),
    FOREIGN KEY (id_zayvka) REFERENCES tovars (id_zayvka)
)""")
    #cur.executemany("INSERT INTO sostav VALUES (?, ?, ?, ?)", date_sostav)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT nazvanie, opisanie FROM tovars") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT nazvanie, adres FROM magaz") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_magaz, data FROM zayvka") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_tov, kol FROM kolsclad") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_tov, kol FROM kolsclad ORDER BY kol DESC") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_zayvka, id_tov FROM sostav") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_tov FROM kolsclad WHERE kol < 350") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_magaz FROM zayvka WHERE data BETWEEN '2021-01-01' AND '2021-12-12' ") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_magaz FROM kolsclad WHERE kol < 500") 
    result = cur.fetchall()
print(result)

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=4999 WHERE id_tov = 4")
    
print("Задания 2 и 3 преподаватель разрешил не делать.")
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE magaz SET adres='Сорняк д21' WHERE id_magaz=(SELECT id_magaz FROM zayvka WHERE id_zayvka=8)")
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE zayvka SET data='2010-05-05' WHERE id_magaz = 1")
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=55555 WHERE (id_tov = 1) or (id_tov = 5)")

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE tovars SET opisanie='Теперь наш мармелад производится по всему миру!' WHERE id_tov = 7")
    cur.execute("UPDATE kolsclad SET kol=950 WHERE id_tov = 7")
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=((SELECT kol FROM kolsclad WHERE id_tov=(SELECT id_tov FROM sostav WHERE id_zayvka=9)) - (SELECT SUM(koli) FROM sostav WHERE id_tov=(SELECT id_tov FROM sostav WHERE id_zayvka=9))) WHERE id_tov=(SELECT id_tov FROM sostav WHERE id_zayvka=9)")    

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=((SELECT kol FROM kolsclad WHERE id_tov=1) - (SELECT SUM(koli) FROM sostav WHERE id_tov=1)) WHERE id_tov=1")

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE magaz SET nazvanie='В може бы', adres='Фупновычй д43 кв1' WHERE id_magaz=(SELECT id_magaz FROM zayvka WHERE id_zayvka = 2)")
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE magaz SET nazvanie='Новое название' WHERE id_magaz=")