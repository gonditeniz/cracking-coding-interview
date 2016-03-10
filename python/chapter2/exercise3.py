class Node:
    next_node = None
    data = 0

    def __init__(self, value):
        self.data = value

def run(input_data):
    if input_data is None or input_data.next_node is None:
        return False
    input_data.data = input_data.next_node.data
    input_data.next_node = input_data.next_node.next_node
    return True
    
