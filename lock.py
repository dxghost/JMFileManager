import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'PASSWORD'
        self.left = 10
        self.top = 10
        self.width = 720
        self.height = 640
        self.initUI()
    def wrongpasswindow(self):
        self.app = QApplication(sys.argv)
        self.w = QWidget()
        self.l = QLabel('Your password is wrong!!')
        self.V_box = QVBoxLayout()
        self.V_box.addWidget(self.l)
        self.w.setLayout(self.V_box)
        self.w.setWindowTitle('Warning')
        self.w.show()
        sys.exit(app.exec_())
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        
        self.getText()
        self.Agree()
 
    def getText(self):
        self.text, okPressed = QInputDialog.getText(self, "PASSWORD","Password :", QLineEdit.Normal, "")
        if okPressed and self.text != '':
            return self.text
    def Agree(self):
        self.password = 'tmoj.1428'
        if self.text == self.password:
            sys.exit(app.exec_())
        else :
            self.wrongpasswindow()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
