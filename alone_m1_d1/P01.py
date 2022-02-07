import sys

import matplotlib.pyplot as plt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import P03


class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def doA(self):

        try:
            P03.doA()
        except Exception as e:
            print(e)
        pm = QPixmap('bream.jpg')
        self.qlabel.setPixmap(pm)
        self.qlabel.resize(pm.width(),pm.height())

    def doB(self):
        length = self.YV.text()
        weight = self.XV.text()
        P03.doB(length,weight)
        pm = QPixmap('bream.jpg')
        self.qlabel.setPixmap(pm)
        self.qlabel.resize(pm.width(), pm.height())

    def initUi(self):
        self.qlabel = QLabel('label',self)
        pm = QPixmap('Giga.png')
        self.qlabel.setPixmap(pm)
        self.qlabel.move(20,50)

        self.btn = QPushButton("그래프",self)
        self.btn.move(700,230)
        self.btn.clicked.connect(self.doA)

        self.btn2 = QPushButton("예측하기",self)
        self.btn2.move(700,350)
        self.btn2.clicked.connect(self.doB)

        self.X = QLabel('X',self)
        self.X.move(650,250)
        self.XV = QLineEdit(self)
        self.XV.move(650,270)
        self.Y = QLabel('Y',self)
        self.Y.move(650,300)
        self.YV = QLineEdit(self)
        self.YV.move(650,320)

        self.setWindowTitle("graph")
        self.move(300,300)
        self.resize(800,600)
        self.show()

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())