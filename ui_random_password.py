# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'random_password.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(425, 198)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_password = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_password.setReadOnly(True)
        self.txt_password.setObjectName("txt_password")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_password)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.btn_copy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_copy.setObjectName("btn_copy")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_copy)
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setObjectName("btn_generate")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.btn_generate)
        self.gridLayout.addLayout(self.formLayout_3, 0, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_length_passowrd = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_length_passowrd.setObjectName("txt_length_passowrd")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_length_passowrd)
        self.gridLayout.addLayout(self.formLayout_2, 2, 0, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.radiobtn_low = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobtn_low.setObjectName("radiobtn_low")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radiobtn_low)
        self.radiobtn_medium = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobtn_medium.setObjectName("radiobtn_medium")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radiobtn_medium)
        self.radiobtn_strong = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobtn_strong.setObjectName("radiobtn_strong")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radiobtn_strong)
        self.gridLayout.addLayout(self.formLayout_4, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 425, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Generator"))
        self.label.setText(_translate("MainWindow", "Password"))
        self.btn_copy.setText(_translate("MainWindow", "Copy"))
        self.btn_generate.setText(_translate("MainWindow", "Reset"))
        self.label_2.setText(_translate("MainWindow", "Length"))
        self.radiobtn_low.setText(_translate("MainWindow", "Low"))
        self.radiobtn_medium.setText(_translate("MainWindow", "Medium"))
        self.radiobtn_strong.setText(_translate("MainWindow", "Strong"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

