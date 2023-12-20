import unittest
from CalculateFactorial import CalculateFactorial

class TestFactorialFunction(unittest.TestCase):

    def test_factorial_of_zero(self):
        calc_factorial = CalculateFactorial()
        result = calc_factorial.CalculateFactorial(0)
        self.assertEqual(result, 1)
        print(f"Test factorial_of_zero passed. Result: {calc_factorial.GetFactorial()}")

    def test_factorial_of_one(self):
        calc_factorial = CalculateFactorial()
        result = calc_factorial.CalculateFactorial(1)
        self.assertEqual(result, 1)
        print(f"Test factorial_of_one passed. Result: {calc_factorial.GetFactorial()}")

    def test_factorial_of_positive_integer(self):
        calc_factorial = CalculateFactorial()
        result = calc_factorial.CalculateFactorial(5)
        self.assertEqual(result, 120)
        print(f"Test factorial_of_positive_integer passed. Result: {calc_factorial.GetFactorial()}")

        # Додам невдалий тест для ілюстрації
        with self.assertRaises(AssertionError):
            self.assertEqual(calc_factorial.GetFactorial(), 121)
            print(f"Test factorial_of_positive_integer with error. Result: {calc_factorial.GetFactorial()}")

    def test_factorial_of_large_number(self):
        calc_factorial = CalculateFactorial()
        result = calc_factorial.CalculateFactorial(20)
        self.assertEqual(result, 2432902008176640000)
        print(f"Test factorial_of_large_number passed. Result: {calc_factorial.GetFactorial()}")

    def test_factorial_of_negative_integer(self):
        calc_factorial = CalculateFactorial()
        with self.assertRaises(ValueError):
            calc_factorial.CalculateFactorial(-5)
        print("Test factorial_of_negative_integer passed. Result: ValueError (as expected)")

    def test_factorial_of_decimal_number(self):
        calc_factorial = CalculateFactorial()
        with self.assertRaises(ValueError):
            calc_factorial.CalculateFactorial(5.5)
        print("Test factorial_of_decimal_number passed. Result: ValueError (as expected)")

if __name__ == '__main__':
    unittest.main()



