import unittest
from unittest.mock import patch, MagicMock
from project import calculate_and_display
import tkinter as tk
from project import messagebox

product_list=MagicMock([])
class TestCalculateAndDisplay(unittest.TestCase):
    def setUp(self):
        product_list.clear()
        self.result_label = MagicMock(spec=tk.Label)
        self.product_listbox = MagicMock(spec=tk.Listbox)

    @patch('project.fetch_products_from_db')
    @patch('project.calculate_nutritional_value')
    @patch('project.messagebox')
    def test_calculate_and_display_success(self, mock_messagebox, mock_calculate, mock_fetch):
        mock_fetch.return_value = {
            'Apple': {'kilocalories': 52, 'proteins': 0.26, 'fats': 0.17, 'carbohydrates': 14},
            'Banana': {'kilocalories': 89, 'proteins': 1.09, 'fats': 0.33, 'carbohydrates': 22.84}
        }
        mock_calculate.return_value = {
            'kilocalories': 141,
            'proteins': 1.35,
            'fats': 0.50,
            'carbohydrates': 36.84
        }
        product_list.extend([('Apple', 100), ('Banana', 200)])
        calculate_and_display()
        expected_result_text = (
            "Килокалории: 141\n"
            "Белки: 1.35\n"
            "Жиры: 0.50\n"
            "Углеводы: 36.84"
        )
        self.result_label.config.assert_called_once_with(text=expected_result_text)
        self.assertEqual(product_list, [])
        self.product_listbox.delete.assert_called_once_with(0, tk.END)
        mock_messagebox.assert_not_called()

    @patch('project.fetch_products_from_db')
    @patch('project.messagebox')
    def test_calculate_and_display_key_error(self, mock_messagebox, mock_fetch):
        
        mock_fetch.return_value = {
            'Apple': {'kilocalories': 52, 'proteins': 0.26, 'fats': 0.17},  # carbohydrates отсутствует
            'Banana': {'kilocalories': 89, 'proteins': 1.09, 'fats': 0.33, 'carbohydrates': 22.84}
        }

        product_list.extend([('Apple', 100), ('Banana', 200)])
        calculate_and_display()
        mock_messagebox.showerror.assert_called_once_with("Product Error", "'carbohydrates'")
        self.assertEqual(product_list, [])
        self.product_listbox.delete.assert_called_once_with(0, tk.END)

    @patch('project.fetch_products_from_db')
    @patch('project.messagebox')
    def test_calculate_and_display_general_exception(self, mock_messagebox, mock_fetch):
        mock_fetch.side_effect = Exception("Test General Error")
        product_list.extend([('Apple', 100), ('Banana', 200)])

        calculate_and_display()

        mock_messagebox.showerror.assert_called_once_with("Error", "Test General Error")
        self.assertEqual(product_list, [])
        self.product_listbox.delete.assert_called_once_with(0, tk.END)

if __name__ == '__main__':
    unittest.main()