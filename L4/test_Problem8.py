import unittest
import Problem8
import statistics
import math
import numpy

class TestProblem8(unittest.TestCase):

    def test_mean_float_array(self):
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.mean(), 5.111, 2)

    def test_mean_int_array(self):
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.mean(), 5)

    def test_mean_str_array(self):
        i_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_mean_irr_array(self):
        i_numbers = [math.pi, math.e, 3, 4, 5, 6, 7, 8, 10]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.mean(), 5.428, 2)

    def test_mean_lesser_than_max(self):
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        obj = Problem8.Statistics(i_numbers)
        self.assertLessEqual(obj.mean(), max(i_numbers))

    def test_mean_greater_than_max(self):
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 10]
        obj = Problem8.Statistics(i_numbers)
        self.assertGreaterEqual(obj.mean(), min(i_numbers))

    def test_mean_empty(self):
        i_numbers = []
        with self.assertRaises(ZeroDivisionError):
            obj = Problem8.Statistics(i_numbers)

    def test_mean_float(self):
        i_numbers = 2.4444
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_mean_int(self):
        i_numbers = 2
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_mean_str(self):
        i_numbers = "2"
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_mean_irr(self):
        i_numbers = math.pi
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_mean_crosscheck(self):
        i_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(statistics.mean(i_numbers), obj.mean())

    #     STD_DEV

    def test_std_dev_float_array(self):
        i_numbers = [1, 2, 3, 4.66, 5, 6.555555, 7.3, 8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.std_dev(), 3.111, 2)

    def test_std_dev_float_array_negative(self):
        i_numbers = [-1, -2, -3, 4.66, 5, -6.555555, 7.3, 8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.std_dev(), 5.893, 2)

    def test_std_dev_int_array(self):
        i_numbers = [1, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.std_dev(), 3.073, 2)

    def test_std_dev_int_array_negative(self):
        i_numbers = [-11, 2, 9, -4, 10, -6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.std_dev(), 7.512, 2)

    def test_std_dev_str_array(self):
        i_numbers = ["1", "2", "9", "4", "10", "6", "7", "8", "5"]
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_std_dev_irr_array(self):
        i_numbers = [math.pi, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.std_dev(), 2.719, 2)

    def test_std_dev_empty(self):
        i_numbers = []
        with self.assertRaises(ZeroDivisionError):
            obj = Problem8.Statistics(i_numbers)

    def test_std_dev_float(self):
        i_numbers = 1.77777
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_std_dev_int(self):
        i_numbers = 1
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_std_dev_irr(self):
        i_numbers = math.pi
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_std_dev_crosscheck(self):
        i_numbers = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.std_dev(), statistics.stdev(i_numbers), 3)

#         MEDIAN

    def test_median_float_array(self):
        i_numbers = [1, 2, 3, 4.66, 5, 6.555555, 7.3, 8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.median(), 5)

    def test_median_float_array_negative(self):
        i_numbers = [-1, -2, -3, 4.66, 5, -6.555555, 7.3, 8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.median(), 4.66)

    def test_median_int_array(self):
        i_numbers = [1, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.median(), 6)

    def test_median_int_negative(self):
        i_numbers = [-11, 2, 9, -4, 10, -6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.median(), 5)

    def test_median_str_array(self):
        i_numbers = ["1", "2", "9", "4", "10", "6", "7", "8", "5"]
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_median_irr_array(self):
        i_numbers = [math.pi, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.median(), 6)

    def test_median_empty(self):
        i_numbers = []
        with self.assertRaises(ZeroDivisionError):
            obj = Problem8.Statistics(i_numbers)

    def test_median_float(self):
        i_numbers = 1.77777
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_median_int(self):
        i_numbers = 1
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_median_irr(self):
        i_numbers = math.pi
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_median_crosscheck_even(self):
        i_numbers = [1.5, 2.5, 2.5, 2.75, 3.25, 4.75]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.median(), statistics.median(i_numbers))

    def test_median_crosscheck_odd(self):
        i_numbers = [1.5, 2.5, 2.5, 2.75, 3.25]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.median(), statistics.median(i_numbers))

#     n_quartil

    def test_n_quartil_float_array(self):
        i_numbers = [1, 2, 3, 4.66, 5, 6.555555, 7.3, 8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_quartil(1), 3)
        self.assertEqual(obj.n_quartil(2), 5)
        self.assertEqual(obj.n_quartil(3), 7.3)

    def test_n_quartil_float_array_negative(self):
        i_numbers = [1, 2, 3, -4.66, 5, -6.555555, -7.3, -8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_quartil(1), -6.555555)
        self.assertEqual(obj.n_quartil(2), 1)
        self.assertEqual(obj.n_quartil(3), 3)

    def test_n_quartil_int_array(self):
        i_numbers = [1, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_quartil(1), 4)
        self.assertEqual(obj.n_quartil(2), 6)
        self.assertEqual(obj.n_quartil(3), 8)

    def test_n_quartil_int_array_negative(self):
        i_numbers = [1, 2, -9, 4, -10, 6, -7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_quartil(1), -7)
        self.assertEqual(obj.n_quartil(2), 2)
        self.assertEqual(obj.n_quartil(3), 5)

    def test_n_quartil_str_array(self):
        i_numbers = ["1", "2", "9", "4", "10", "6", "7", "8", "5"]
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_quartil_irr_array(self):
        i_numbers = [math.pi, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.median(), 6)

    def test_n_quartil_empty(self):
        i_numbers = []
        with self.assertRaises(ZeroDivisionError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_quartil_float(self):
        i_numbers = 1.77777
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_quartil_int(self):
        i_numbers = 1
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_quartil_irr(self):
        i_numbers = math.pi
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

#     PERCENTIL

    def test_n_percentil_float_array(self):
        i_numbers = [1, 2, 3, 4.66, 5, 6.555555, 7.3, 8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_percentil(60), 5)
        self.assertEqual(obj.n_percentil(34), 3)

    def test_n_percentil_float_array_negative(self):
        i_numbers = [1, 2, 3, -4.66, 5, -6.555555, -7.3, -8.5, 10.45]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_percentil(60), 1)
        self.assertEqual(obj.n_percentil(34), -6.555555)

    def test_n_percentil_int_array(self):
        i_numbers = [1, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_percentil(60), 6)
        self.assertEqual(obj.n_percentil(34), 4)

    def test_n_percentil_int_array_negative(self):
        i_numbers = [1, 2, -9, 4, -10, 6, -7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertEqual(obj.n_percentil(60), 2)
        self.assertEqual(obj.n_percentil(34), -7)

    def test_n_percentil_str_array(self):
        i_numbers = ["1", "2", "9", "4", "10", "6", "7", "8", "5"]
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_percentil_irr_array(self):
        i_numbers = [math.pi, 2, 9, 4, 10, 6, 7, 8, 5]
        obj = Problem8.Statistics(i_numbers)
        self.assertAlmostEqual(obj.median(), 6)

    def test_n_percentil_empty(self):
        i_numbers = []
        with self.assertRaises(ZeroDivisionError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_percentil_float(self):
        i_numbers = 1.77777
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_percentil_int(self):
        i_numbers = 1
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)

    def test_n_percentil_irr(self):
        i_numbers = math.pi
        with self.assertRaises(TypeError):
            obj = Problem8.Statistics(i_numbers)


if __name__ == '__main__':
    unittest.main()