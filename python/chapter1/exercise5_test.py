import exercise5
import unittest

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.input_data = ""
        self.expected_output = ""
        
    def _check_run(self):
        self.assertEqual(exercise5.run(self.input_data), self.expected_output)

    def test_1(self):
        self.input_data = "aaabbcc"
        self.expected_output = "a3b2c2"
        self._check_run()

    def test_2(self):
        self.input_data = "aabbcc"
        self.expected_output = "aabbcc"
        self._check_run()
