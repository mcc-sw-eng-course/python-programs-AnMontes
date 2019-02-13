import unittest
import Problem8

class TestProblem8(unittest.TestCase):

    def test_mean_float(self):
        # i_numbers = [7, 8, 5.8, 2, 4.3, 4, 6, 3, 1.5, 8, 10]
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.mean(), 5.111, 2)

    def test_mean_int(self):
        # i_numbers = [7, 8, 5.8, 2, 4.3, 4, 6, 3, 1.5, 8, 10]
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.mean(), 5)


if __name__ == '__main__':
    unittest.main()