class Node:
    next_node = None
    data = 0

    def __init__(self, value):
        self.data = value
        
def run(input_data):
    values = []
    while input_data is not None:
        if input_data.data in values:
            previous.next_node = input_data.next_node
        else:
            values.append(input_data.data)
            previous = input_data
        input_data = input_data.next_node

