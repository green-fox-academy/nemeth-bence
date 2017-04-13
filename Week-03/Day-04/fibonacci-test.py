import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
            self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_first(self):
            self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_seventh(self):
            self.assertEqual(fibonacci(7), 13)

    def test_fibonacci_seventeenth(self):
            self.assertEqual(fibonacci(17), 1597)
if __name__ == '__main__':
    unittest.main()
