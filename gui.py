from PyQt5 import QtWidgets, uic
from cipher import hill_cipher_encryption, preprocess_inputs, hill_cipher_decryption
from utils import check_key, check_msg
import sys


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
        if "~" in msg:
            self.showerror("you can't use ~ in your message")
            exit()
        elif "~" in key:
            self.showerror("you can't use ~ in your key")
            exit()
        key, n = check_key(key)
        msg, p = check_msg(msg, n)
        enc_text = hill_cipher_encryption(
            *preprocess_inputs(msg, key, n, p))
        if enc_text != False:
            self.result.setText("encrypted Text : " + enc_text)
        else:
            self.showerror("Invalid Key!")

    def decrypt_message(self):
        msg = self.get_message()
        key = self.get_key()
        key, n = check_key(key)
        msg, p = check_msg(msg, n)
        dec_text = hill_cipher_decryption(
            *preprocess_inputs(msg, key, n, p))
        if dec_text != False:
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
