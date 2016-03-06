def run(input_data):
    dimension = len(input_data) # 4
    for layer in range(0, dimension/2): # 0, 1
        for pos in range(layer, dimension-1-layer): # 0 1 2 3
            first_element = input_data[layer][pos]
            input_data[layer][pos] = input_data[dimension-1-pos][layer]
            input_data[dimension-1-pos][layer] = input_data[dimension-1-layer][dimension-1-pos]
            input_data[dimension-1-layer][dimension-1-pos] = input_data[pos][dimension-1-layer]
            input_data[pos][dimension-1-layer] = first_element

    return input_data
    
