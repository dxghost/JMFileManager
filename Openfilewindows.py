# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Openfolder(object):
    def setupUi(self, Openfolder):
        Openfolder.setObjectName("Openfolder")
        Openfolder.resize(700, 130)
        Openfolder.setMinimumSize(QtCore.QSize(700, 130))
        Openfolder.setMaximumSize(QtCore.QSize(700, 130))
        self.centralwidget = QtWidgets.QWidget(Openfolder)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 42, 121, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 551, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        Openfolder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Openfolder)
        self.statusbar.setObjectName("statusbar")
        Openfolder.setStatusBar(self.statusbar)
        self.comboBox.currentText()
        self.retranslateUi(Openfolder)
        QtCore.QMetaObject.connectSlotsByName(Openfolder)

    def retranslateUi(self, Openfolder):
        _translate = QtCore.QCoreApplication.translate
        Openfolder.setWindowTitle(_translate("Openfolder", "MainWindow"))
        self.label.setText(_translate("Openfolder", "Enter Your Address"))
        self.pushButton.setText(_translate("Openfolder", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Openfolder = QtWidgets.QMainWindow()
    ui = Ui_Openfolder()
    ui.setupUi(Openfolder)
    Openfolder.show()
    sys.exit(app.exec_())

