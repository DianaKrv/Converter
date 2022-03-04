import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_choice(self):
        self.assertEqual("Выбрано 1: Ru", choice(1))
        self.assertEqual("Выбрано 2: Eng", choice(2))




    if __name__ == '__main__':
        unittest.main()
