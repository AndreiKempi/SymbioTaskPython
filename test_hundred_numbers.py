import unittest
import hundred_numbers


class TestHundredNumbers(unittest.TestCase):

    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_file_name = 'files/testNumberFile.txt'

    def test_create_list_of_100_numbers(self):
        list_of_numbers = hundred_numbers.create_list_of_100_numbers()
        self.assertEqual(len(list_of_numbers), 100)

    def test_write_numbers_to_file(self):
        numbers_are_written = hundred_numbers.write_numbers_into_the_file(TestHundredNumbers.test_file_name, TestHundredNumbers.test_numbers)
        self.assertTrue(numbers_are_written)

    def test_read_numbers_from_file(self):
        numbers_from_the_file = hundred_numbers.read_numbers_from_file(TestHundredNumbers.test_file_name)
        self.assertTrue(numbers_from_the_file)
        self.assertEqual(len(numbers_from_the_file), 10)
        self.assertEqual(numbers_from_the_file, TestHundredNumbers.test_numbers)

    def test_get_every_second_number_from_file_to_console(self):
        half_of_numbers = hundred_numbers.get_every_second_number_from_list(TestHundredNumbers.test_numbers)
        self.assertTrue(half_of_numbers)
        self.assertEqual(len(half_of_numbers), 5)