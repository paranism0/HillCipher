from math import sqrt, ceil
from constants import alphabets
import numpy as np
import copy


def modInverse(A, M):
    g = gcd(A, M)
    if (g != 1):
        return -1
    else:
        return power(A, M - 2, M)


def power(x, y, M):
    if (y == 0):
        return 1
    p = power(x, y // 2, M) % M
    p = (p * p) % M
    if (y % 2 == 0):
        return p
    else:
        return ((x * p) % M)


def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)


def get_comatrix(matrix, n):
    inverse = np.array([[0 for x in range(n)] for y in range(n)])
    for i in range(n):
        for j in range(n):
            adj = [[0 for x in range(n-1)] for y in range(n-1)]
            row_index = col_index = 0
            for row in range(n):
                if (row == i):
                    continue
                col_index = 0
                for col in range(n):
                    if (col == j):
                        continue
                    adj[row_index][col_index] = matrix[row][col]
                    col_index += 1
                row_index += 1
            adj_det = determinant_gauss_jordan(adj, n-1)
            inverse[i][j] = pow(-1, i+j) * adj_det
    temp = copy.deepcopy(inverse)
    for i in range(n):
        for j in range(n):
            inverse[i][j] = temp[j][i]
    return inverse


def determinant_gauss_jordan(m, n):
    # Convert the input matrix to a NumPy array
    mat = np.array(m, dtype=float)

    # Initialize the determinant as 1
    det = 1.0

    for i in range(n):
        # Find the maximum element in the current column
        max_row = i + np.argmax(np.abs(mat[i:, i]))

        # If the maximum element is 0, the determinant is 0
        if mat[max_row, i] == 0:
            return 0

        # Swap the current row with the row of the maximum element
        if i != max_row:
            # print("mat before = \n", mat)
            mat[[i, max_row]] = mat[[max_row, i]]
            # print("mat after = \n", mat)
            # print(mat[[max_row, i]])
            det *= -1  # Swapping rows changes the sign of the determinant

        # Multiply the determinant by the pivot element
        det *= mat[i, i]

        # Normalize the pivot row
        mat[i] /= mat[i, i]

        # Eliminate the current column elements below the pivot
        for j in range(i + 1, n):
            mat[j] -= mat[j, i] * mat[i]

    return det


# we don't use it because of its complexity

def calculate_det_laplace(m, n):
    if (n < 0):
        print("index out of bound")
        return
    det = 0
    if (n == 1):
        det = m[0]
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
        det += m[0][k] * pow(-1, 1+(k+1)) * calculate_det_laplace(new_m, n-1)
    return det

####


def calc_inverse_matrix(matrix):
    n = len(matrix)
    det = round(determinant_gauss_jordan(matrix, n)) % 71
    adj = get_comatrix(matrix, n) % 71
    inv = modInverse(
        det,
        71
    )
    return (inv*adj) % 71


def convert_str_to_matrix(text, p, n):
    matrix = [[0]*p for i in range(n)]
    counter = 0
    for i in range(n):
        for j in range(p):
            matrix[i][j] = alphabets.get(text[counter])
            counter += 1
    return matrix


def check_key(key: str):
    key_length = len(key)
    sqrt_of_len = sqrt(key_length)
    if sqrt_of_len == 0:
        sqrt_of_len = 0.5
    if sqrt_of_len == int(sqrt_of_len):
        return key, int(sqrt_of_len)
    new_sqrt_of_len = ceil(sqrt_of_len)
    number_of_needed_padding = new_sqrt_of_len**2 - key_length
    key += "~"*number_of_needed_padding
    return key, new_sqrt_of_len


def check_msg(msg: str, n):
    msg_length = len(msg)
    result_divide = msg_length / n
    if result_divide == 0:
        result_divide = 0.5
    if result_divide == int(result_divide):
        return msg, int(result_divide)
    new_result_divide = ceil(result_divide)
    number_of_needed_padding = (new_result_divide * n) - msg_length
    msg += "~"*number_of_needed_padding
    return msg, new_result_divide


def simple_multiple(matrix1, matrix2):
    res = [[0]*len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                res[i][j] += matrix1[i][k] * matrix2[k][j]
    return res
