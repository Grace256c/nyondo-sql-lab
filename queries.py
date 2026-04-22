import sqlite3

conn = sqlite3.connect('nyondo_stock.db')
cursor = conn.cursor()
#This is the Querry A
print("querry A")
rows = cursor.execute("SELECT *from products").fetchall()
for row in rows:
    print(row)
print()

#This is the Query B
print("query B")
rows = cursor.execute("SELECT name, price from products").fetchall()
for row in rows:
    print(row)
print()

#This is the Query C
print("query C")
rows = cursor.execute("SELECT *from products where id = 3").fetchall()
for row in rows:
    print(row)
print()

#This is the Query D
print("query D")
rows = cursor.execute("SELECT *from products where name like '% sheet %'").fetchall()
for row in rows:
    print(row)
print()

#This is the Query E
print("query E")
rows = cursor.execute("SELECT *from products order by price desc").fetchall()
for row in rows:
    print(row)
print()

#This is the Query F
print("query F")
rows = cursor.execute("SELECT *from products order by price desc limit 2").fetchall()
for row in rows:
    print(row)
print()

#This is the Query G
print("query G")
cursor.execute("update products set price = 38000 where id = 1")
conn.commit
rows = cursor.execute("SELECT *from products where id = 1").fetchall()
for row in rows:
    print(row)
print()