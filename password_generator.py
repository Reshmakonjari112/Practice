from ui_random_password import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.Qt import QIntValidator
import random, copy
import sys

class MainController(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.radiobtn_low.clicked.connect(lambda: self.calculate('low'))
        self.ui.radiobtn_medium.clicked.connect(lambda: self.calculate('medium'))
        self.ui.radiobtn_strong.clicked.connect(lambda: self.calculate('high'))
        self.ui.btn_generate.clicked.connect(self.generate)

    def generate(self):
        self.ui.txt_length_passowrd.clear()
        self.ui.txt_password.clear()


    def calculate(self, strength):
        validator = QIntValidator()
        self.ui.txt_length_passowrd.setValidator(validator)
        self.ui.txt_length_passowrd.setMaxLength(10)
        length_of_password = self.ui.txt_length_passowrd.text()

        lower = "abcdefghijklmnopqrstuvwxyz"
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
        password = " "

        if length_of_password == '':
            QMessageBox.information(self, "Information" , "Please select strength for password.")
        else:
            if strength == 'low':
                for i in range(0, int(length_of_password)):
                    password = password + random.choice(lower)

            elif strength == 'medium':
                for i in range(0, int(length_of_password)):
                    password = password + random.choice(upper)

            elif strength == 'high':
                for i in range(0, int(length_of_password)):
                    password = password + random.choice(digits)

        self.ui.txt_password.setText(password)
        return password

def main():
    app = QApplication(sys.argv)
    window = MainController()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
