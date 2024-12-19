
from project import from_par_to_main
import unittest
from unittest.mock import patch, MagicMock


class TestFromParToMain(unittest.TestCase):

    @patch('project.parametrs_window', new_callable=MagicMock)
    @patch('project.open_main_menu')
    def test_from_par_to_main(self, mock_open_main_menu, mock_parametrs_window):
        # Убедитесь, что destroy вызывается на объекте parametrs_window
        from_par_to_main()

        # Проверяем, что destroy был вызван
        mock_parametrs_window.destroy.assert_called_once()

        # Проверяем, что open_main_menu был вызван
        mock_open_main_menu.assert_called_once()

if __name__ == '__main__':
    unittest.main()
