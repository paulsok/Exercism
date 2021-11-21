def saddle_points(matrix):
    if len(set(map(len, matrix))) > 1:
        raise ValueError('irregular matrix')

    mat, points = list(zip(*matrix)), []

    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            if num == max(row) and num == min(mat[j]):
                point_dict = {'row': i+1, 'column': j+1}
                points.append(point_dict)

    return points
