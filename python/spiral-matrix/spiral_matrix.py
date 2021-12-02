def spiral_matrix(size):
    answer = [[0] * size for _ in range(size)]

    dim_min, dim_max = 0, size - 1
    row, column = 0, 0
    modl = size

    for i in range(size ** 2):
        if not answer[row][column]:
            answer[row][column] = i + 1
        if row == dim_min and column != dim_max:
            column = (column + 1) % modl
        elif column == dim_min:
            row = (row - 1) % modl
        elif row == dim_max:
            column = (column - 1) % modl
        elif column == dim_max:
            row = (row + 1) % modl

        if column == dim_min and row == dim_min + 1:
            dim_min += 1
            dim_max -= 1

    return answer
