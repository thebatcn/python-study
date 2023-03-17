import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def testDivide01(self):
        cal = Calculator()
        result = cal.divide(10, 2)
        self.assertEqual(result, 5)

    def testDivide02(self):
        cal = Calculator()
        result = cal.divide(20, 0.5)
        self.assertEqual(result, 40)


if __name__ == '__main__':
    unittest.main()
