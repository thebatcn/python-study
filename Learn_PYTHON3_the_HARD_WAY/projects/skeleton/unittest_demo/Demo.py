import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def testDivide01(self):
        cal = Calculator()
        result = cal.divide(10, 2)
        self.assertEqual(result, 5)

    def testDivide02(self):
        cal = Calculator()
        result = cal.divide(10 ,0.5)
        self.assertEqual(result, 20)

    def testDivide03(self):
        cal = Calculator()
        result = cal.divide(10, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
