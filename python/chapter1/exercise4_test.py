import exercise4
import unittest

class Exercise4Test(unittest.TestCase):

    def setUp(self):
        self.input_data = ""
        self.expected_output = ""
        
    def _check_function(self, func):
        self.assertEqual(func(self.input_data), self.expected_output)

    def test_1(self):
        self.input_data = "ho la"
        self.expected_output = "ho%20la"
        self._check_function(exercise4.run)
