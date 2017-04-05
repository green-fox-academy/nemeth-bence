import unittest
from bence_nemeth_work import *

class TestApple(unittest.TestCase):
    def test_get_apple(self):
        apple = Apple()
        self.assertEqual(apple.get_apple(), "apple")


    def test_result(self):
        sum = Apple([4,5,6])
        self.assertEqual(sum.get_sum(), 15 )


    def test_anagram(self):
        check = Apple()
        self.assertEqual(check.anagram("buda", "abud"))





if __name__ == '__main__':
    unittest.main()
