def get_minor(m, i, j):
    # Return the minor of the element at row i and column j
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]


# Recursive function to find the determinant of a matrix with memoization
def calculate_det(n, m, memo={}):
    
    matrix_tuple = tuple(map(tuple, m))  # Convert to tuple for memoization
    if matrix_tuple in memo:
        return memo[matrix_tuple]

    
    if n == 1:
        result = m[0][0]
        memo[matrix_tuple] = result
        return result

    if n == 2:
        result = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        memo[matrix_tuple] = result
        return result
    
    det = 0
    for j in range(n):
        minor = get_minor(m, 0, j)
        cofactor = ((-1) * j) * m[0][j]
        det += cofactor * calculate_det(n-1, minor, memo)
    
    memo[matrix_tuple] = det
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