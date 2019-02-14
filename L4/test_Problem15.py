import unittest
import Problem15


class TestProblem15(unittest.TestCase):

    def test_constructor_expected_output(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        self.assertEqual(direct.directory[0]['name'], "Antonio")
        self.assertEqual(direct.directory[0]['Address'], "Depa")
        self.assertEqual(direct.directory[0]['Phone'], "3316778899")
        self.assertEqual(direct.directory[0]['email'], "anmksd@hotmail.com")

    def test_constructor_email_syntax(self):

        with self.assertRaises(ValueError):
            direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksdhotmail.com")

    def test_constructor_email_syntax_domain(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmailcom")

        # HERE IT SHOULD RAISE A VALUE ERROR

    def test_constructor_phone_syntax(self):
        direct = Problem15.Directory("Antonio", "Depa", "ANT", "anmksd@hotmail.com")

        # HERE IT SHOULD RAISE A VALUE ERROR

    def test_constructor_phone_lenght(self):
        direct = Problem15.Directory("Antonio", "Depa", "1", "anmksd@hotmail.com")

        # HERE IT SHOULD RAISE A VALUE ERROR

    def test_constructor_number_name(self):
        direct = Problem15.Directory("1", "Depa", "3316778899", "anmksd@hotmail.com")
        # HERE IT SHOULD RAISE A VALUE ERROR

    def test_constructor_empty_field(self):
        direct = Problem15.Directory("1", "", "3316778899", "anmksd@hotmail.com")
        direct = Problem15.Directory("1", "", "", "anmksd@hotmail.com")
        direct = Problem15.Directory("1", "", "3316778899", "@")
        direct = Problem15.Directory("", "", "3316778899", "anmksd@hotmail.com")

        # HERE IT SHOULD RAISE A VALUE ERROR

    def test_constructor_name_symbol(self):
        direct = Problem15.Directory("$$", "calle", "3316778899", "anmksd@hotmail.com")

        # HERE IT SHOULD RAISE A VALUE ERROR

    def test_constructor_extra_spaces(self):
        direct = Problem15.Directory("$$", "calle                          ", "3316778899", "anmksd@hotmail.com")
        self.assertNotEqual(direct.directory[0]['Address'], "calle")

    def test_add_record_expected_output(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        direct.add_record("JUAN", "CASA", "3316778899", "a@google.com")
        self.assertEqual(direct.directory[1]['name'], "JUAN")
        self.assertEqual(direct.directory[1]['Address'], "CASA")
        self.assertEqual(direct.directory[1]['Phone'], "3316778899")
        self.assertEqual(direct.directory[1]['email'], "a@google.com")

    def test_add_record_missing_parameter(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        with self.assertRaises(TypeError):
            direct.add_record("JUAN", "CASA", "3316778899")

    def test_add_record_empty_parameter(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        with self.assertRaises(ValueError):
            direct.add_record("JUAN", "CASA", "", "a@google.com")

    def test_load_record_expected_output_multiple_entries(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        direct.load_record("test2")
        self.assertEqual(direct.directory[1]['name'], "BETO")
        self.assertEqual(direct.directory[0]['Address'], "GUGU")
        self.assertEqual(direct.directory[1]['Phone'], "22222222222")
        self.assertEqual(direct.directory[0]['email'], "fox@hot.com")

    def test_load_record_without_NL_terminator(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        direct.load_record("test3")
        with self.assertRaises(IndexError):
            self.assertEqual(direct.directory[1]['name'], "BETO")

    def test_load_record_more_parameters(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        direct.load_record("test4")
        self.assertEqual(direct.directory[0]["gender"], "male")
        # with self.assertRaises(IndexError):
        #     self.assertEqual(direct.directory[1]['name'], "BETO")

    def test_load_record_no_parameters(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        direct.load_record("test5")
        self.assertEqual(direct.directory[0], {})

    def test_load_record_file_extension(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        with self.assertRaises(FileNotFoundError):
            direct.load_record("test6")

#             Ending with .rtf

    def test_search_from_record_expected_output(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        result1 = direct.search_from_record(0, "name")
        result2 = direct.search_from_record(0, "Address")
        result3 = direct.search_from_record(0, "Phone")
        result4 = direct.search_from_record(0, "email")
        self.assertEqual(result1, "Antonio")
        self.assertEqual(result2, "Depa")
        self.assertEqual(result3, "3316778899")
        self.assertEqual(result4, "anmksd@hotmail.com")

    def test_search_from_record_invalid_key(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        with self.assertRaises(ValueError):
            result1 = direct.search_from_record(0, "nameeee")

    def test_search_from_record_invalid_key_type(self):
        direct = Problem15.Directory("Antonio", "Depa", "3316778899", "anmksd@hotmail.com")
        with self.assertRaises(ValueError):
            result1 = direct.search_from_record(0, 2)

    def test_save_record_expected_output(self):
        direct = Problem15.Directory("SaveTest", "Depa", "3316778899", "anmksd@hotmail.com")
        direct1 = Problem15.Directory("ShouldBeErased", "Erased", "111111111", "No_email@hotmail.com")
        direct.save_record("test7")
        direct1.load_record("test7")
        self.assertEqual(direct1.directory[0]['name'], "SaveTest")
        self.assertEqual(direct1.directory[0]['Address'], "Depa")
        self.assertEqual(direct1.directory[0]['Phone'], "3316778899")
        self.assertEqual(direct1.directory[0]['email'], "anmksd@hotmail.com")

    def test_save_record_invalid_filename_type(self):
        direct = Problem15.Directory("SaveTest", "Depa", "3316778899", "anmksd@hotmail.com")
        with self.assertRaises(TypeError):
            direct.save_record(1)


if __name__ == '__main__':
    unittest.main()