def run(input_data):
    input_len = len(input_data)
    input_list = list(input_data)
    med = input_len/2
    for i in range(0, med):
        temp_val = input_list[i]
        input_list[i] = input_list[input_len-i-1]
        input_list[input_len-i-1] = temp_val
    return ''.join(input_list)
