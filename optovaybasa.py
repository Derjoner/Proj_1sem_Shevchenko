import sqlite3 as sq
from danye_bd import date_tovar, date_magaz, date_zayvka, date_kol, date_sostav

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS tovars(
    id_tov INTEGER PRIMARY KEY AUTOINCREMENT,
    nazvanie TEXT,
    opisanie TEXT,
    ed_iz TEXT
)""")
    #cur.executemany("INSERT INTO tovars VALUES (?, ?, ?, ?)", date_tovar)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS magaz(
    id_magaz INTEGER PRIMARY KEY AUTOINCREMENT,
    nazvanie TEXT,
    adres TEXT,
    tel TEXT
)""")
    #cur.executemany("INSERT INTO magaz VALUES (?, ?, ?, ?)", date_magaz)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS zayvka(
    id_zayvka INTEGER PRIMARY KEY AUTOINCREMENT,
    id_magaz INTEGER,
    data DATE,
    FOREIGN KEY (id_magaz) REFERENCES magaz (id_magaz)
)""")
    #cur.executemany("INSERT INTO zayvka VALUES (?, ?, ?)", date_zayvka)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS kolsclad(
    id_sclad INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tov INTEGER,
    kol INTEGER,
    FOREIGN KEY (id_tov) REFERENCES tovars (id_tov)
)""")
    #cur.executemany("INSERT INTO kolsclad VALUES (?, ?, ?)", date_kol)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS sostav(
    id_sostav INTEGER PRIMARY KEY AUTOINCREMENT,
    id_zayvka INTEGER,
    id_tov INTEGER,
    koli INTEGER,
    FOREIGN KEY (id_tov) REFERENCES tovars (id_tov),
    FOREIGN KEY (id_zayvka) REFERENCES tovars (id_zayvka)
)""")
    cur.executemany("INSERT INTO kolsclad VALUES (?, ?, ?)", date_sostav)