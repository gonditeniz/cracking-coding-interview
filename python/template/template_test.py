import template
import unittest

class TemplateTest(unittest.TestCase):

    def test_1(self):

        self.assertTrue(template.run('hola'))
