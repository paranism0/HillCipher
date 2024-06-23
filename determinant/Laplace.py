def calculate_det(m, n):

    if(n < 0):
        print("index out of bound")
        return
    
    det = 0
    if(n == 1):
        det = m[0]
        return det
    
    if(n == 2):
        det = (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
        return det
    
    new_m = [[0 for x in range(n-1)] for y in range(n-1)]
    
    for k in range(n):

        for i in range(n):
            col_index = 0
            for j in range(n):
                if(i == 0 or j == k):
                    continue
                new_m[i-1][col_index] = m[i][j]
                col_index += 1


        det += m[0][k] * pow(-1, 1+(k+1)) * calculate_det(new_m, n-1)

    return det


m = [
    [-3, 4, 2, 1, 10, 6],
     [8, 3, 1, -2, 9, -7],
     [-5, -7, -3, 9, 11, 3],
     [1, -2, -1, 4, 13, 3],
     [4, 7, 4, 6, -5, 5],
     [-9, 3, 75, 3, -3.6, 6]
]

print("determinant using laplace =",calculate_det(m, 6))

        

        