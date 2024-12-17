import sqlite3
import unittest
from unittest.mock import patch, MagicMock

import tkinter as tk

from project import open_hello_window, open_parametrs_window
from db import insert_data_2


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


class TestOpenHelloWindow(unittest.TestCase):
    @patch("tkinter.PhotoImage")
    @patch("tkinter.Label")
    @patch("tkinter.Button")
    @patch("tkinter.font.Font")
    def test_open_hello_window_success(self, mock_font, mock_button, mock_label, mock_photo):
        """
        Тест успешного создания приветственного окна.
        """
        # Create a real root window but hide it
        root = tk.Tk()
        root.withdraw()

        # Mock PhotoImage and other widgets
        mock_photo.return_value = MagicMock()

        # Call the function
        open_hello_window()

        # Verify that fonts and widgets were created
        self.assertEqual(mock_font.call_count, 2)
        mock_label.assert_called_once()
        mock_button.assert_called_once()

        # Clean up the root window
        root.destroy()

    @patch("tkinter.PhotoImage", side_effect=tk.TclError)
    def test_open_hello_window_logo_not_found(self, mock_photo):
        """
        Тест случая, когда файл logo.png отсутствует.
        """
        # Create a real root window but hide it
        root = tk.Tk()
        root.withdraw()

        with patch("builtins.print") as mock_print:
            open_hello_window()
            mock_print.assert_called_once_with("Warning: logo.png not found.")

        # Clean up the root window
        root.destroy()

class TestOpenParametrsWindow(unittest.TestCase):

    @patch("tkinter.Tk")
    @patch("tkinter.PhotoImage")
    @patch("tkinter.Label")
    @patch("tkinter.Entry")
    @patch("tkinter.OptionMenu")
    @patch("tkinter.Button")
    @patch("tkinter.font.Font")
    def test_open_parametrs_window_success(self, mock_font, mock_button, mock_optionmenu,
                                           mock_entry, mock_label, mock_photo, mock_tk):
        """
        Тест успешного создания окна параметров и его компонентов.
        """
        # Mock Tk root window
        mock_window = MagicMock()
        mock_tk.return_value = mock_window

        # Mock PhotoImage
        mock_photo.return_value = MagicMock()

        # Call the function
        open_parametrs_window()

        # Assertions: ensure window and widgets are created
        mock_tk.assert_called_once()
        mock_window.title.assert_called_once_with("Ваши параметры")
        mock_window.geometry.assert_called_once_with("300x300+600+200")

        # Verify PhotoImage is called with master
        mock_photo.assert_called_once_with(master=mock_window, file='logo.png')

        # Check that fonts, labels, entries, and buttons were created
        self.assertEqual(mock_font.call_count, 3)
        mock_label.assert_called()
        mock_entry.assert_called()
        mock_optionmenu.assert_called()
        mock_button.assert_called()

    @patch("tkinter.Tk")
    @patch("tkinter.PhotoImage")
    @patch("tkinter.Entry")
    @patch("tkinter.StringVar")
    @patch("tkinter.Button")
    @patch("builtins.print")
    def test_save_data_bmi_calculation(self, mock_print, mock_button, mock_stringvar, mock_entry, mock_photo, mock_tk):
        """
        Тест проверки сохранения данных и вычисления ИМТ.
        """
        # Mock Tk root window
        mock_window = MagicMock()
        mock_tk.return_value = mock_window

        # Mock entry fields
        mock_entry.side_effect = [
            MagicMock(get=MagicMock(return_value="170")),  # height
            MagicMock(get=MagicMock(return_value="70")),   # weight
            MagicMock(get=MagicMock(return_value="25"))    # age
        ]

        # Mock StringVar for gender
        mock_gendr_var = MagicMock()
        mock_gendr_var.get.return_value = "Мужской"

        # Mock PhotoImage
        mock_photo.return_value = MagicMock()

        # Capture the Button command argument
        button_command = None

        def mock_button_init(*args, **kwargs):
            nonlocal button_command
            if "command" in kwargs:
                button_command = kwargs["command"]

        mock_button.side_effect = mock_button_init

        with patch("project.open_main_menu") as mock_open_main_menu:
            open_parametrs_window()

            # Simulate pressing the save button
            if button_command:
                button_command()

            # Assert correct BMI calculation and printed output
            mock_print.assert_called_with("Рост: 170.0 см, Вес: 70.0 кг, Возраст: 25.0, Пол: Мужской, ИМТ: 24.2")
            mock_open_main_menu.assert_called_once()

        # Verify PhotoImage was called correctly
        mock_photo.assert_called_once_with(master=mock_window, file="logo.png")


    @patch("tkinter.Tk")
    @patch("tkinter.PhotoImage")
    @patch("tkinter.Entry")
    @patch("tkinter.StringVar")
    @patch("tkinter.Button")
    @patch("builtins.print")
    def test_save_data_bmi_calculation(self, mock_print, mock_button, mock_stringvar, mock_entry, mock_photo, mock_tk):
        """
        Тест проверки сохранения данных и вычисления ИМТ.
        """
        # Mock Tk root window
        mock_window = MagicMock()
        mock_tk.return_value = mock_window

        # Mock entry fields
        mock_entry.side_effect = [
            MagicMock(get=MagicMock(return_value="170")),  # height
            MagicMock(get=MagicMock(return_value="70")),   # weight
            MagicMock(get=MagicMock(return_value="25"))    # age
        ]

        mock_gendr_var_instance = MagicMock()
        mock_gendr_var_instance.get.return_value = "Мужской"
        mock_stringvar.return_value = mock_gendr_var_instance


# Mock PhotoImage
        mock_photo.return_value = MagicMock()

        # Ensure Button returns a mock object with a .grid method
        mock_button_instance = MagicMock()
        mock_button.return_value = mock_button_instance

        # Capture the Button command argument
        button_command = None

        def mock_button_init(*args, **kwargs):
            nonlocal button_command
            if "command" in kwargs:
                button_command = kwargs["command"]
            return mock_button_instance

        mock_button.side_effect = mock_button_init

        # Mock open_main_menu to verify it gets called
        with patch("project.open_main_menu") as mock_open_main_menu:
            open_parametrs_window()

            # Simulate pressing the save button
            if button_command:
                button_command()

            # Assert correct BMI calculation and printed output
            mock_print.assert_called_with("Рост: 170.0 см, Вес: 70.0 кг, Возраст: 25.0, Пол: Мужской, ИМТ: 20.0")
            mock_open_main_menu.assert_called_once()

        # Verify PhotoImage was called correctly
        mock_photo.assert_called_once_with(master=mock_window, file="logo.png")
        mock_button_instance.grid.assert_called_once_with(row=5, column=1, columnspan=2, padx=30, pady=10, sticky="w")



if __name__ == '__main__':
    unittest.main()
