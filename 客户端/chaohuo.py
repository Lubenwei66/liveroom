# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from hb import tp
import random
import re
import sys


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        # label3 = QLabel(self)
        # label3.setPixmap(QPixmap('AID1806-1920.jpg'))
        self.setWindowTitle('弹幕')
        self.setGeometry(0, 0, 1480, 930)

    def initAnimation(self, text):
        tp1(text)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('name.png'))
        self.label.setGeometry(1480, 0, 156, 110)
        self.label1 = QLabel(self)
        self.label1.setPixmap(QPixmap('10.png'))
        self.label1.setStyleSheet(
            "QLabel{border-image:url(./name4.png)}")
        self.label1.setGeometry(1636, 42, QPixmap('10.png').width(), 36)
        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap('name5.png'))
        self.label2.setGeometry(1636 + QPixmap('10.png').width(), 42, 166, 36)
        self.anim = QPropertyAnimation(self.label1, b'pos')
        self.anim.setDuration(20000)  # 20秒完成移动
        self.anim.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.anim.setEndValue(
            QPointF(-400 - QPixmap('10.png').width(), 42))  # 结束位置
        self.anim.start()  # 弹幕开始移动
        self.anim1 = QPropertyAnimation(self.label, b'pos')
        self.anim1.setDuration(20000)  # 20秒完成移动
        self.anim1.setStartValue(QPointF(1480, 0))  # 开始位置
        self.anim1.setEndValue(
            QPointF(-400 - 156 - QPixmap('10.png').width(), 0))  # 结束位置
        self.anim1.start()  # 弹幕开始移动
        self.anim2 = QPropertyAnimation(self.label2, b'pos')
        self.anim2.setDuration(20000)  # 20秒完成移动
        self.anim2.setStartValue(
            QPointF(1480 + 156 + QPixmap('10.png').width(), 42))  # 开始位置
        self.anim2.setEndValue(QPointF(-400, 42))  # 结束位置
        self.anim2.start()  # 弹幕开始移动


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.initAnimation('asdAS1')
    ex.show()
    sys.exit(app.exec_())
# self.label6.setGeometry(1200, 960, 400, 50)
