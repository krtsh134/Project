import sqlite3

cnct = sqlite3.connect('health_control.db')
cursor = cnct.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables = cursor.fetchall()
print("Tables:", tables)

cursor.execute("SELECT * FROM MealPlans;") #после FROM - имя любой таблицы
rows = cursor.fetchall()

for row in rows:
    print(row)

cnct.close()