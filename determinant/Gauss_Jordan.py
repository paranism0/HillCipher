def calculate_det(n, m):
    det = 1

    for i in range(n):
        # Search for maximum in this column
        max_elem = abs(m[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(m[k][i]) > max_elem:
                max_elem = abs(m[k][i])
                max_row = k

        # Swap maximum row with current row if needed
        if max_row != i:
            m[i], m[max_row] = m[max_row], m[i]
            det *= -1  

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            if m[i][i] == 0:
                return 0
            factor = m[k][i] / m[i][i]
            for j in range(i, n):
                m[k][j] -= factor * m[i][j]

    # Multiply diagonal elements to get determinant
    for i in range(n):
        det *= m[i][i]

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

