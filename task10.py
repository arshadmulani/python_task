def factorial(n):
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

import unittest
class TestFactorial(unittest.TestCase):
    def test_factorial_positive(self):
        self.assertEqual(factorial(5),120)
        print("Test Passed for input 5")
    def test_factorial_zero(self):
        self.assertEqual(factorial(0),1)
        print("Test Passed for input 0")
    def test_factorial_one(self):
        self.assertEqual(factorial(1),1)
        print("Test Passed for input 1")
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
             factorial(-1)
if __name__=='__main__':
    unittest.main()
