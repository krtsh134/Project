import sqlite3

cnct = sqlite3.connect('health_control.db')
cursor = cnct.cursor()

# cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
# tables = cursor.fetchall()
# print("Tables:", tables)

# cursor.execute("SELECT * FROM TrainPlans;") #после FROM - имя любой таблицы
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# cnct.close()

cursor.execute("PRAGMA table_info(TrainPlans);")
columns = [column[1] for column in cursor.fetchall()]

if 'description_train' not in columns:
    cursor.execute("ALTER TABLE TrainPlans ADD COLUMN description_train TEXT;")
    print("Столбец 'description_train' был добавлен.")
else:
    print("Столбец 'description_train' уже существует.")

cnct.commit()
cnct.close()