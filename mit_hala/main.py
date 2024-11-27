import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, QStackedWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QFont
from PyQt5.uic import loadUi


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi('login.ui', self)
        self.btn_login.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):
        email = self.txt_email.text()
        password = self.txt_password.text()

        if email == 'a@gmail.com' and password == '1234':
            print("Welcome to your account")
        else:
            self.label_error.setText('Invalid credentials!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
