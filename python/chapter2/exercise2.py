class Node:
    next_node = None
    data = 0

    def __init__(self, value):
        self.data = value

def run(input_data, k):
   first = input_data
   second = input_data
   i = 0
   for i in range(0, k):
       if first is None:
           return None
       first = first.next_node

   if first is None:
       return None

   while first.next_node is not None:
       first = first.next_node
       second = second.next_node

   return second
