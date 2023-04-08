# Вариант 2
# Разработать БД «ОПТОВАЯ БАЗА».
# Структура БД состоит из пяти таблиц:
# Товары, Магазины, Заявки магазинов, Количество товаров на складе, Состав.
# Установить связь между таблицами.
# Заполнить таблицы произвольными данными (не менее 10 записей).
# Реализовать SQL- запросы на выборку, обновление, удаление данных из БД.



import sqlite3 as sq
from danye_bd import date_tovar, date_magaz, date_zayvka, date_kol, date_sostav

with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS tovars")
    cur.execute("""CREATE TABLE IF NOT EXISTS tovars(
    id_tov INTEGER PRIMARY KEY AUTOINCREMENT,
    nazvanie TEXT,
    opisanie TEXT,
    ed_iz TEXT
)""")
    cur.executemany("INSERT INTO tovars VALUES (?, ?, ?, ?)", date_tovar)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS magaz")
    cur.execute("""CREATE TABLE IF NOT EXISTS magaz(
    id_magaz INTEGER PRIMARY KEY AUTOINCREMENT,
    nazvanie TEXT,
    adres TEXT,
    tel TEXT
)""")
    cur.executemany("INSERT INTO magaz VALUES (?, ?, ?, ?)", date_magaz)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS zayvka")
    cur.execute("""CREATE TABLE IF NOT EXISTS zayvka(
    id_zayvka INTEGER PRIMARY KEY AUTOINCREMENT,
    id_magaz INTEGER,
    data DATE,
    FOREIGN KEY (id_magaz) REFERENCES magaz (id_magaz)
)""")
    cur.executemany("INSERT INTO zayvka VALUES (?, ?, ?)", date_zayvka)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS kolsclad")
    cur.execute("""CREATE TABLE IF NOT EXISTS kolsclad(
    id_sclad INTEGER PRIMARY KEY AUTOINCREMENT,
    id_tov INTEGER,
    id_magaz INTEGER,
    kol INTEGER,
    FOREIGN KEY (id_tov) REFERENCES tovars (id_tov),
    FOREIGN KEY (id_magaz) REFERENCES magaz (id_magaz)
)""")
    cur.executemany("INSERT INTO kolsclad VALUES (?, ?, ?, ?)", date_kol)
    
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS sostav")
    cur.execute("""CREATE TABLE IF NOT EXISTS sostav(
    id_sostav INTEGER PRIMARY KEY AUTOINCREMENT,
    id_zayvka INTEGER,
    id_tov INTEGER,
    koli INTEGER,
    FOREIGN KEY (id_tov) REFERENCES tovars (id_tov),
    FOREIGN KEY (id_zayvka) REFERENCES tovars (id_zayvka)
)""")
    cur.executemany("INSERT INTO sostav VALUES (?, ?, ?, ?)", date_sostav)

print("Задание SELECT №1. Вывести список всех товаров и их описания:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT nazvanie, opisanie FROM tovars") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №2. Вывести список всех магазинов и их адресов:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT nazvanie, adres FROM magaz") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №3. Вывести список всех заявок магазинов и даты, на которые они были поданы:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_magaz, data FROM zayvka") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №4. Вывести список товаров и количество их наличия на складе:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_tov, kol FROM kolsclad") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №5. Вывести список товаров и количество их наличия на складе в порядке убывания количества:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_tov, kol FROM kolsclad ORDER BY kol DESC") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №6. Вывести список всех заявок магазинов и товаров, которые были в них заказаны:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_zayvka, id_tov FROM sostav") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №7. Вывести список всех товаров, у которых на складе количество меньше минимально допустимого:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_tov FROM kolsclad WHERE kol < 350") 
    result = cur.fetchall()
print(result)


print("Задание SELECT №8. Вывести список всех заявок магазинов, которые были сделаны в определенный период времени:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_magaz FROM zayvka WHERE data BETWEEN '2023-01-01' AND '2023-02-04' ") 
    result = cur.fetchall()
print(result)

print("Задание SELECT №9. Вывести список всех магазинов, у которых суммарное количество товаров на складе меньше заданного значения:")
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("SELECT id_magaz FROM kolsclad WHERE kol < 500") 
    result = cur.fetchall()
print(result)

# Задание UPDATE №1. 
# Обновить количество товара на складе для конкретного товара
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=4999 WHERE id_tov = 4")
    
# Задания 2 и 3 преподаватель разрешил не делать.

# Задание UPDATE №4. 
# Обновить адрес магазина, который подал заявку
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE magaz SET adres='Сорняк д21' WHERE id_magaz=(SELECT id_magaz FROM zayvka WHERE id_zayvka=8)")
    
# Задание UPDATE №5. 
# Обновить дату заявки для конкретного магазина
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE zayvka SET data='2023-05-05' WHERE id_magaz = 1")

# Задание UPDATE №6. 
# Обновить количество товара на складе для нескольких товаров
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=55555 WHERE (id_tov = 1) or (id_tov = 5)")

# Задание UPDATE №7.
# Обновить описание товара и количество на складе для конкретного товара
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE tovars SET opisanie='Теперь наш мармелад производится по всему миру!' WHERE id_tov = 7")
    cur.execute("UPDATE kolsclad SET kol=950 WHERE id_tov = 7")

# Задание UPDATE №8. 
# Обновление количества товаров на складе, учитывая выполненную заявку магазина
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=((SELECT kol FROM kolsclad WHERE id_tov=(SELECT id_tov FROM sostav WHERE id_zayvka=9)) - (SELECT SUM(koli) FROM sostav WHERE id_tov=(SELECT id_tov FROM sostav WHERE id_zayvka=9))) WHERE id_tov=(SELECT id_tov FROM sostav WHERE id_zayvka=9)")    

# Задание UPDATE №9. 
# Обновление количества товаров на складе, учитывая выполненную заявку магазина с учетом конкретного товара
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE kolsclad SET kol=((SELECT kol FROM kolsclad WHERE id_tov=1) - (SELECT SUM(koli) FROM sostav WHERE id_tov=1)) WHERE id_tov=1")

# Задание UPDATE №10. 
# Обновить название магазина, который подал заявку, и адрес магазина для конкретной заявки.
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE magaz SET nazvanie='В може бы', adres='Фупновычй д43 кв1' WHERE id_magaz=(SELECT id_magaz FROM zayvka WHERE id_zayvka = 2)")
    
# Отказались от 11 задания

# Задание UPDATE №12. 
# Обновить адрес магазина и количество товара в заявке для конкретного товара
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE magaz SET adres='Мойдодырский край д54' WHERE id_magaz= (SELECT id_magaz FROM zayvka WHERE id_zayvka=(SELECT id_zayvka FROM sostav WHERE id_tov=10))")
    cur.execute("UPDATE sostav SET koli=896 WHERE id_tov=10")

# Задание UPDATE №13. 
# Обновить описание товара и количество на складе для нескольких товаров
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("UPDATE tovars SET opisanie='Содержит вкусные вкусы' WHERE (id_tov = 2) or (id_tov=3)")
    cur.execute("UPDATE kolsclad SET kol=7000 WHERE (id_tov = 2) or (id_tov=3)")

# Задание DELETE №1. 
# Удаление заявки магазина и соответствующих записей в таблице состава
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM zayvka WHERE id_zayvka=6")
    cur.execute("DELETE FROM sostav WHERE id_zayvka=6")

# Задание DELETE №2. 
# Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, не имеющим заявок в таблице "Состав"
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM kolsclad WHERE id_tov NOT IN (SELECT id_tov FROM sostav)")
    
# Задание DELETE №3. 
# Удалить из таблицы "Заявки магазинов" все заявки магазинов, адрес которых начинается на "ул. Ленина"
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM zayvka WHERE id_magaz IN (SELECT id_magaz FROM magaz WHERE adres LIKE 'ул. Ленина%')")
    
# Задание DELETE №4. 
# Удалить из таблицы "Состав" записи, соответствующие товарам, которых нет на складе (количество = 0)
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM sostav WHERE id_tov IN (SELECT id_tov FROM kolsclad WHERE kol=0)")

# Задание DELETE №5. 
# Удалить из таблицы "Магазины" магазины, в которых не было заявок в течение последнего месяца
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM magaz WHERE id_magaz NOT IN (SELECT id_magaz FROM zayvka WHERE data BETWEEN '2023-04-01' AND '2023-04-30')")

# Задание DELETE №6. 
# Удалить из таблицы "Товары" товары, которые не были заказаны ни разу
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM tovars WHERE id_tov NOT IN (SELECT id_tov FROM sostav)")
    
# Задание DELETE №7. 
# Удалить из таблицы "Количество товаров на складе" записи, соответствующие товарам, которые не были заказаны ни разу
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM kolsclad WHERE id_tov NOT IN (SELECT id_tov FROM sostav)")
    
# Задание DELETE №8. 
# Удалить из таблицы "Состав" записи, соответствующие заявкам, которые были поданы более месяца назад
with sq.connect('optovbd.db') as con: 
    cur = con.cursor()
    cur.execute("DELETE FROM sostav WHERE id_zayvka IN (SELECT id_zayvka FROM zayvka WHERE data BETWEEN '2023-01-01' AND '2023-03-31')")