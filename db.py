import sqlite3
import json

def create_database():
    """Creates the SQLite database and tables."""
    with sqlite3.connect('health_control.db') as cnct:
        cursor = cnct.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                kilocalories REAL,
                protein_gramms REAL,
                fat_gramms REAL,
                carbohydrates_gramms REAL,
                serving_size_gramms REAL
                                    
            )           
        """)

        cnct.commit()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS MealPlans (
                plan_id INTEGER PRIMARY KEY AUTOINCREMENT,
                age_min INTEGER,
                age_max INTEGER,
                bmi_min REAL,
                bmi_max INTEGER,
                description TEXT,
                time TEXT,
                products_needed TEXT   
            )
        """)
        
        cnct.commit()

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

products = [
    ('Яблоко', 47, 0.4, 0.4, 9.8, 100), 
    ('Банан', 96, 1.5, 0.5, 21, 100),  
    ('Апельсин', 36, 0.9, 8.1, 0.2, 100),
    ('Абрикос', 45, 0.9, 0, 10.5, 100),
    ('Арбуз', 27, 0.5, 0.2, 6, 100),
    ('Виноград', 85, 1, 1, 18, 100),
    ('Баклажан', 25, 0.6, 0.1, 0.5, 100),
    ('Гранат', 50, 0.9, 0, 11.8, 100),
    ('Грейпфрут', 32, 0.9, 0, 7.3, 100),
    ('Груша', 44, 0.4, 0, 10.7, 100),
    ('Кабачок', 27, 0.6, 0.3, 5.7, 100),
    ('Капуста', 28, 1.8, 0, 5.4, 100),
    ('Картофель', 87, 2, 0.1, 19.7, 100),
    ('Клубника', 36, 1.2, 0.3, 8, 100),
    ('Лимон', 18, 0.9, 0, 3.6, 100),
    ('Лук', 22, 1.3, 0, 4.3, 100),
    ('Малина', 39, 4, 0.8, 9, 100),
    ('Морковь', 34, 1.3, 0.1, 7, 100),
    ('Огурцы', 15, 0.8, 0, 3, 100),
    ('Перец', 28, 1.3, 0, 5.7, 100),
    ('Помидоры', 20, 1, 0.2, 3.7, 100),
    ('Редис', 21, 1.2, 0, 4.1, 100),
    ('Свекла', 50, 1.7, 0, 10.8, 100),
    ('Манго', 62, 1, 0, 13, 100),
    ('Авокадо', 197, 2, 19, 7, 100),
    ('Грибы', 22, 4, 1, 0, 100),
    ('Горошек', 59, 4, 0, 10, 100),
    ('Фасоль', 30, 3, 0, 4, 100),
    ('Тыква', 22, 1, 0, 5, 100),
    ('Курица', 113, 23.6, 1.9, 0.4, 100),
    ('Рис', 259.07, 5.92, 1.52, 56.11, 100),
    ('Гречневая крупа', 346, 11.73, 3.4, 74.95, 100),
    ('Масло сливочное', 747, 0.5, 82.5, 1, 100),
    ('Хлеб', 210, 4.7, 0.6, 49.5, 100),
    ('Молоко', 53, 2.8, 2.5, 4.6, 100),
    ('Кефир', 37, 2.8, 1, 4, 100),
    ('Сметана', 118, 3, 10, 2.9, 100),
    ('Творог', 89, 18.2, 0.6, 1.8, 100),
    ('Макароны', 400, 30, 12, 20, 100),
    ('Овсяная крупа', 342, 12.3, 6.1, 59.5, 100),
    ('Пшеничная крупа', 342, 11.2, 2, 65.7, 100),
    ('Манная крупа', 333, 10.3, 1, 38, 100),
    ('Яйцо куриное', 153, 12.7, 11.1, 0.6, 100),
    ('Сыр', 366, 24.1, 29.8, 0.4, 100),      
    ('Говядина', 191, 18.7, 12.6, 0, 100),
    ('Ветчина', 83, 9, 3, 5, 100),
    ('Семга', 142, 19.84, 6.34, 0, 100)
    
]

def insert_data_1(products):
    """Inserts data into the database."""
    with sqlite3.connect('health_control.db') as cnct:
        cursor = cnct.cursor()
        cursor.executemany("""
                        INSERT OR IGNORE INTO Products 
                        (name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms) 
                        VALUES (?, ?, ?, ?, ?, ?)""", 
                        products)
    cnct.commit()

meal_plans = [
(16, 20, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(16, 20, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(16, 20, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(16, 20, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(16, 20, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(21, 25, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(21, 25, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(21, 25, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(21, 25, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(21, 25, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(26, 30, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(26, 30, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(26, 30, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(26, 30, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(26, 30, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(31, 35, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(31, 35, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(31, 35, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(31, 35, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(31, 35, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(36, 40, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(36, 40, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(36, 40, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(36, 40, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(36, 40, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(41, 45, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(41, 45, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(41, 45, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(41, 45, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(41, 45, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(46, 50, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(46, 50, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(46, 50, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(46, 50, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(46, 50, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

(51, 55, 10, 20, "Low-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Манная крупа', 'Молоко')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Молоко')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйца', "Кефир")])),
(51, 55, 10, 20, "Low-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Курица')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Макароны', 'Огурец', 'Помидор')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Картофель')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Рис')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный')])),
(51, 55, 10, 20, "Low-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),

(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Кефир')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Хлеб', 'Ветчина из индейки')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Банан', 'Яблоко', 'Творог')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Огурец', 'Помидор', 'Перец красный сладкий')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Гречневая крупа', 'Курица')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Помидор', 'Хлеб')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Рис', 'Помидор', 'Огурец')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Говядина', 'Картофель')])),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль')])),

(51, 55, 25.1, 35, "High-Caloried Plan", "Breakfast_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Овсяная крупа', 'Клубника', 'Малина', 'Молоко')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Breakfast_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Яйцо', 'Хлеб', 'Авокадо')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Breakfast_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Lunch_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Огурец', 'Перец', 'Морковь')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Lunch_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Курица', 'Хлеб', 'Помидор')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Lunch_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Творог', 'Сметана', 'Малина')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Dinner_1", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Семга', 'Фасоль', 'Капуста')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Dinner_2", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий')])),
(51, 55, 25.1, 35, "High-Caloried Plan", "Dinner_3", json.dumps([products[key] for key in range(len(products)) if products[key][0] in ('Ветчина из индейки', 'Хлеб', 'Авокадо')])),

]

def insert_data_2(meal_plans):
    with sqlite3.connect('health_control.db') as cnct:
        cursor = cnct.cursor()
        cursor.executemany("""
            INSERT OR IGNORE INTO MealPlans 
            (age_min, age_max, bmi_min, bmi_max, description, time, products_needed) 
            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
            meal_plans)
        cnct.commit()


create_database()
insert_data_1(products)
insert_data_2(meal_plans)