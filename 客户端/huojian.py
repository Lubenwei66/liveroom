# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from threading import Thread
import random
import re
import sys


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        # label3 = QLabel(self)
        # label3.setPixmap(QPixmap('AID1806-1920.jpg'))
        # self.setWindowTitle('弹幕')
        # self.setGeometry(0,0,1480,930)

    def initAnimation(self, text):
        text1 = text[-6:]
        text2 = text[:-6]
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('name2.png'))
        self.label1 = QLabel(self)
        self.label1.setText(text)
        self.label1.setFont(QFont('Microsoft YaHei', 18))
        self.label1.setStyleSheet(
            "QLabel{border-image:url(./name3.png); color:red; }")
        self.label2 = QLabel(self)
        self.label2.setPixmap(QPixmap('name1.png'))
        self.label3 = QLabel(self)
        self.label3.setText(text1)
        self.label3.setFont(QFont('Microsoft YaHei', 18))
        self.anim = QPropertyAnimation(self.label1, b'pos')
        self.anim.setDuration(20000)  # 20秒完成移动
        self.anim.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anim.setEndValue(QPointF(-400 - (24 * len(text)), 40))  # 结束位置
        self.anim.start()  # 弹幕开始移动
        self.anim1 = QPropertyAnimation(self.label, b'pos')
        self.anim1.setDuration(20000)  # 20秒完成移动
        self.anim1.setStartValue(QPointF(1480, 0))  # 开始位置
        self.anim1.setEndValue(
            QPointF(-400 - 210 - (24 * len(text)), 0))  # 结束位置
        self.anim1.start()  # 弹幕开始移动
        self.anim2 = QPropertyAnimation(self.label2, b'pos')
        self.anim2.setDuration(20000)  # 20秒完成移动
        self.anim2.setStartValue(
            QPointF(1480 + 210 + (24 * len(text)), 40))  # 开始位置
        self.anim2.setEndValue(QPointF(-400, 40))  # 结束位置
        self.anim2.start()  # 弹幕开始移动
        self.anim3 = QPropertyAnimation(self.label3, b'pos')
        self.anim3.setDuration(20000)  # 20秒完成移动
        self.anim3.setStartValue(
            QPointF(1480 + 210 + (24 * len(text2)), 40))  # 开始位置
        self.anim3.setEndValue(QPointF(-400 - 24 * len(text1), 40))  # 结束位置
        self.anim3.start()  # 弹幕开始移动


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.initAnimation('ＸＸＸ送了一发火箭')
    ex.show()
    sys.exit(app.exec_())
