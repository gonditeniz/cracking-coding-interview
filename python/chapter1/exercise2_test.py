import exercise2
import unittest

class Exercise2Test(unittest.TestCase):

    def setUp(self):
        self.input_data = ""
        self.expected_output = ""
        
    def _check_function(self, func):
        self.assertEqual(func(self.input_data), self.expected_output)

    def test_1(self):
        self.input_data = "hola"
        self.expected_output = ''.join(reversed(self.input_data))
        self._check_function(exercise2.run)
