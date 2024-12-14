import sqlite3
import unittest

def insert_data_2(connection, meal_plans):
    cursor = connection.cursor()
    
    try:
        cursor.executemany("""
            INSERT INTO MealPlans (age_min, age_max, bmi_min, bmi_max, description, time, products_needed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, meal_plans)
        connection.commit()
    except sqlite3.IntegrityError:
        print("Duplicate entry detected.")
    finally:
        cursor.close()

class TestInsertData(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.cursor = cls.connection.cursor()
        
        cls.cursor.execute("""
            CREATE TABLE MealPlans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age_min INTEGER,
                age_max INTEGER,
                bmi_min REAL,
                bmi_max REAL,
                description TEXT,
                time TEXT,
                products_needed TEXT,
                UNIQUE(age_min, age_max, bmi_min, bmi_max, description, time)
            )
        """)
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_insert_data_success(self):
        meal_plans = [
            (18, 25, 18.5, 24.9, 'Healthy Plan', 'Breakfast', 'Eggs, Toast'),
            (26, 35, 25.0, 29.9, 'Balanced Plan', 'Lunch', 'Chicken Salad')
        ]
        
        insert_data_2(self.connection, meal_plans)  # Передаем соединение
        
        self.cursor.execute("SELECT COUNT(*) FROM MealPlans")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_insert_data_duplicate(self):
        meal_plans = [
            (18, 25, 18.5, 24.9, 'Healthy Plan', 'Breakfast', 'Eggs, Toast'),
            (26, 35, 25.0, 29.9, 'Balanced Plan', 'Lunch', 'Chicken Salad')
        ]
        
        insert_data_2(self.connection, meal_plans)  # Первая вставка
        insert_data_2(self.connection, meal_plans)  # Повторная вставка
        
        self.cursor.execute("SELECT COUNT(*) FROM MealPlans")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()


