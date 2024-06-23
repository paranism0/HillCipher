def calculate_det(m, n):
    if(n < 0):
        print("index out of bound")
        return
    
    det = 0
    if(n == 1):
        det = m[0][0]
        return det
    
    if(n == 2):
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return det
    
    m_11 = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if(i == 0 or j == 0):
                continue
            m_11[i-1][col_index] = m[i][j]
            col_index += 1


    m_1n = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if(i == 0 or j == n-1):
                continue
            m_1n[i-1][col_index] = m[i][j]
            col_index += 1


    m_n1 = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if(i == n-1 or j == 0):
                continue
            m_n1[i][col_index] = m[i][j]
            col_index += 1


    m_nn = [[0 for x in range(n-1)] for y in range(n-1)]

    for i in range(n):
        col_index = 0
        for j in range(n):
            if(i == n-1 or j == n-1):
                continue
            m_nn[i][col_index] = m[i][j]
            col_index += 1


    m_11_nn = [[0 for x in range(n-2)] for y in range(n-2)]


    for i in range(n-1):
        col_index = 0
        for j in range(n-1):
            if(i == 0 or j == 0):
                continue
            m_11_nn[i-1][col_index] = m_nn[i][j]
            col_index += 1


    det = ((calculate_det(m_11, n-1) * calculate_det(m_nn, n-1)) - (calculate_det(m_1n, n-1) * calculate_det(m_n1, n-1))) / (calculate_det(m_11_nn, n-2))

    return det

m = [
     [5, 9, 7],
    [8, 0, 13],
    [-1, 15, 4]
]

print("determinant using rezaeifar =",calculate_det(m, 3))