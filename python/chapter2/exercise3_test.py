import exercise3
import unittest

class Exercise3Test(unittest.TestCase):

    def test_1(self):
        n1 = exercise3.Node(1)
        n2 = exercise3.Node(2)
        n3 = exercise3.Node(3)
        n4 = exercise3.Node(4)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        self.assertTrue(exercise3.run(n2))

        count = 1
        while n1.next_node is not None:
            n1 = n1.next_node
            count += 1
        self.assertEqual(count, 3)

    def test_2(self):
        n1 = exercise3.Node(1)
        n2 = exercise3.Node(2)
        n3 = exercise3.Node(3)
        n4 = exercise3.Node(4)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        self.assertFalse(exercise3.run(n4))

