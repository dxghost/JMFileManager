import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        self.imageLabel = QLabel()
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setBackgroundRole(QPalette.Base)
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.layout = QGridLayout()
        self.layout.addWidget(self.imageLabel)
        self.setLayout(self.layout)
        self.resize(431, 641)
        self.show()

    def open(self, path):

        fileName = path
        if fileName:
            image = QImage(fileName)
            if image.isNull():
                QMessageBox.information(self, "Image Viewer",
                                        "Cannot load %s." % fileName)
                return

            self.imageLabel.setPixmap(QPixmap.fromImage(image))
            self.scaleFactor = 1.0
            self.fitToWindow()

    def QSizeToTuple(self, QSize):
        tupledSizeListStr = (str(QSize).split('('))[1][:len((str(QSize).split('('))[1]) - 1].split(',')
        tupledSize = (int(tupledSizeListStr[0]), int(tupledSizeListStr[1]))
        return tupledSize

    def fitToWindow(self):
        imageSize = self.QSizeToTuple(self.imageLabel.pixmap().size())
        windowSize = self.QSizeToTuple(self.size())
        factor = min(windowSize[0] / imageSize[0], windowSize[1] / imageSize[1])
        print(min(windowSize[0] / imageSize[0], windowSize[1] / imageSize[1]))
        print((windowSize[0], imageSize[0], windowSize[1], imageSize[1]))
        self.scaleFactor *= factor
        self.imageLabel.resize(self.scaleFactor * self.imageLabel.pixmap().size())
        print(self.imageLabel.size())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.open('D:\\Pictures\\Baby Wallpapers\\4K\\325.jpg')
    sys.exit(app.exec_())
