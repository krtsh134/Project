import unittest
import sqlite3
import os
from count_nutritional_value import add_meal_plans, get_meal_plan

TEST_DB = 'test_health_control.db'

class TestMealPlans(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Создание тестовой базы данных перед выполнением всех тестов"""
        cls.connection = sqlite3.connect(TEST_DB)
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute("""
            CREATE TABLE IF NOT EXISTS MealPlans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age_min INTEGER,
                age_max INTEGER,
                bmi_min FLOAT,
                bmi_max FLOAT,
                description TEXT,
                time TEXT,
                products_needed TEXT
            )
        """)
        cls.connection.commit()

    @classmethod
    def tearDownClass(cls):
        """Удаление тестовой базы данных после выполнения всех тестов"""
        cls.connection.close()
        os.remove(TEST_DB)

    def setUp(self):
        """Очистка таблицы перед каждым тестом"""
        self.cursor.execute("DELETE FROM MealPlans")
        self.connection.commit()

    def test_add_meal_plans(self):
        """Тест на добавление плана питания в базу данных"""
        add_meal_plans(18, 30, 18.5, 24.9, "Healthy Breakfast", "breakfast", "oats, milk, fruits", db_name=TEST_DB)
        self.cursor.execute("SELECT * FROM MealPlans")
        results = self.cursor.fetchall()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][3], 18.5)  # Проверка bmi_min
        self.assertEqual(results[0][6], "breakfast")  # Проверка времени

    def test_get_meal_plan(self):
        """Тест на получение плана питания"""
        # Добавляем тестовые планы питания
        add_meal_plans(18, 30, 18.5, 24.9, "Healthy Breakfast", "breakfast", "oats, milk", db_name=TEST_DB)
        add_meal_plans(18, 30, 18.5, 24.9, "Light Lunch", "lunch", "salad, chicken", db_name=TEST_DB)
        add_meal_plans(18, 30, 18.5, 24.9, "Dinner Plan", "dinner", "rice, fish", db_name=TEST_DB)

        # Получаем план питания на основе доступных продуктов
        result = get_meal_plan(25, 22.0, ["oats", "milk", "chicken", "salad"], db_name=TEST_DB)

        self.assertIsNotNone(result['breakfast'])
        self.assertEqual(result['breakfast'][0], "Healthy Breakfast")
        self.assertIsNotNone(result['lunch'])
        self.assertEqual(result['lunch'][0], "Light Lunch")
        self.assertIsNotNone(result['dinner'])
        self.assertEqual(result['dinner'][0], "Dinner Plan")

    def test_get_meal_plan_no_match(self):
        """Тест на случай, если подходящих продуктов нет"""
        add_meal_plans(18, 30, 18.5, 24.9, "Healthy Breakfast", "breakfast", "oats, milk", db_name=TEST_DB)
        add_meal_plans(18, 30, 18.5, 24.9, "Light Lunch", "lunch", "salad, chicken", db_name=TEST_DB)

        # Передаем список продуктов, который не соответствует ни одному плану
        result = get_meal_plan(25, 22.0, ["bread", "butter"], db_name=TEST_DB)
        self.assertIsNotNone(result['breakfast'])
        self.assertEqual(result['breakfast'][0], "Healthy Breakfast")  # Возьмется первый завтрак

        self.assertIsNotNone(result['lunch'])
        self.assertEqual(result['lunch'][0], "Light Lunch")  # Возьмется первый обед
