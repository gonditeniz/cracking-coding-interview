def run(input_data):
    last_char = None
    count_char = 0
    output = ""
    for char in input_data:
        if char == last_char:
            count_char += 1
        else:
            if count_char > 0:
                output += last_char
                output += str(count_char)
            last_char = char
            count_char = 1
    output += last_char
    output += str(count_char)

    return output if len(output) < len(input_data) else input_data
