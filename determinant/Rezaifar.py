def calculate_det(n, m):
    if (n < 0):
        print("index out of bound")
        return

    det = 0
    if (n == 1):
        det = m[0][0]
        return det

    if (n == 2):
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return det

    m_11 = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if (i == 0 or j == 0):
                continue
            m_11[i-1][col_index] = m[i][j]
            col_index += 1

    m_1n = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if (i == 0 or j == n-1):
                continue
            m_1n[i-1][col_index] = m[i][j]
            col_index += 1

    m_n1 = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if (i == n-1 or j == 0):
                continue
            m_n1[i][col_index] = m[i][j]
            col_index += 1

    m_nn = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if (i == n-1 or j == n-1):
                continue
            m_nn[i][col_index] = m[i][j]
            col_index += 1

    m_11_nn = [[0 for x in range(n-2)] for y in range(n-2)]

    for i in range(n-1):
        col_index = 0
        for j in range(n-1):
            if (i == 0 or j == 0):
                continue
            m_11_nn[i-1][col_index] = m_nn[i][j]
            col_index += 1

    det = ((calculate_det(n-1, m_11) * calculate_det(n-1, m_nn)) -
           (calculate_det(n-1, m_1n) * calculate_det(n-1, m_n1))) / (calculate_det(n-2, m_11_nn))

    return det



n = int(input())

m = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    line = input()
    row = line.split()
    for j in range(n):
        m[i][j] = float(row[j])

determinant = calculate_det(n, m)
print(f"{determinant:.2f}")
