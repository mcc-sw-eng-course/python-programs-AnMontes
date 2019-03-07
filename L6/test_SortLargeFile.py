import unittest
import SortLargeFile


class TestSortLargeFile(unittest.TestCase):

    def test_set_input_data_filename(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(ValueError):
            obj.set_input_data(235, ',')

    def test_set_input_data_delimiter(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(ValueError):
            obj.set_input_data("large_csv.csv", 'w')

    def test_set_input_data_exist(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(Exception):
            obj.set_input_data("Hola", ',')

    def test_set_input_data_array(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        self.assertEqual(obj.data_array, [5, 4, 3, 2])

    def test_set_output_data_not_input_state(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(Exception):
            obj.set_output_data("large_csv.csv", ',')

    def test_set_output_data_string(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        with self.assertRaises(ValueError):
            obj.set_output_data(200, ',')

    def test_set_output_data_string2(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        obj.set_output_data("outputcsv.csv", ',')

    def test_execute_merge_sort(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(Exception):
            obj.execute_merge_sort()

    def test_merge_sort(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        obj.merge_sort(obj.data_array)
        self.assertEqual(obj.data_array, [2, 3, 4, 5])

    def test_execute_heap_sort(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(Exception):
            obj.execute_heap_sort()

    def test_heap_sort(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        obj.heap_sort(obj.data_array)
        self.assertEqual(obj.data_array, [2, 3, 4, 5])

    def test_execute_quick_sort(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(Exception):
            obj.execute_quick_sort()

    def test_quick_sort(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        obj.quick_sort(obj.data_array)
        self.assertEqual(obj.quick_sort(obj.data_array), [2, 3, 4, 5])

    def test_get_performance_data(self):
        obj = SortLargeFile.SortLargeCsv()
        obj.set_input_data("large_csv - copia.csv", ',')
        obj.heap_sort(obj.data_array)
        self.assertIsNot(obj.get_performance_data,None)


if __name__ == '__main__':
    unittest.main()
