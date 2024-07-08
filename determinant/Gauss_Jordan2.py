def scale_row(m, row, scalar):
    # Scale a row by a given scalar
    m[row] = [element * scalar for element in m[row]]

def add_scaled_row(m, target_row, source_row, scale):
    # Add a scaled row to another row 
    m[target_row] = [target + scale * source for target, source in zip(m[target_row], m[source_row])]

def calculate_det(n, m):

    det = 1
    
    for i in range(n):
        # Make the diagonal element 1 and adjust the rows accordingly
        if m[i][i] == 0:
            for k in range(i + 1, n):
                if m[k][i] != 0:
                    m[k], m[i] = m[i], m[k]
                    det *= -1
                    break
            else:
                return 0
        
        pivot = m[i][i]
        det *= pivot
        scale_row(m, i, 1 / pivot)
        
        # Eliminate the column elements below and above the pivot
        for j in range(n):
            if i != j:
                factor = m[j][i]
                add_scaled_row(m, j, i, -factor)
    
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