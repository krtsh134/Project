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
            CREATE TABLE IF NOT EXISTS TrainPlans (
                train_id INTEGER PRIMARY KEY AUTOINCREMENT,
                min_age INTEGER,
                max_age INTEGER,
                min_bmi INTEGER,
                max_bmi INTEGER,
                train_number TEXT 
                description TEXT              
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
(16, 20, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(16, 20, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(16, 20, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(16, 20, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(16, 20, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(16, 20, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(16, 20, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(16, 20, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(16, 20, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(16, 20, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(16, 20, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(16, 20, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(16, 20, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(21, 25, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(21, 25, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(21, 25, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(21, 25, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(21, 25, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(21, 25, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(21, 25, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(21, 25, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(21, 25, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(21, 25, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(21, 25, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(21, 25, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(21, 25, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(26, 30, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(26, 30, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(26, 30, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(26, 30, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(26, 30, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(26, 30, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(26, 30, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(26, 30, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(26, 30, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(26, 30, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(26, 30, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(26, 30, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(26, 30, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(31, 35, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(31, 35, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(31, 35, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(31, 35, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(31, 35, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(31, 35, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(31, 35, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(31, 35, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(31, 35, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(31, 35, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(31, 35, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(31, 35, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(31, 35, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(36, 40, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(36, 40, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(36, 40, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(36, 40, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(36, 40, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(36, 40, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(36, 40, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(36, 40, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(36, 40, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(36, 40, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(36, 40, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(36, 40, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(36, 40, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(41, 45, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(41, 45, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(41, 45, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(41, 45, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(41, 45, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(41, 45, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(41, 45, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(41, 45, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(41, 45, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(41, 45, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(41, 45, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(41, 45, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(41, 45, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(46, 50, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(46, 50, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(46, 50, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(46, 50, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(46, 50, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(46, 50, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(46, 50, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(46, 50, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(46, 50, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(46, 50, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(46, 50, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(46, 50, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(46, 50, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']"),

(51, 55, 10, 20, "Low-Caloried Plan", "breakfast", "['Манная крупа', 'Молоко']"),
(51, 55, 10, 20, "Low-Caloried Plan", "breakfast", "['Овсяная крупа', 'Молоко']"),
(51, 55, 10, 20, "Low-Caloried Plan", "breakfast", "['Яйца', 'Кефир']"),
(51, 55, 10, 20, "Low-Caloried Plan", "lunch", "['Хлеб', 'Курица']"),
(51, 55, 10, 20, "Low-Caloried Plan", "lunch", "['Семга', 'Макароны', 'Огурец', 'Помидор']"),
(51, 55, 10, 20, "Low-Caloried Plan", "lunch", "['Курица', 'Картофель']"),
(51, 55, 10, 20, "Low-Caloried Plan", "dinner", "['Семга', 'Рис']"),
(51, 55, 10, 20, "Low-Caloried Plan", "dinner", "['Курица', 'Помидор', 'Огурец', 'Фасоль', 'Горошек зелёный']"),
(51, 55, 10, 20, "Low-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),

(51, 55, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Творог', 'Кефир']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Хлеб', 'Ветчина из индейки']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "breakfast", "['Банан', 'Яблоко', 'Творог']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Огурец', 'Помидор', 'Перец красный сладкий']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Гречневая крупа', 'Курица']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Помидор', 'Хлеб']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Курица', 'Рис', 'Помидор', 'Огурец']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Говядина', 'Картофель']"),
(51, 55, 20.1, 25, "Balanced-Caloried Plan", "dinner", "['Семга', 'Перец красный сладкий', 'Помидор', 'Фасоль']"),

(51, 55, 25.1, 35, "High-Caloried Plan", "breakfast", "['Овсяная крупа', 'Клубника', 'Малина', 'Молоко']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "breakfast", "['Яйцо', 'Хлеб', 'Авокадо']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "breakfast", "['Творог', 'Сметана', 'Малина']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Огурец', 'Перец', 'Морковь']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "lunch", "['Курица', 'Хлеб', 'Помидор']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "lunch", "['Творог', 'Сметана', 'Малина']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "dinner", "['Семга', 'Фасоль', 'Капуста']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "dinner", "['Рис', 'Фасоль', 'Капуста', 'Перец красный сладкий']"),
(51, 55, 25.1, 35, "High-Caloried Plan", "dinner", "['Ветчина из индейки', 'Хлеб', 'Авокадо']")
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

train_plans = [
    (16, 20, 10, 20, "Train_1", "разминка, пробежка 20 минут, приседания 3х15, отжимания 3х15,подтягивания (или тяги к поясу) 3х10, заминка."),
    (16, 20, 10, 20, "Train_2", "разминка, высокоинтенсивная интервальная тренировка (HIIT) 15 минут, берпи 3х12, планка 3х30сек, заминка."),
    (16, 20, 10, 20, "Train_3", "разминка, велотренажер 25 минут, выпады 3х15 на каждую ногу, подъёмы на икры 3х10, заминка."),
    (16, 20, 20.1, 25, "Train_1", "разминка, пробежка 25 минут, приседания 3х10 с гантелями (2-3 кг), отжимания 3х12, выпады 3х12 на каждую ногу, заминка."),
    (16, 20, 20.1, 25, "Train_2", "разминка, высокоинтенсивная интервальная тренировка 20 минут, берпи 3х10, прыжковые приседания 3х15, альпинист 3х15, заминка."),
    (16, 20, 20.1, 25, "Train_3", "разминка, эллиптический тренажер 30 минут, приседания 3х15, отжимания 3х10, заминка."),
    (16, 20, 25.1, 35, "Easy", "Train_1", "разминка, 30 минут быстрой ходьбы, приседания 3х10, отжимания у стены 3х10, поворот корпуса  3х15, заминка."),
    (16, 20, 25.1, 35, "Train_2", "разминка, езда на велосипеде 25 минут, приседания 3х12, подъём ног 3х10, заминка."),
    (16, 20, 25.1, 35, "Train_3", "разминка, 20 минут быстрой ходьбы, приседаний на стуле 3х10, 3х15 шагов на месте, заминка."),

    (21, 25, 10, 20, "Train_1", "разминка, пробежка 20 минут, приседания 3х15, отжимания на брусьях 3х15, подтягивания (или тяга к поясу) 3х15, заминка."),
    (21, 25, 10, 20, "Train_2", "разминка, высокоинтенсивная интервальная тренировка 15 минут (берпи, альпинисты, прыжки), 3х30сек в планке, 3х15 прыжков в приседе, заминка."),
    (21, 25, 10, 20, "Train_3", "разминка, 25-минутная езда на велосипеде, выпады 3х15 на каждую ногу, подъёмы на икры 3х10, скручивания на пресс 3х15, заминка."),
    (21, 25, 20.1, 25, "Train_1", "разминка, 25-минутный интервальный бег, приседания с гантелями (5 кг) 3х12, отжимания 3х10, 3х10 подтягиваний, заминка."),
    (21, 25, 20.1, 25, "Train_2", "разминка, 20-минутная высокоинтенсивная интервальная тренировка (берпи, прыжки на скакалке, альпинист), 3х15 махов гирей, 3 подхода по 20 русских скруток, заминка."),
    (21, 25, 20.1, 25, "Train_3", "разминка, 30 минут на гребном тренажере, приседания 3х15, отжимания 3х10, выпады 3х15, заминка."),
    (21, 25, 25.1, 35, "Train_1", "разминка, 30 минут быстрой ходьбы, приседания 3х10, отжимания на брусьях 3х10, 3х15 поворотов корпуса, заминка."),
    (21, 25, 25.1, 35, "Train_2", "разминка, 25-минутная езда на велосипеде, приседания 3х12, подъёмы ног 3х10, скручивания сидя 3х15, заминка."),
    (21, 25, 25.1, 35, "Train_3", "разминка, 20 минут быстрой ходьбы, приседания на стуле 3х10, шаги на месте 3х15, круговые движения руками 3х10, заминка."),

    (26, 30, 10, 20, "Train_1", "разминка 5 минут, бег трусцой 25 минут, приседания 3х15, отжимания на брусьях 3х12, тяга гантелей в наклоне 3х10 на каждую руку (гантели по 5–8 кг), планка 3х30сек, заминка 5 минут."),
    (26, 30, 10, 20, "Train_2", "разминка, высокоинтенсивная интервальная тренировка 20 минут (30 секунд упражнение и 30 секунд отдыха): берпи, альпинисты, прыжки на месте; выпады 3х10 на каждую ногу, скручивания 3х15 на каждую сторону, подъёмы ног 3х15, заминка."),
    (26, 30, 10, 20, "Train_3", "разминка, велотренажёр 30 минут, приседания 3х15, отжимания 3хМаксимальное кол-во повторений, боковая планка 3х30сек на каждую сторону, ягодичный мостик 3х15, заминка."),
    (26, 30, 20.1, 25, "Train_1", "разминка, бег трусцой 30 минут, приседания с гантелью или гирей 3х10, отжимания 3х12, тяга гантели в наклоне 3х10 на каждую руку (гантели 8–12 кг), планка 3х45сек, заминка."),
    (26, 30, 20.1, 25, "Train_2", "разминка, круговая тренировка 25 минут (берпи, прыжки в приседе, высокие колени), тяга гантелей 3х10 (гантели 5–8 кг), скручивания 3х15 на каждую сторону, боковая планка 3х45 каждую сторону, заминка."),
    (26, 30, 20.1, 25, "Train_3", "разминка, занятия на эллиптическом тренажере 35 минут, прыжки со скакалкой 3х100, отжимания на наклонной скамье 3х12, сгибания рук с гантелями 3х12 (гантели 5–8 кг), заминка."),
    (26, 30, 25.1, 35, "Train_1", "разминка, быстрая ходьба 35 минут, приседания на стуле 3х12, отжимания от стены 3х12, повороты корпуса 3х15 на каждую сторону, подъёмы рук 3х15, заминка."),
    (26, 30, 25.1, 35, "Train_2", "разминка, велотренажёр 30 минут, модифицированные приседания 3х12, подъёмы ног 3х15, скручивания корпуса сидя 3х15 на каждую сторону, круговые движения руками 3х15 вперёд, 3х15 назад, заминка."),
    (26, 30, 25.1, 35, "Train_3", "разминка, аквааэробика 30 минут, ходьба на месте 3х60сек, движения рук в воде 3х60сек, движения ног в воде 3х60сек, заминка"),

    (31, 35, 10, 20, "Train_1", "Разминка 5 минут, Кардио 25 минут, Приседания 3х15, Отжимания на наклонной скамье 3х12, Тяга гантелей в наклоне 3х12, Планка 3х45сек, статическая растяжка 5 минут"),
    (31, 35, 10, 20, "Train_2", "Разминка 5 минут, Круговая тренировка 20 минут (45 секунд упражнения и отдых 15 секунд) 3 раза: берпи, альпинисты, выпрыгивания, выпады с чередованием ног; скручивания 3х20, планка 3х30сек, растяжка 5 минут"),
    (31, 35, 10, 20, "Train_3", "Разминка 5 минут, йога 45 минут, заминка 5 минут"),
    (31, 35, 20.1, 25, "Train_1", "разминка 5 минут, кардио 30 имнут, Приседания с гантелями 3х12, Отжимания 3хМаксимальное кол-во повторений, Жим гантелей лёжа 3х10, Тяга гантелей в наклоне 3х10, Планка 3х60сек, растяжка 5 минут"),
    (31, 35, 20.1, 25, "Train_2", "разминка 5 минут, круговая тренировка 25 мин: берпи, размахивания гантелями, степ, выпады; русские скрутки 3х25, планка 3х45сек, статическая растяжка 5 минут"),
    (31, 35, 20.1, 25, "Train_3", "разминка 5 минут, приседания, становая тяга, заминка 5 минут"),
    (31, 35, 25.1, 35, "Train_1", "Разминка 5 минут, кардио 35 мин, Приседания на стуле 3х15, Отжимания от стены 3х12, Подъём гантелей на бицепс 3х15, Разгибание трицепсов с гантелями 3х15, планка 3х30сек, заминка"),
    (31, 35, 25.1, 35, "Train_2", "Разминка 5 минут, акваэробика 45 мин, заминка 5 минут"),
    (31, 35, 25.1, 35, "Train_3", "Разминка 5 минут, Круговая тренировка 30 минут: подтягивания, подъем ног лежа на боку, скручивания туловища;  заминка"),

    (36, 40, 10, 20, "Train_1", "Разминка 7 минут, кардио 30 минут, Приседания 3х12, отжимания 3хМаксимальное кол-во, тяга в наклоне с гантелями 3х12, жим над головой 3х12, планка минуту, заминка 7 минут"),
    (36, 40, 10, 20, "Train_2", "Разминка 7 минут, Круговая тренировка (45 секунд упражнения, 15 секунд отдыха): берпи, скалолаз, выпрыгивания, выпады; планка 3х30сек, заминка 5 минут"),
    (36, 40, 10, 20, "Train_3", "Разминка 5 минут, Йога 45 минут, заминка 5 минут"),
    (36, 40, 20.1, 25, "Train_1", "Разминка 5 минут, кардио 30 минут, отжимания 3хМаксимальное кол-во, приседания 3х12, скручивания на пресс 3х10, румынская тяга (8кг) 3х10, планка 60 секунд, заминка 5 минут"),
    (36, 40, 20.1, 25, "Train_2", "Разминка 5 минут, круговая тренировка 25 минут (45 секунд упражнения, 15 отдых): берпи, скалолаз, выпрыгивания; заминка 5 минут"),
    (36, 40, 20.1, 25, "Train_3", "Разминка 5 минут, плаванье 40 минут, йога 30 минут, заминка 5 минут"),
    (36, 40, 25.1, 35, "Train_1", "Разминка 5 минут, кардио 35 минут, степ 3х15, планка, заминка 5 минут"),
    (36, 40, 25.1, 35, "Train_2", "Разминка 5 минут, круговая тренировка 20 минут (45 секунд упражнения, 15 отдых): берпи, скалолаз, выпрыгивания, заминка 5 минут"),
    (36, 40, 25.1, 35, "Train_3", "Разминка 5 минут, акваэробика 50 минут, заминка 5 минут"),

    (41, 45, 10, 20, "Train_1", "Разминка 7 минут, кардио 30 минут, приседания 3х12, отжимания 3хМаксимальное кол-во, Тяга гантелей в наклоне 3х12 на каждую руку, планка 3х45сек, заминка 5 минут"),
    (41, 45, 10, 20, "Train_2", "Разминка 5 минут, Круговая тренировка 20 минут (45 секунд упражнения, 15 секунд отдыха): берпи, скалолаз, выпрыгивания, выпады; заминка 5 минут"),
    (41, 45, 10, 20, "Train_3", "Разминка 5 минут, йога 60 минут, заминка 5 минут"),
    (41, 45, 20.1, 25, "Train_1", "Разминка 5 минут, кардио 30 минут, приседания 3х15, отжимания 3хМаксимальное кол-во, Тяга гантелей в наклоне 3х15 на каждую руку, планка 3х45сек, заминка 5 минут"),
    (41, 45, 20.1, 25, "Train_2", "Разминка 5 минут, Круговая тренировка 25 минут (45 секунд упражнения, 15 секунд отдыха): берпи, скалолаз, выпрыгивания, выпады; заминка 5 минут"),
    (41, 45, 20.1, 25, "Train_3", "Разминка 5 минут, йога 70 минут, заминка 5 минут"),
    (41, 45, 25.1, 35, "Train_1", "Разминка 7 минут, кадио 35, приседания у стула 3х15, отжимания от стены 3х12, Сгибания рук с гантелями 3х15, Разгибания рук с гантелями 3х12, планка 3х40сек заминка 5 минут"),
    (41, 45, 25.1, 35, "Train_2", "Разминка 5 минут, аквааэробика 40 минут, заминка 5 минут"),
    (41, 45, 25.1, 35, "Train_3", "Разминка 5 минут, йога 50 минут, растяжка в воде 5 минут"),

    (46, 50, 10, 20, "Train_1", "Разминка 10 минут, ходьба 25 минут, приседания у стуал 3х12, отжимания у стены 3х10, Подъемы рук с гантелями 3х12, Подъемы ног лежа 3х10, планка 3х40, упражнение на балланс по 30 секунд, заминка 7 минут"),
    (46, 50, 10, 20, "Train_2", "Разминка 7 минут, йога 60 минут, заминка 7 минут"),
    (46, 50, 10, 20, "Train_3", "Разминка 7 минут, круговая трениовка 20 минут (30 секунд упражнение, 15 секунд отдых): ходьба на месте, медленные приседания у стуал, подъемы ног и руук лежа, планка, растяжка, заминка 7 минут"),
    (46, 50, 20.1, 25, "Train_1", "Разминка 10 минут, ходьба 30 минут, приседания у стуал 3х15, отжимания у стены 3х12, Подъемы рук с гантелями 3х15, Подъемы ног лежа 3х12, планка 3х45, упражнение на балланс по 40 секунд, заминка 5 минут"),
    (46, 50, 20.1, 25, "Train_2", "Разминка 7 минут, акваэробика 60 минут, заминка 5 минут"),
    (46, 50, 20.1, 25, "Train_3", "Разминка 7 минут, круговая трениовка 25 минут (30 секунд упражнение, 15 секунд отдых): ходьба на месте, медленные приседания у стуал, подъемы ног и руук лежа, планка, растяжка, заминка 5 минут"),
    (46, 50, 25.1, 35, "Train_1", "Разминка 7 минут, ходьба 30 минут, приседания у стуал 3х10, отжимания от стены 3х10, подъемы рук с легкими гантелями 3х10, подъемы туловища 3х10, заминка 8 минут"),
    (46, 50, 25.1, 35, "Train_2", "Разминка 5 минут в воде, аквааэробика 45 минут, заминка 5 минут"),
    (46, 50, 25.1, 35, "Train_3", "Разминка 5 минут, йога, упражнения на гибкость 60 минут, заминка 5 минут"),

    (51, 55, 10, 20, "Train_1", "Разминка 10 минут, скандинавская ходьба 25 минут, приседания у стула 3х8, отжимания у стены 3х8, Подъемы рук с легкими гантелями 3х8, Подъемы ног лежа на спине 3х8, планка 3х30 сек, Упражнения на баланс, заминка 10 минут"),
    (51, 55, 10, 20, "Train_2", "Разминка 7 минут, йога 45 минут, упражнения на гибкость, заминка 7 минут"),
    (51, 55, 10, 20, "Train_3", "Разминка 5 минут, круговая тренировка 20 минут (упражнение 30 секунд, отдых 15 секунд): Ходьба на месте с высоким подниманием коленей, Медленные приседания у стула, Подъемы рук, Подъемы ног лежа на спине, Упражнения на растяжку, заминка 5 минут"),
    (51, 55, 20.1, 25, "Train_1", "Разминка 10 минут, скандинавская ходьба 30 минут, приседания у стула 3х10, отжимания у стены 3х10, Подъемы рук с легкими гантелями 3х10, Подъемы ног лежа на спине 3х8, планка 3х25 сек, Упражнения на баланс, заминка 10 минут"),
    (51, 55, 20.1, 25, "Train_2", "Разминка 7 минут, йога 60 минут, упражнения на гибкость, заминка 7 минут"),
    (51, 55, 20.1, 25, "Train_3", "Разминка 5 минут, круговая тренировка 30 минут (упражнение 30 секунд, отдых 15 секунд): Ходьба на месте с высоким подниманием коленей, Медленные приседания у стула, Подъемы рук, Подъемы ног лежа на спине, Упражнения на растяжку, заминка 5 минут"),
    (51, 55, 25.1, 35, "Train_1", "Разминка 10 минут, ходьба 30 минут, приседания у стула 3х8, подъемы рук 3х10, подъемы ног 3х10, заминка 10 минут"),
    (51, 55, 25.1, 35, "Train_2", "Разминка в воде 7 минут, аквааэробика 40 минут низкая интенсивность, заминка в воде 7 минут"),
    (51, 55, 25.1, 35, "Train_3", "Разминка 7 минут, йога 45 минут - базовые упражнения на гибкость и укрепление мышц, заминка 5 минут - расслабление и глубокое дыхание"),
]

create_database()
insert_data_1(products)
insert_data_2(meal_plans)