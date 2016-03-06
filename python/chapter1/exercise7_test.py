import exercise7
import unittest

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.input_data = []
        self.expected_output = []
        
    def _check_run(self):
        self.assertEqual(exercise7.run(self.input_data), self.expected_output)

    def test_1(self):
        self.input_data = [[1, 2, 0, 4], [5, 6, 7, 8], [9, 10, 0, 12]]
        """
        1 2  0 4
        5 6  7 8
        9 10 0 12
        """
        self.expected_output = [[0, 0, 0, 0], [5, 6, 0, 8], [0, 0, 0, 0]]
        """
        0 0 0 0
        5 6 0 8
        0 0 0 0
        """
        self._check_run()

    def test_2(self):
        self.input_data = [[1, 2, 0, 4], [0, 6, 7, 8], [9, 10, 0, 12]]
        """
        1 2  0 4
        0 6  7 8
        9 10 0 12
        """
        self.expected_output = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        """
        0 0 0 0
        0 0 0 0
        0 0 0 0
        """
        self._check_run()
