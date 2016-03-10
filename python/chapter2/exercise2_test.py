import exercise2
import unittest

class Exercise2Test(unittest.TestCase):

    def test_1(self):
        n1 = exercise2.Node(1)
        n2 = exercise2.Node(2)
        n3 = exercise2.Node(3)
        n4 = exercise2.Node(4)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        node = exercise2.run(n1, 2)
        self.assertEqual(node.data, n2.data)

    def test_2(self):
        n1 = exercise2.Node(1)
        n2 = exercise2.Node(2)
        n3 = exercise2.Node(3)
        n4 = exercise2.Node(4)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        node = exercise2.run(n1, 3)
        self.assertEqual(node.data, n1.data)

    def test_3(self):
        n1 = exercise2.Node(1)
        n2 = exercise2.Node(2)
        n3 = exercise2.Node(3)
        n4 = exercise2.Node(4)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        node = exercise2.run(n1, 4)
        self.assertEqual(node, None)
