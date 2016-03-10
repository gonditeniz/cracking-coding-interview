import exercise1
import unittest

class Exercise1Test(unittest.TestCase):

    def test_1(self):
        n1 = exercise1.Node(1)
        n2 = exercise1.Node(2)
        n3 = exercise1.Node(3)
        n4 = exercise1.Node(1)
        n1.next_node = n2
        n2.next_node = n3
        n3.next_node = n4

        exercise1.run(n1)
        
        count = 1
        while n1.next_node is not None:
            n1 = n1.next_node
            count += 1
        self.assertEqual(count, 3)
