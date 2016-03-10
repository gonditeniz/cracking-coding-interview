import exercise7
import unittest

class Exercise7Test(unittest.TestCase):

    def test_1_1(self):
        n1 = exercise7.Node('a')
        n2 = exercise7.Node('b')
        n3 = exercise7.Node('c')
        n4 = exercise7.Node('b')
        n5 = exercise7.Node('a')
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4
        n4.next_node = n5

        self.assertTrue(exercise7.run(n1))

    def test_1_2(self):
        n1 = exercise7.Node('a')
        n2 = exercise7.Node('b')
        n3 = exercise7.Node('c')
        n4 = exercise7.Node('c')
        n5 = exercise7.Node('b')
        n6 = exercise7.Node('a')
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4
        n4.next_node = n5
        n5.next_node = n6

        self.assertTrue(exercise7.run(n1))

    def test_2_1(self):
        n1 = exercise7.Node('a')
        n2 = exercise7.Node('b')
        n3 = exercise7.Node('c')
        n4 = exercise7.Node('b')
        n5 = exercise7.Node('c')
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4
        n4.next_node = n5

        self.assertFalse(exercise7.run(n1))

    def test_2_2(self):
        n1 = exercise7.Node('a')
        n2 = exercise7.Node('b')
        n3 = exercise7.Node('c')
        n4 = exercise7.Node('c')
        n5 = exercise7.Node('b')
        n6 = exercise7.Node('d')
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4
        n4.next_node = n5
        n5.next_node = n6

        self.assertFalse(exercise7.run(n1))
