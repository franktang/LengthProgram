import unittest
from src.MyLength import MyLength

class Test(unittest.TestCase):
    def testHappyFow(self):
        self.assertTrue(True)

    def test1mileEqual1mile(self):

        lenObj1 = MyLength(1, "mile")
        lenObj2 = MyLength(1, "mile")

        self.assertTrue(lenObj1.equals(lenObj2))

    def test1mileShouldNotEqual2Mile(self):
        lenObj1 = MyLength(1, "mile")
        lenObj2 = MyLength(2, "mile")

        self.assertFalse(lenObj1.equals(lenObj2))

    def test1feetShouldNotEqual1inch(self):
        lenObj1 = MyLength(1, "feet")
        lenObj2 = MyLength(1, "inch")

        self.assertFalse(lenObj1.equals(lenObj2))

    def test1MileShouldEqual1760Yard(self):
        lenObj1 = MyLength(1, "mile")
        lenObj2 = MyLength(1176, "yard")

        self.assertTrue(lenObj1.equals(lenObj2))

if __name__ == '__main__':
    unittest.main(verbosity=2)