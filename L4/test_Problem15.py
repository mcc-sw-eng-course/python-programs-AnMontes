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


if __name__ == '__main__':
    unittest.main()