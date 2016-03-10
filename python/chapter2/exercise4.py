class Node:
    next_node = None
    data = 0

    def __init__(self, value):
        self.data = value

def run(input_data, value):
    pre_head = None    
    pre = None
    post_head = None
    post = None

    while input_data is not None:
        next = input_data.next_node
        input_data.next_node = None
        if input_data.data <= value:
            if pre is not None:
                pre.next_node = input_data
            if pre_head is None:
                pre_head = input_data
            pre = input_data
        else:
            if post is not None:
                post.next_node = input_data
            if post_head is None:
                post_head = input_data
            post = input_data

        input_data = next

    pre.next_node = post_head
    return pre_head
