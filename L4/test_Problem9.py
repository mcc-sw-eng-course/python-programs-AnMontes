import unittest
from Problem9 import roman

class TestProblem9(unittest.TestCase):

    def test_roman_conversion(self):
        number = 100
        self.assertEqual(roman(number), "c")
        number = 3999999
        self.assertEqual(roman(number), "MMMCMXCIXcmxcix")
        number = 400000
        self.assertEqual(roman(number), "CD")

    def test_exceeds_max(self):
        number = 4000000
        self.assertEqual(roman(number),"Exceeds max.")

    def test_exceed_min(self):
        number = -10
        self.assertEqual(roman(number), "Exceeds min.")

    def test_not_int(self):
        number="mil"
        with self.assertRaises(TypeError):
            roman(number)

    def test_none_value(self):
        number = None
        with self.assertRaises(TypeError):
            roman(number)

    def test_array_value(self):
        number = [1,2,3]
        with self.assertRaises(TypeError):
            roman(number)

if __name__ == '__main__':
    unittest.main()