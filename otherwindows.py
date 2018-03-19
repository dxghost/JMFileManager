# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindos(object):
    def setupUi(self, OtherWindos):
        OtherWindos.setObjectName("OtherWindos")
        OtherWindos.resize(400, 200)
        OtherWindos.setMaximumHeight(200)
        OtherWindos.setMaximumWidth(400)
        OtherWindos.setMinimumHeight(200)
        OtherWindos.setMinimumWidth(400)
        self.centralwidget = QtWidgets.QWidget(OtherWindos)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 68, 261, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 110, 93, 28))
        self.pushButton.setObjectName("pushButton")
        OtherWindos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OtherWindos)
        self.statusbar.setObjectName("statusbar")
        OtherWindos.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindos)
        QtCore.QMetaObject.connectSlotsByName(OtherWindos)

        print(self.lineEdit.text())
        self.pushButton.text()
    def retranslateUi(self, OtherWindos):
        _translate = QtCore.QCoreApplication.translate
        OtherWindos.setWindowTitle(_translate("OtherWindos", "MainWindow"))
        self.label.setText(_translate("OtherWindos", "Enter Folder Name:"))
        self.pushButton.setText(_translate("OtherWindos", "OK"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    OtherWindos = QtWidgets.QMainWindow()
    ui = Ui_OtherWindos()
    ui.setupUi(OtherWindos)
    OtherWindos.show()
    sys.exit(app.exec_())
