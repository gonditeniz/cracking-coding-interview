import template
import unittest

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.input_data = ""
        self.expected_output = ""

    def _check_function(self, func):
        self.assertEqual(func(self.input_data), self.expected_output)

    def test_1(self):
        self.input_data = "hola"
        self.expected_output = "hola"
        self._check_function(template.run)
