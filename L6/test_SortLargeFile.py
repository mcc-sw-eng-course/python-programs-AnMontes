import unittest
import SortLargeFile


class TestSortLargeFile(unittest.TestCase):

    def test_set_input_data(self):
        obj = SortLargeFile.SortLargeCsv()
        with self.assertRaises(ValueError):
            obj.set_input_data(235, ',')

        with self.assertRaises(ValueError):
            obj.set_input_data("")


