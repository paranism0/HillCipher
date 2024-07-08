def calculate_det(n, m):

    det = 0
    if (n == 1):
        det = m[0][0]
        return det

    if (n == 2):
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return det

    new_m = [[0 for x in range(n-1)] for y in range(n-1)]

    for k in range(n):

        for i in range(n):
            col_index = 0
            for j in range(n):
                if (i == 0 or j == k):
                    continue
                new_m[i-1][col_index] = m[i][j]
                col_index += 1

        det += m[0][k] * pow(-1, 1+(k+1)) * calculate_det(n-1, new_m)

    return det



n = int(input())

m = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    line = input()
    row = line.split()
    for j in range(n):
        m[i][j] = float(row[j])

determinant = int(calculate_det(n, m))
print(determinant)
