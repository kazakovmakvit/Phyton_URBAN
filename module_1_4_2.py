def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for k in range(m):
            matrix[i].append(value)
    return matrix

print(get_matrix(2,3,10))