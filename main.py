from cipher import hill_cipher_encryption, preprocess_inputs, hill_cipher_decryption
from utils import check_key, check_msg


def main():
    choose = input("encrypt or decrypt(e or d)? ")
    if choose == "e":
        message = input("input message to encrypt: ")
        key = input("input key to encrypt message: ")
        if "~" in message:
            print("you can't use ~ in your message")
            exit()
        if "~" in key:
            print("you can't use ~ in your key")
            exit()
        key, n = check_key(key)
        message, p = check_msg(message, n)
        enc_text = hill_cipher_encryption(
            *preprocess_inputs(message, key, n, p))
        print("encrypted Text : " + enc_text)
    elif choose == "d":
        message = input("input encrypted message to decrypt: ")
        key = input("input key to decrypt message: ")
        key, n = check_key(key)
        message, p = check_msg(message, n)
        dec_text = hill_cipher_decryption(
            *preprocess_inputs(message, key, n, p))
        print("decrypted Text : " + dec_text)
    else:
        print("invalid input.")


if __name__ == "__main__":
    main()
