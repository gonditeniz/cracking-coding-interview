import exercise4
import unittest

class Exercise4Test(unittest.TestCase):

    def test_1(self):
        n1 = exercise4.Node(5)
        n2 = exercise4.Node(4)
        n3 = exercise4.Node(2)
        n4 = exercise4.Node(1)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        node = exercise4.run(n1, 3)
        self.assertEqual(node.data, 2)
        node = node.next_node
        self.assertEqual(node.data, 1)
        node = node.next_node
        self.assertEqual(node.data, 5)
        node = node.next_node
        self.assertEqual(node.data, 4)
        node = node.next_node
        self.assertEqual(node, None)
