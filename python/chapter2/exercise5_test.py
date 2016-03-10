import exercise5
import unittest

class Exercise5Test(unittest.TestCase):

    def test_1(self):
        n1_1 = exercise5.Node(1)
        n1_2 = exercise5.Node(2)
        n1_3 = exercise5.Node(3)
        n1_1.next_node = n1_2
        n1_2.next_node = n1_3

        n2_1 = exercise5.Node(4)
        n2_2 = exercise5.Node(5)
        n2_3 = exercise5.Node(6)
        n2_1.next_node = n2_2
        n2_2.next_node = n2_3

        node = exercise5.run(n1_1, n2_1)
        self.assertEqual(node.data, 9)
        node = node.next_node
        self.assertEqual(node.data, 7)
        node = node.next_node
        self.assertEqual(node.data, 5)
        node = node.next_node
        self.assertEqual(node, None)

    def test_2(self):
        n1_1 = exercise5.Node(1)
        n1_2 = exercise5.Node(2)
        n1_3 = exercise5.Node(4)
        n1_1.next_node = n1_2
        n1_2.next_node = n1_3

        n2_1 = exercise5.Node(4)
        n2_2 = exercise5.Node(5)
        n2_3 = exercise5.Node(6)
        n2_1.next_node = n2_2
        n2_2.next_node = n2_3

        node = exercise5.run(n1_1, n2_1)
        self.assertEqual(node.data, 1)
        node = node.next_node
        self.assertEqual(node.data, 0)
        node = node.next_node
        self.assertEqual(node.data, 7)
        node = node.next_node
        self.assertEqual(node.data, 5)
        node = node.next_node
        self.assertEqual(node, None)
