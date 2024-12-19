import tkinter as tk
from project import add_new_train
import unittest
from unittest.mock import patch


class TestAddNewTrain(unittest.TestCase):

    @patch('project.add_train_plans')
    def test_add_new_train_age_bmi(self, mock_add_train_plans):
        
        age = 18
        bmi = 15
        new_train_plan = "Train plan description"
        gendr = "Male"
        
        add_new_train(age, bmi, new_train_plan, gendr)

        mock_add_train_plans.assert_called_once_with(16, 20, 10, 20, 'Train_3', gendr, new_train_plan)

        age = 22
        bmi = 22.5
        
        add_new_train(age, bmi, new_train_plan, gendr)

        mock_add_train_plans.assert_called_with(21, 25, 20.1, 25, 'Train_3', gendr, new_train_plan)

        age = 28
        bmi = 30
        
        add_new_train(age, bmi, new_train_plan, gendr)

        mock_add_train_plans.assert_called_with(26, 30, 25.1, 35, 'Train_3', gendr, new_train_plan)

        age = 34
        bmi = 18
        
        add_new_train(age, bmi, new_train_plan, gendr)

        mock_add_train_plans.assert_called_with(31, 35, 10, 20, 'Train_3', gendr, new_train_plan)

if __name__ == '__main__':
    unittest.main()
