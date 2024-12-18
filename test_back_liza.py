import unittest
from unittest.mock import patch, MagicMock
from project import back_to_add_data_window3, back_to_add_data_window1





class TestBackToDataWindow3(unittest.TestCase):

    @patch('project.counter_kcal_window', new_callable=MagicMock)
    @patch('project.main_window', new_callable=MagicMock)
    def test_back_to_add_data_window3(self, mock_main_window, mock_counter_kcal_window):
        back_to_add_data_window3()

    
        mock_counter_kcal_window.destroy.assert_called_once()
        mock_main_window.deiconify.assert_called_once()


class TestBackToAddDataWindow1(unittest.TestCase):
    @patch('project.add_newfood_window', new_callable=MagicMock)
    @patch('project.add_data_window', new_callable=MagicMock)
    def test_back_to_add_data_window1(self, mock_add_data_window, mock_add_newfood_window):
        # Arrange
        mock_add_newfood_window.is_add_newfood_window_open = True

        # Act
        back_to_add_data_window1()

        # Assert
        mock_add_newfood_window.destroy.assert_called_once()
        mock_add_data_window.deiconify.assert_called_once()





if __name__ == '__main__':
    unittest.main()