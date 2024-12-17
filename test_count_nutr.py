import unittest
from unittest.mock import patch, MagicMock
import sqlite3
import os
from count_nutritional_value import add_newfoods, counter_nutritional_value

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
        add_newfoods("Apple", 52, 0.3, 0.2, 14.0, 100, dbname=TEST_DB, run_counter=False)
        self.cursor.execute("SELECT * FROM Products WHERE name = 'Apple'")
        result = self.cursor.fetchone()

        self.assertIsNotNone(result)
        self.assertEqual(result[1], "Apple")  # Проверка имени продукта
        self.assertEqual(result[2], 52)  # Проверка килокалорий
        self.assertEqual(result[3], 0.3)  # Проверка белков

    @patch('count_nutritional_value.input', side_effect=["q"])  # Сразу завершаем функцию
    def test_counter_nutritional_value_no_products(self, mock_input):
        """Тест подсчета без продуктов"""
        with patch('builtins.print') as mock_print:
            result = counter_nutritional_value()
            self.assertEqual(result, (0, 0, 0, 0))
            mock_print.assert_any_call("Ваши килокалории за день: ", 0)

    @patch('count_nutritional_value.input', side_effect=["Apple", "150", "q"])
    def test_counter_nutritional_value_with_product(self, mock_input):
        """Тест подсчета пищевой ценности с добавленным продуктом"""
        self.cursor.execute(
            "INSERT INTO Products (name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            ("Apple", 52, 0.3, 0.2, 14.0, 100)
        )
        self.connection.commit()

        with patch('builtins.print') as mock_print:
            result = counter_nutritional_value()
            self.assertEqual(result, (78.0, 0.45, 0.3, 21.0))  # Проверка на 150 г
            mock_print.assert_any_call("Ваши килокалории за день: ", 78.0)
            mock_print.assert_any_call("Ваши белки за день: ", 0.45)
            mock_print.assert_any_call("Ваши жиры за день: ", 0.3)
            mock_print.assert_any_call("Ваши углеводы за день: ", 21.0)


if __name__ == '__main__':
    unittest.main()
