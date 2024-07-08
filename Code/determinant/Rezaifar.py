def calculate_det(n, m):
    det = 0
    if (n == 1):
        det = m[0][0]
        return det

    if (n == 2):
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return det

    m_11 = [[m[i][j] for j in range(n) if j != 0] for i in range(n) if i != 0]
    m_1n = [[m[i][j] for j in range(n) if j != n-1] for i in range(n) if i != 0]
    m_n1 = [[m[i][j] for j in range(n) if j != 0] for i in range(n) if i != n-1]
    m_nn = [[m[i][j] for j in range(n) if j != n-1] for i in range(n) if i != n-1]
    m_11_nn = [[m[i][j] for j in range(n) if (j != 0 and j != n-1)] for i in range(n) if (i != 0 and i != n-1)]

    dt = calculate_det(n-2, m_11_nn)
    if dt == 0:
        factor = 1
        for i in range(0,n-1,2):
            m[i], m[i+1] = m[i+1], m[i]
            factor *= -1     
        m_11 = [[m[i][j] for j in range(n) if j != 0] for i in range(n) if i != 0]
        m_1n = [[m[i][j] for j in range(n) if j != n-1] for i in range(n) if i != 0]
        m_n1 = [[m[i][j] for j in range(n) if j != 0] for i in range(n) if i != n-1]
        m_nn = [[m[i][j] for j in range(n) if j != n-1] for i in range(n) if i != n-1]
        m_11_nn = [[m[i][j] for j in range(n) if (j != 0 and j != n-1)] for i in range(n) if (i != 0 and i != n-1)]

        dt = calculate_det(n-2, m_11_nn)
        if dt == 0:
            return 0

        dt *= factor

    det = ((calculate_det(n-1, m_11) * calculate_det(n-1, m_nn)) -
           (calculate_det(n-1, m_1n) * calculate_det(n-1, m_n1))) / dt

    return det

if __name__=="__main__":
    n = int(input())

    m = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        line = input()
        row = line.split()
        for j in range(n):
            m[i][j] = float(row[j])

    determinant = int(calculate_det(n, m))
    print(determinant)