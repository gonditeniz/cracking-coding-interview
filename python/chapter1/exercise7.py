def run(input_data):
    rows = len(input_data)
    columns = len(input_data[0])

    zero_rows = []
    zero_columns = []
    for row in range(0, rows):
        for column in range(0, columns):
            if input_data[row][column] == 0:
                zero_rows.append(row)
                zero_columns.append(column)

    for row in zero_rows:
        for column in range(0, columns):
            input_data[row][column] = 0
    for column in zero_columns:
        for row in range(0, rows):
            input_data[row][column] = 0
            
    return input_data
    
