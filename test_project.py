import sqlite3
import unittest
from db import insert_data_1, insert_data_2
from unittest.mock import MagicMock, Mock

import pytest
from project import open_hello_window()

def test_open_hello_window_success(mock_tk, mock_photoimage):
    mock_window = Mock() 
    mock_tk.return_value = mock_window 
    mock_photoimage.return_value = Mock() 
    open_hello_window() 
    mock_tk.assert_called_once()

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
        
        insert_data_2(self.connection, meal_plans) 
        
        self.cursor.execute("SELECT COUNT(*) FROM MealPlans")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_insert_data_duplicate(self):
        meal_plans = [
            (18, 25, 18.5, 24.9, 'Healthy Plan', 'Breakfast', 'Eggs, Toast'),
            (26, 35, 25.0, 29.9, 'Balanced Plan', 'Lunch', 'Chicken Salad')
        ]
        
        insert_data_2(self.connection, meal_plans)  
        insert_data_2(self.connection, meal_plans)  
        
        self.cursor.execute("SELECT COUNT(*) FROM MealPlans")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 2)

if __name__ == '__main__':
    unittest.main()


def test_successful_insertion(mocker):
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mocker.patch('sqlite3.connect', return_value=mock_connection)

    test_products = [
        ("Apple", 52.0, 0.3, 0.2, 14.0, 100.0),
        ("Banana", 96.0, 1.2, 0.3, 23.0, 120.0),
    ]
    insert_data_1(test_products)

    mock_cursor.executemany.assert_called_once_with(
        """
                        INSERT OR IGNORE INTO Products 
                        (name, kilocalories, protein_gramms, fat_gramms, carbohydrates_gramms, serving_size_gramms) 
                        VALUES (?, ?, ?, ?, ?, ?)""",
         test_products
    )

    mock_connection.commit.assert_called_once()


def test_empty_product_list(mocker):
     mock_cursor = MagicMock()
     mock_connection = MagicMock()
     mock_connection.cursor.return_value = mock_cursor
     mocker.patch('sqlite3.connect', return_value=mock_connection)

     insert_data_1([])

     mock_cursor.executemany.assert_not_called()
     mock_connection.commit.assert_called_once()

def test_insertion_failure(mocker):
    mock_cursor = MagicMock()
    mock_connection = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    mocker.patch('sqlite3.connect', return_value=mock_connection)

    mock_cursor.executemany.side_effect = sqlite3.Error("Simulated error")

    test_products = [("Apple", 52.0, 0.3, 0.2, 14.0, 100.0)]
    with pytest.raises(sqlite3.Error):
      insert_data_1(test_products)
    mock_connection.commit.assert_not_called()
    mock_cursor.executemany.assert_called_once()