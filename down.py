if __name__ == '__main__':
    n = 10 #строки
    m = 10 #столбцы
    matrix1 = []
    for _ in range(n):
        row = list(map(int, input().split()))
        assert len(row) == m
        matrix1.append(row)

    matrix2 = []

    for row in range(m):
        matrix2.append([0] * n)

    for row in range(n):
        for col in range(m):
            matrix2[0][0] = matrix1[0][0]
            matrix2[0][col] = matrix2[0][col-1] + matrix1[0][col]
            matrix2[row][0] = matrix2[row-1][0] + matrix1[row][0]

    for row in range(1, n):
        for col in range(1, m):
            matrix2[row][col] = max(matrix2[row-1][col], matrix2[row][col-1]) + matrix1[row][col]

    # print(matrix2)
    print(matrix2[n-1][m-1])

    for row in range(1, n):
        for col in range(1, m):
            matrix2[row][col] = min(matrix2[row - 1][col], matrix2[row][col - 1]) + matrix1[row][col]
    print(matrix2[n-1][m-1])
