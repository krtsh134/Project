import unittest
from unittest.mock import patch
import sqlite3
import os
from count_nutritional_value import add_newfoods

TEST_DB = 'test_health_control.db'


class TestNutritionalFunctions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Создание тестовой базы данных перед выполнением всех тестов"""
        cls.connection = sqlite3.connect(TEST_DB)
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                kilocalories FLOAT,
                protein_gramms FLOAT,
                fat_gramms FLOAT,
                carbohydrates_gramms FLOAT,
                serving_size_gramms FLOAT
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
        self.cursor.execute("DELETE FROM Products")
        self.connection.commit()

    def test_add_newfoods(self):
        """Тест добавления нового продукта в базу данных"""
        add_newfoods("Яблоко", 47, 0.4, 0.4, 9.8, 100, dbname=TEST_DB)
        self.cursor.execute("SELECT * FROM Products WHERE name = 'Яблоко'")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Яблоко")  
        self.assertEqual(result[2], 47)  
        self.assertEqual(result[3], 0.4)  



if __name__ == '__main__':
    unittest.main()
