import unittest
from what_misses import what_misses


class TestEx2(unittest.TestCase):

    def test_what_misses(self):
        n = 10
        input_data = [2, 3, 7, 4, 9]
        output_data = what_misses(input_data, n)
        expected_data = [1, 5, 6, 8, 10]
        self.assertEqual(output_data, expected_data)


if __name__ == '__main__':
    unittest.main()
