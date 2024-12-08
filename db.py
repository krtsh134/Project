import sqlite3
import json

def create_database(db = "health_controller.db"):
    """Creates the SQLite database and tables."""
    cnct = sqlite3.connect(db)
    cursor = cnct.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            calories INTEGER,
            protein_grams INTEGER,
            fat_grams REAL,
            corbohydrates_grams REAL,               
        )           
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MealPlans (
            plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            age_min INTEGER,
            age_max INTEGER,
            bmi_min REAL,
            bmi_max INTEGER,
            description TEXT,
            products_needed TEXT   
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS UserProfiles (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            height INTEGER,
            weight INTEGER,
            gender INTEGER,
            age INTEGER,
            user_products TEXT             
        )
    """)
    cnct.commit()
    cnct.close()

def insert_data(db = "health_controller.db"):
    """"Inserts data into the database."""
    cnct = sqlite3.connect(db)
    cursor = cnct.cursor()   

    products = [
        ('Яблоко', 47, 0.4, 0.4, 9.8, 100), #0
        ('Банан', 96, 1.5, 0.5, 21, 100),  #1
        ('Апельсин', 36, 0.9, 8.1, 0.2, 100),
        ('Абрикос', 45, 0.9, 0, 10.5, 100),
        ('Арбуз', 27, 0.5, 0.2, 6, 100),
        ('Виноград', 85, 1, 1, 18, 100),
        ('Баклажан', 25, 0.6, 0.1, 0.5, 100),
        ('Гранат', 50, 0.9, 0, 11.8, 100),
        ('Грейпфрут', 32, 0.9, 0, 7.3, 1000),
        ('Груша', 44, 0.4, 0, 10.7, 100),
        ('Кабачок', 27, 0.6, 0.3, 5.7, 100),
        ('Капуста белокочанная', 28, 1.8, 0, 5.4, 100),
        ('Картофель', 87, 2, 0.1, 19.7, 100),
        ('Клубника/земляника', 36, 1.2, 8, 100),
        ('Лимон', 18, 0.9, 0, 3.6, 100),
        ('Лук зеленый', 22, 1.3, 0, 4.3, 100),
        ('Малина', 39, 0.8, 9, 100),
        ('Морковь', 34, 1.3, 0.1, 7, 100),
        ('Огурцы', 15, 0.8, 0, 3, 100),
        ('Перец красный сладкий', 28, 1.3, 0, 5.7, 100),
        ('Помидоры', 20, 1, 0.2, 3.7, 100),
        ('Редис', 21, 1.2, 0, 4.1, 100),
        ('Свекла', 50, 1.7, 0, 10.8, 100),
        ('Манго', 62, 1, 0, 13, 100),
        ('Авокадо', 197, 2, 19, 7, 100),
        ('Грибы шампиньоны', 22, 4, 1, 0, 100),
        ('Горошек зелёный', 59, 4, 0, 10, 100),
        ('Фасоль', 30, 3, 0, 4, 100),
        ('Тыква', 22, 1, 0, 5, 100),
        ('Курица', 113, 23.6, 1.9, 0.4, 100),
        ('Рис белый', 259.07, 5.92, 1.52, 56.11, 100),
        ('Гречневая крупа', 346, 11.73, 74.95, 100),
        ('Масло сливочное', 747, 0.5, 82.5, 1, 100),
        ('Хлеб ржаной', 210, 4.7, 0.6, 49.5, 100),
        ('Молоко', 53, 2.8, 2.5, 4.6, 100),
        ('Кефир', 37, 2.8, 1, 4, 100),
        ('Сметана', 118, 3, 10, 2.9, 100),
        ('Творог нежирный', 89, 18.2, 0.6, 1.8, 100),
        ('Макароны', 400, 30, 12, 20, 100),
        ('Овсяная крупа', 342, 12.3, 6.1, 59.5, 100),
        ('Пшеничная крупа', 342, 11.2, 2, 65.7, 100),
        ('Манная крупа', 333, 10.3, 1, 38, 100),
        ('Яйцо куриное', 153, 12.7, 11.1, 0.6, 100),
        ('Сыр', 366, 24.1, 29.8, 0.4, 100),      
        ('Говядина', 191, 18.7, 12.6, 0, 100),
        ('Ветчина из индейки', 83, 9, 3, 5, 100),
        ('Семга', 142, 19.84, 6.34, 0, 100)
        
    ]

    cursor.executemany("""
                       INSERT INTO Products 
                       (name, calories, protein_grams, fat_grams, carbohydrates_grams, serving_size_grams) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                       products)
    
    meal_plans = [
        (16, 20, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([products[i] for i in (0, 4, 6) if i < len(products)], db)),
        (16, 20, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (16, 20, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (16, 20, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (16, 20, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (16, 20, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (16, 20, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (16, 20, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (16, 20, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (21, 25, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (21, 25, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (21, 25, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (21, 25, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (21, 25, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (21, 25, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (21, 25, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (21, 25, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (21, 25, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (26, 30, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (26, 30, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (26, 30, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (26, 30, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (26, 30, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (26, 30, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (26, 30, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (26, 30, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (26, 30, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (31, 35, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (31, 35, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (31, 35, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (31, 35, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (31, 35, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (31, 35, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (31, 35, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (31, 35, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (31, 35, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (36, 40, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (36, 40, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (36, 40, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (36, 40, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (36, 40, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (36, 40, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (36, 40, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (36, 40, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (36, 40, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (41, 45, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (41, 45, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (41, 45, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (41, 45, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (41, 45, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (41, 45, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (41, 45, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (41, 45, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (41, 45, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (46, 50, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (46, 50, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (46, 50, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (46, 50, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (46, 50, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (46, 50, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (46, 50, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (46, 50, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (46, 50, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([])),

        (51, 55, 10, 20, "Low-Caloried Plan", "Breakfast", json.dump([])),
        (51, 55, 10, 20, "Low-Caloried Plan", "Lunch", json.dump([])),
        (51, 55, 10, 20, "Low-Caloried Plan", "Dinner", json.dump([])),
        (51, 55, 20.1, 25, "Balanced-Caloried Plan", "Breakfast", json.dump([])),
        (51, 55, 20.1, 25, "Balanced-Caloried Plan", "Lunch", json.dump([])),
        (51, 55, 20.1, 25, "Balanced-Caloried Plan", "Dinner", json.dump([])),
        (51, 55, 25.1, 35, "High-Caloried Plan", "Breakfast", json.dump([])),
        (51, 55, 25.1, 35, "High-Caloried Plan", "Lunch", json.dump([])),
        (51, 55, 25.1, 35, "High-Caloried Plan", "Dinner", json.dump([]))

        # (20, 30, 18.5, 25, "Low-Calorie Plan", json.dumps([1, 2]))
        # (30, 40, 22, 28, "Balanced-Calorie Plan", json.dumps([1, 3, 4]))
        # (45, 60, 25, 30, "High-Caloried Plan", json.dumps([3, 5]))
    ]

    cursor.executemany(""" INSERT INTO MealPlans 
                       (age_min, age_max, bmi_min, bmi_max, description, products_nedeed)
                       VALUES (?, ?, ?, ?, ?, ?)""", 
                       meal_plans)
    
    cnct.commit()
    cnct.close()

create_database()
insert_data()