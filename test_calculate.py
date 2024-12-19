import unittest
from project import calculate_nutritional_value

class TestBusinessLogicLayer(unittest.TestCase):
    def test_calculate_nutritional_value_success(self):
        product_list = [("Apple", 150), ("Banana", 100)]
        product_data = {"apple": (52, 0.3, 0.2, 14), "banana": (96, 1.3, 0.3, 27)}

        result = calculate_nutritional_value(product_list, product_data)

        expected = {
            "kilocalories": 150 * 52 / 100 + 100 * 96 / 100,  
            "proteins": round(150 * 0.3 / 100 + 100 * 1.3 / 100, 2),  
            "fats": round(150 * 0.2 / 100 + 100 * 0.3 / 100, 2), 
            "carbohydrates": round(150 * 14 / 100 + 100 * 27 / 100, 2)  
        }
        self.assertEqual(result, expected)

    def test_calculate_nutritional_value_product_not_found(self):
        product_list = [("Orange", 100)]
        product_data = {"apple": (52, 0.3, 0.2, 14)}

        with self.assertRaises(KeyError) as context:
            calculate_nutritional_value(product_list, product_data)
        self.assertIn("Product 'Orange' not found", str(context.exception))

if __name__ == "__main__":
    unittest.main()
