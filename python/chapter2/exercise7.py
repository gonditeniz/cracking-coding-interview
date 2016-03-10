class Node:
    next_node = None
    data = 0

    def __init__(self, value):
        self.data = value

def run(input_data):
    slow = input_data
    fast = input_data
    stack = []
    while fast is not None and fast.next_node is not None:
        stack.append(slow.data)
        fast = fast.next_node.next_node
        slow = slow.next_node

    #import pdb; pdb.set_trace()
    if fast is not None:
        slow = slow.next_node

    while slow is not None:
        if stack.pop() != slow.data:
            return False
        slow = slow.next_node

    if len(stack) == 0:
        return True
    return False
    
