def run1(input_data1, input_data2):
    if len(input_data1) != len(input_data2):
        return False

    char_dict = {}
    for char in input_data1:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in input_data2:
        if char in char_dict:
            char_dict[char] -= 1
        else:
            return False

    return sum(abs(x) for x in char_dict.values()) == 0

def run2(input_data1, input_data2):
    if len(input_data1) != len(input_data2):
        return False

    return sorted(input_data1) == sorted(input_data2)
    
