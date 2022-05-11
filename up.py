if __name__ == '__main__':
    n = 10
    m = 10
    matrix1 = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        matrix1.append(row)

    matrix3 = []
    for row in range(n):
        matrix3.append([0] * m)
    for i in range(n):
        for j in range(m):
            matrix3[i][j] = matrix1[9-i][j]

    matrix2 = []
    for row in range(n):
        matrix2.append([0] * m)

    for row in range(n):
        for col in range(m):
            matrix2[0][0] = matrix3[0][0]
            matrix2[0][col] = matrix2[0][col - 1] + matrix3[0][col]
            matrix2[row][0] = matrix2[row - 1][0] + matrix3[row][0]

    for row in range(1, n):
        for col in range(1, m):
            matrix2[row][col] = max(matrix2[row - 1][col], matrix2[row][col - 1]) + matrix3[row][col]

    # print(matrix2)
    print(matrix2[n - 1][m - 1])

    for row in range(1, n):
        for col in range(1, m):
            matrix2[row][col] = min(matrix2[row - 1][col], matrix2[row][col - 1]) + matrix3[row][col]
    print(matrix2[n - 1][m - 1])


