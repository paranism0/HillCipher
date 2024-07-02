from math import sqrt, ceil
from constants import alphabets
import numpy as np
from mathmatrix import Matrix
from determinant.Gauss_Jordan import determinant_gauss_jordan


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


def calc_inverse_matrix(matrix):
    n = len(matrix)

    det = round(determinant_gauss_jordan(matrix, n)) % 71

    if det == 0:
        return False
    # (x * det) mod by 71 = 1 -> here minimum number of x is our inverse
    inv = modInverse(
        det,
        71
    )
    if inv == -1:
        return False
    adj = Matrix(n, n, matrix).adjoint()
    adj = np.array([[adj[i][j] for j in range(n)] for i in range(n)]) % 71
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
