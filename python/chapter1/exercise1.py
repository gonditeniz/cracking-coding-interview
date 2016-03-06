def run1(input_data):
    char_list = []
    for character in input_data:
        if character in char_list:
            return False
        else:
            char_list.append(character)
    return True

def run2(input_data):
    char_set = set()
    for character in input_data:
        prev_len = len(char_set)
        char_set.add(character)
        if prev_len == len(char_set):
            return False
    return True
    
def run3(input_data):
    checker = 0
    for character in input_data:
        char_val = ord(character) - ord('a')
        char_pos = 1 << char_val
        if checker & char_pos != 0:
            return False
        checker |= char_pos
    return True

