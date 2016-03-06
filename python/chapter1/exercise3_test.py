import exercise3
import unittest

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.input_data1 = ""
        self.input_data2 = ""
        self.expected_output = ""
        
    def _check_function(self, func):
        self.assertEqual(func(self.input_data1, self.input_data2), self.expected_output)

    def test_1_1(self):
        self.input_data1 = "hola"
        self.input_data2 = "halo"
        self.expected_output = True
        self._check_function(exercise3.run1)

    def test_1_2(self):
        self.input_data1 = "hola"
        self.input_data2 = "holo"
        self.expected_output = False
        self._check_function(exercise3.run1)

    def test_2_1(self):
        self.input_data1 = "hola"
        self.input_data2 = "halo"
        self.expected_output = True
        self._check_function(exercise3.run2)

    def test_2_2(self):
        self.input_data1 = "hola"
        self.input_data2 = "holo"
        self.expected_output = False
        self._check_function(exercise3.run2)
