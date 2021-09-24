def annotate(minefield):
    if minefield == []:
        return []

    column_max, row_max = len(minefield[0]), len(minefield)

    field = {}
    for i, row in enumerate(minefield):
        if len(row) != column_max:
            raise ValueError("Rows lengths are different!")

        for j, k in enumerate(row):
            if k not in ' *':
                raise ValueError("Failed input!")
            field[i, j] = k

    t_set = (-1, 0, 1)
    for (i, j), k in field.items():
        if k == ' ':
            value = (field.get((i+x, j+y), '') == '*' for x in t_set for y in t_set)
            field[i, j] = str(sum(value) or k)

    return [''.join(field[i, j] for j in range(column_max)) for i in range(row_max)]
