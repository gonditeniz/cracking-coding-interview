import exercise6
import unittest

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.input_data = []
        self.expected_output = []
        
    def _check_run(self):
        self.assertEqual(exercise6.run(self.input_data), self.expected_output)

    def test_1(self):
        self.input_data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        """
        1  2  3  4
        5  6  7  8
        9  10 11 12
        13 14 15 16
        """
        self.expected_output = [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]]
        """
        13  9  5  1
        14 10  6  2
        15 11  7  3
        16 12  8  4
        """
        self._check_run()
