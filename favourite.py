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

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 15, 121, 16))
        self.label_1.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 15, 600, 16))
        self.label_2.setObjectName("label")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 40, 551, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 70, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 70, 140, 28))
        self.pushButton_2.setObjectName("pushButton")
        Openfolder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Openfolder)
        self.statusbar.setObjectName("statusbar")
        Openfolder.setStatusBar(self.statusbar)
        self.retranslateUi(Openfolder)
        QtCore.QMetaObject.connectSlotsByName(Openfolder)

    def retranslateUi(self, Openfolder):
        _translate = QtCore.QCoreApplication.translate
        Openfolder.setWindowTitle(_translate("Openfolder", "MainWindow"))
        self.label.setText(_translate("Openfolder", "Favourite Address" ))
        self.pushButton.setText(_translate("Openfolder", "Go"))
        self.pushButton_2.setText(_translate("Openfolder", "Add to Favourite list"))
        self.label_1.setText(_translate("Openfolder", "Current Address" ))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Openfolder = QtWidgets.QMainWindow()
    ui = Ui_Openfolder()
    ui.setupUi(Openfolder)
    Openfolder.show()
    sys.exit(app.exec_())

