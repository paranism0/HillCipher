from math import ceil , sqrt
import copy

alphabets = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25 , "_": 26
}

reverse_dict_alphabets = {
    0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
    10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S',
    19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z' , 26: "_"
}

def convert_str_to_matrix(text, p, n , msg = True):
    if msg:
        matrix = []
        for _ in range(0,p,n):
            matrix.append([[alphabets.get(q)] for q in text[_:_+n]])
        return matrix
    else:
        matrix = [[0]*p for i in range(n)]
        counter = 0
        for i in range(n):
            for j in range(p):
                matrix[i][j] = alphabets.get(text[counter])
                counter += 1
        return matrix

def check_msg(msg: str, n):
    msg = msg.upper().replace(" ","_")
    msg_length = len(msg)
    result_divide = msg_length / n
    if result_divide == 0:
        result_divide = 0.5
    if result_divide == int(result_divide):
        return msg, msg_length
    new_result_divide = ceil(result_divide)
    number_of_needed_padding = (new_result_divide * n) - msg_length
    msg += "_"*number_of_needed_padding
    return msg,new_result_divide*2

def check_key(key: str):
    key = key.upper().replace(" ","_")
    key_length = len(key)
    sqrt_of_len = sqrt(key_length)
    if sqrt_of_len == 0:
        sqrt_of_len = 0.5
    if sqrt_of_len == int(sqrt_of_len):
        return key, int(sqrt_of_len)
    new_sqrt_of_len = ceil(sqrt_of_len)
    number_of_needed_padding = new_sqrt_of_len**2 - key_length
    key += "_"*number_of_needed_padding
    return key, new_sqrt_of_len

def simple_multiple(matrix1, matrix2):
    res = ""
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            x = 0
            for k in range(len(matrix2)):
                if matrix2[k][j]:
                    x += matrix1[i][k] * matrix2[k][j]
            x = x%27
            res+=reverse_dict_alphabets.get(x)
    return res

def cofactor(l, m: int, n: int):
    actualn = len(l)
    return [[l[i][j] for j in range(
        0, n)] + [l[i][j] for j in range(
            n+1, actualn)] for i in range(0, m)] + [[l[i][j] for j in range(
                0, n)] + [l[i][j] for j in range(
                    n+1, actualn)] for i in range(m+1, actualn)]

def scale_row(m, row, scalar):
    # Scale a row by a given scalar
    m[row] = [element * scalar for element in m[row]]

def add_scaled_row(m, target_row, source_row, scale):
    # Add a scaled row to another row 
    m[target_row] = [target + scale * source for target, source in zip(m[target_row], m[source_row])]

def calculate_det(n = None, m = []):
    if not n:
        n = len(m)
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

def adjoint(l):
    an = len(l)
    return [[((-1) ** (i + j)) * calculate_det(m = cofactor(l, i, j)) for j in range(an)] for i in range(an)]

class Matrix:
    __values = []
    m = 0
    n = 0

    def __init__(self, m: int, n: int, listInit, checkForOrder: bool = True) -> None:
        self.m = m
        self.n = n
        if checkForOrder:
            if len(listInit) != m:
                raise ValueError(
                    f"Number of lists ({len(listInit)}) in listInit does not match number of rows 'm' ({m})")
            for row in range(len(listInit)):
                if len(listInit[row]) != n:
                    raise ValueError(
                        f"Length of column number: {row+1} is not equal to the value {n} given in order of Matrix")
        self.__values = listInit

    def determinant(self):
        return calculate_det( len(self.__values)  , self.__values)

    def adjoint(self):
        return Matrix(self.m, self.n, adjoint(self.__values), False).transpose()

    def cofactor(self, m: int, n: int):
        '''
        Returns the Cofactor matrix of a given element in the Matrix
        '''
        if self.m != self.n:
            raise ValueError(
                'Cofactors are only available for square matrices')
        mtrx = cofactor(self.__values, m-1, n-1)
        return (-1)**(m+n) * calculate_det(len(mtrx) , mtrx)

    def transpose(self):
        '''
        Returns the tranpose of the matrix
        '''
        return Matrix(self.n, self.m, [[self.__values[j][i] for j in range(self.m)] for i in range(self.n)], False)

    def __getitem__(self, sub):
        t = type(sub)
        if t == int:
            try:
                return self.__values[sub]
            except IndexError:
                raise Exception('Row number must be an integer greater than or equal to 1' if sub <
                                0 else 'Row number exceeds size of the Matrix')

def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1

def calc_inverse_matrix(matrix):
    n = len(matrix)
    det = round(calculate_det(n , copy.deepcopy(matrix))) % 27
    if det == 0:
        return False
    inv = modInverse(
        det,
        27
    )
    if inv == -1:
        return False
    adj = Matrix(n, n, matrix).adjoint()
    return list([[(inv*(adj[i][j]))%27 for j in range(n)] for i in range(n)])

def check_key_matrix(key_matrix):
    inverse = calc_inverse_matrix(copy.deepcopy(key_matrix))
    if isinstance(inverse, bool) and inverse == False:
        return "NO_VALID_KEY"
    return inverse

def hill_cipher_encryption(message_matrix, key_matrix):
    cipher_text = ""
    for mtrx in message_matrix:
        cipher_text += simple_multiple(
            key_matrix,
            mtrx
        )
    return cipher_text

if __name__=="__main__":
    key = []
    n = int(input())
    for _ in range(n):
        key.append([int(num) for num in input().split(" ")])
    msg = input()
    msg, p = check_msg(msg, n)
    if check_key_matrix(key)!="NO_VALID_KEY":
        print(hill_cipher_encryption(convert_str_to_matrix(msg,p,n),key))
    else:
        print("NO_VALID_KEY")