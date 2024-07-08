from PyQt5 import QtWidgets, uic
import sys
from encryption import check_key , check_msg , hill_cipher_encryption , \
    convert_str_to_matrix
from decryption import hill_cipher_decryption , check_key_matrix

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('ui.ui', self)
        self.setFixedSize(291, 244)
        self.setWindowTitle("HillCipher")
        self.define_widgets()
        self.define_events()
        self.error_dialog = QtWidgets.QMessageBox()
        self.show()

    def define_events(self):
        self.enc_btn.clicked.connect(
            self.encrypt_message
        )

        self.dec_btn.clicked.connect(
            self.decrypt_message
        )

    def showerror(self, msg):
        self.error_dialog.setWindowTitle("Error!")
        self.error_dialog.setText(msg)
        self.error_dialog.show()

    def get_message(self):
        return self.message.text()

    def get_key(self):
        return self.key.text()

    def encrypt_message(self):
        msg = self.get_message()
        key = self.get_key()
        if "_"==msg[-1]:
            self.showerror("you can't use _ as your last character in message")
            exit()
        key, n = check_key(key)
        msg, p = check_msg(msg, n)
        key = convert_str_to_matrix(key,n,n,msg=False)
        if check_key_matrix(key)!="NO_VALID_KEY":
            enc_text = hill_cipher_encryption(convert_str_to_matrix(msg,p,n),key)
            self.result.setText("encrypted Text : " + enc_text)
        else:
            self.showerror("Invalid Key!")

    def decrypt_message(self):
        msg = self.get_message()
        key = self.get_key()
        key, n = check_key(key)
        msg, p = check_msg(msg, n)
        key = convert_str_to_matrix(key,n,n,msg=False)
        inverse = check_key_matrix(key)
        if inverse!="NO_VALID_KEY":
            dec_text = hill_cipher_decryption(convert_str_to_matrix(msg,p,n),inverse)
            self.result.setText("decrypted Text : " + dec_text)
        else:
            self.showerror("Invalid Key!")

    def define_widgets(self):
        self.message = self.findChild(QtWidgets.QLineEdit, "msg")
        self.key = self.findChild(
            QtWidgets.QLineEdit, "key")
        self.enc_btn = self.findChild(QtWidgets.QPushButton, "enc_btn")
        self.dec_btn = self.findChild(QtWidgets.QPushButton, "dec_btn")
        self.result = self.findChild(QtWidgets.QLineEdit, "result")


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
