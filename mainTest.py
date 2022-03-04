import unittest
from main import *

class MyTestCase(unittest.TestCase):
    def test_choice(self):
        self.assertEqual("Выбрано 1: Ru", choice(1))
        self.assertEqual("Выбрано 2: Eng", choice(2))

    #def test_convertToRu(self):
        #self.assertEqual(1, convertToRu())
        #self.assertEqual(2, convertToRu())


    #def test_convertToEng(self):
        #self.assertEqual(1, convertToEng())
        #self.assertEqual(2, convertToEng())






    if __name__ == '__main__':
        unittest.main()
