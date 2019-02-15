import unittest
import Problem14


class TestProblem14(unittest.TestCase):

    def test_add_item(self):
        obj = Problem14.MyPowerClass()
        obj.add_item(5)
        obj.save_to_text_file("test1")
        self.assertEqual(obj.read_from_text_file("test1"), [5])

    def test_remove_item(self):
        obj = Problem14.MyPowerClass()
        obj.add_item(5)
        obj.remove_item(1)
        obj.save_to_text_file("test1")
        self.assertEqual(obj.read_from_text_file("test1"), [])

    def test_sort_list(self):
        obj = Problem14.MyPowerClass()
        obj.add_item(5)
        obj.add_item(3)
        obj.add_item(1)
        obj.sort_list()
        obj.save_to_text_file("test1")
        self.assertEqual(obj.read_from_text_file("test1"), [1,3,5])

    def test_l_merge(self):
        obj1 = Problem14.MyPowerClass()
        obj1.add_item(5)
        obj1.add_item(5)
        obj1.add_item(5)
        obj1.l_merge([3,3,3])
        obj1.save_to_text_file("test1")
        self.assertEqual(obj1.read_from_text_file("test1"), [3,3,3,5,5,5])

    def test_r_merge(self):
        obj1 = Problem14.MyPowerClass()
        obj1.add_item(5)
        obj1.add_item(5)
        obj1.add_item(5)
        obj1.r_merge([3, 3, 3])
        obj1.save_to_text_file("test1")
        self.assertEqual(obj1.read_from_text_file("test1"), [5,5,5,3,3,3])

    def test_not_an_int_or_float(self):
        obj = Problem14.MyPowerClass()
        with self.assertRaises(TypeError):
            obj.add_item("Hola")

    def test_index_limits(self):
        obj = Problem14.MyPowerClass()
        with self.assertRaises(ValueError):
            obj.remove_item(1)

    def test_not_int_or_float_in_merge(self):
        obj = Problem14.MyPowerClass()
        with self.assertRaises(ValueError):
            obj.l_merge(["hola"])

    def test_not_string_save(self):
        obj = Problem14.MyPowerClass()
        with self.assertRaises(TypeError):
            obj.save_to_text_file(5)

    def test_not_string_read(self):
        obj = Problem14.MyPowerClass()
        with self.assertRaises(TypeError):
            obj.read_from_text_file(5)

if __name__ == '__main__':
    unittest.main()


