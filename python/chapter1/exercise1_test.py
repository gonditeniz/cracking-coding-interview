import exercise1
import unittest

class Exercise1Test(unittest.TestCase):

    def setUp(self):
        self.input_data = ""
        self.expected_output = ""
        
    def _check_function(self, func):
        self.assertEqual(func(self.input_data), self.expected_output)

    def test_1_1(self):
        self.input_data = "hola"
        self.expected_output = True
        self._check_function(exercise1.run1)

    def test_1_2(self):
        self.input_data = "holo"
        self.expected_output = False
        self._check_function(exercise1.run2)

    def test_2_1(self):
        self.input_data = "hola"
        self.expected_output = True
        self._check_function(exercise1.run2)

    def test_2_2(self):
        self.input_data = "holo"
        self.expected_output = False
        self._check_function(exercise1.run2)

    def test_3_1(self):
        self.input_data = "hola"
        self.expected_output = True
        self._check_function(exercise1.run3)

    def test_3_2(self):
        self.input_data = "holo"
        self.expected_output = False
        self._check_function(exercise1.run3)
