class Node:
    next_node = None
    data = 0

    def __init__(self, value):
        self.data = value

def run(input_data1, input_data2):
    i = 0
    number1 = 0
    while input_data1 is not None:
        number1 += input_data1.data * pow(10, i)
        input_data1 = input_data1.next_node
        i += 1

    i = 0
    number2 = 0
    while input_data2 is not None:
        number2 += input_data2.data * pow(10, i)
        input_data2 = input_data2.next_node
        i += 1

    total = number1 + number2
    total_str = str(total)

    output_data = None
    for char in reversed(total_str):
        node = Node(int(char))
        node.next_node = output_data
        output_data = node

    return output_data
        

    
