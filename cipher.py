from utils import convert_str_to_matrix, simple_multiple, calc_inverse_matrix
from constants import reverse_dict_alphabets


def preprocess_inputs(message, key, n, p):
    message_matrix = convert_str_to_matrix(
        message,
        p,
        n
    )
    key_matrix = convert_str_to_matrix(
        key,
        n,
        n
    )
    return message_matrix, key_matrix


def hill_cipher_decryption(encrypted_msg_matrix, key_matrix):
    inverse = calc_inverse_matrix(key_matrix)
    if isinstance(inverse, bool) and inverse == False:
        return inverse
    cipher_matrix = simple_multiple(
        inverse,
        encrypted_msg_matrix
    )
    for i in range(len(cipher_matrix)):
        for j in range(len(cipher_matrix[0])):
            cipher_matrix[i][j] = reverse_dict_alphabets.get(
                cipher_matrix[i][j] % 71
            )
    return "".join(["".join(p) for p in cipher_matrix]).replace("~", "")


def hill_cipher_encryption(message_matrix, key_matrix):
    inverse = calc_inverse_matrix(key_matrix)
    if isinstance(inverse, bool) and inverse == False:
        return inverse
    cipher_matrix = simple_multiple(
        key_matrix,
        message_matrix
    )
    for i in range(len(cipher_matrix)):
        for j in range(len(cipher_matrix[0])):
            cipher_matrix[i][j] = reverse_dict_alphabets.get(
                cipher_matrix[i][j] % 71
            )
    return "".join(["".join(p) for p in cipher_matrix])
