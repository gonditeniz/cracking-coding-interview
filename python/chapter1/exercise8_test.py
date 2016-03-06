import exercise8
import unittest

class TemplateTest(unittest.TestCase):

    def setUp(self):
        self.input_data1 = ""
        self.input_data2 = ""
        self.expected_output = False
        
    def _check_run(self):
        self.assertEqual(exercise8.run(self.input_data1, self.input_data2), self.expected_output)

    def test_1(self):
        self.input_data = "waterbottle"
        self.input_data = "erbottlewat"
        self.expected_output = True
        self._check_run()

    def test_2(self):
        self.input_data = "waterbottle"
        self.input_data = "arbottlewat"
        self.expected_output = True
        self._check_run()
