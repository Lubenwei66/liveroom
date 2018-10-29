#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from PIL import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from cv2 import *
import zlib
import struct
import pickle
import numpy
import sys
import time
from socket import *
from chat_client import *
from login_interface import *
import threading
import pyaudio
import wave
import random
from alipay import AliPay
import qrcode
from zhifubao import *
from hb import *

alipay_public_key_string = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA3SR2KYvarYLqO74YKfMs1y7YF/3It9grR0y2138s920sq4yGjdvGgbpBtkSecaVrvPVTMtQJ1t/l8UAV4Tfy1TfL2ey0S+znbP5gKguqdWqwaJYTo3N5/k2SiEStlq/OBpoAgYwn0mfu6BGol0p0c4ZYimbfSeJLk4W5AUuifHROuEIHPbtKOUrYER8N+KGx9qcYBw9dZxRb0QgtVnehtMGDp9mvpo9NvUuUUYIMpoA9G64lgL6Q5revuJVKCaROj/YJMK1fl9gkI1i07ze7lw+sjMWkHB/z2SN6wecCYUC9OnwHrZgYYM18Ls0vvG7Ebpc+iV1/yoH5NB8YhDHEAwIDAQAB
-----END PUBLIC KEY-----'''


app_private_key_string = '''-----BEGIN RSA PRIVATE KEY-----
    MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC/GK4uK/73ZDdp4ovyWZMiH4nJEnFm1olwFsh14K6bCTagj40yZCr2gnsMnE5NYrVFJwgEPqyWx5d8HPq0qjIFk/jfNCnn86KFzOt3r4QeTNNg2ZoyGXS1kB+zLUvkQBHnVtcIK8YRNrYUdbf7c1XVtm+yRj86TOYsjdvsWVwi4OvHWw4nzvAK0WvHZLnAhY9y3JKsPQ5JBWMBRXWp4I+TjEcKJEDqUPzal1mddWMZ2mrynYnp/MRC+nsSY6/DKzXTt1E6U9b4RJsWNqdgvCUcWGL0XMEBXoACYJ/nmyRgIi/bM1tJd13ofoJh4BNeVdM5HBspepdawyzCybKgu97rAgMBAAECggEADFHKAN4DPO2wCNp7DS+rJZsE5fqTZv7Ts280kyzd9M6+P9GhV6tPfb7hseltvt1rND8U7DkiJUJOyMiRfQ4v1V45wCH7xaFWS+vvDjM5gD6Rrf+5ShuMA5x7/rAf4WIkBVb62+L+jOOLD3ybVNGVqgZt4v9WWirU9/BZSj5kizb6DribgAPjp1W3s1yT+BlbtxmK1KIMYWk4I6Is+zirfjRbyMpbovIkP8jtt1SCXTobR+BGL7ibkCxPPHxbaUSd4Djs4dbL0JQchPar0EWSSUgH3gtYqKWWJkdfCPzlQYagl9F/zbcHUYODFueLbccG44H97CJam5aHZeXggqxWyQKBgQD+uQyu7z2X2rEF/8MgINR8DYrsJYGXkd7RH89lSaTQ/WYuCv7EIUn0SgxLEmlyZeuJraXOq6y1tnNOGMWDz7Sy3MCYdUftMbMJTJbSBrApMFUS1+WQmtFFRuv3P6Bl3jq+qgikEnmgK8RuDMfwcdYl4cXQ5vufydGqQ3xJJhK+twKBgQDADfaAJSehyxkA1EctXa//Ed5ZQuB8BQkHQXrfwd4lyCVfCBr6rSsx5IM1ynj2mKNpmhDAg+Jt33xdlP/pkLJeEvgb6XtNPpr0jCw86AzrcyyBnC4SpoWL7u1Wp2C0i3wRAYlC/KbKPzDsf5db3EsLC008YGlZ+HyCDBnS4BmtbQKBgGD8IkklDEWaXdaT6D5+YYkOOvvo1+vW/YiQXQ4KuTddlB8pzpDsv9TEsOOQkhedmM3mEQCcuvjBDCwLIIEsf3eut6IU3ZsBVlLPF4nGRCKapXm0PFMPr2h6NXQBhNfkgmeAJCQcaLTElVj1gtcY8NmhmgkNOXdAh5UVduf/GBoHAoGATZrWyn05AIXC+rTMdiZvYZBk2ojNkQ+v0EDDV/tMutOfVkE+NaEX3TdLVccVDgAruBZLQp+INYGjDWWR611O1fiwTQcRjesITlz92zahUdreVxk2/M5RFHRdbzB/QTVD0tNeFbVl6D+Uk1wTW0kvAa11bjo/F93y4dHl9XIcrhkCgYAYjuJaGNqdM1Sz9ZGXdvARmdeZqSerp13xw1BM0yikhlrYSGWcz4uagx71SrK6jNH9ptQ6KlAKjLmwOFfXxqpj+4ZigdM6JhH7Y/LAbAE2/L7kDswQqj4QT+URyup5rZc0cxZKSGDAWmolu+bsqbx++ieHb9RkZxAiAdAn/AWyhA==
-----END RSA PRIVATE KEY-----'''

# 注意：一个是支付宝公钥，一个是应用私钥

APP_ID = '2016091700528524'
NOTIFY_URL = 'https://openapi.alipaydev.com/gateway.do'


class MyBtn_1(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_1.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_1.resize(0, 0)


class MyBtn_2(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_2.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_2.resize(0, 0)


class MyBtn_3(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_3.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_3.resize(0, 0)


class MyBtn_4(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_4.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_4.resize(0, 0)


class MyBtn_5(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_5.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_5.resize(0, 0)


class MyBtn_6(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_6.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_6.resize(0, 0)


class MyBtn_7(QPushButton):

    def enterEvent(self, event):
        ni.liwu_gif_7.resize(90, 90)

    def leaveEvent(self, event):
        ni.liwu_gif_7.resize(0, 0)


class client_interface(QWidget):
    signal_write_msg = pyqtSignal(str)
    signal_tou = pyqtSignal(bytes)
    signal = pyqtSignal(bytes)
    signal_gift = pyqtSignal(str)
    signal_buzu = pyqtSignal(str)
    signal_yue = pyqtSignal(str)
    signal_danmu = pyqtSignal(str)
    signal_huojian = pyqtSignal(str)
    signal_chaohuo = pyqtSignal(str)
    signal_zhubodanmu = pyqtSignal(str)
    signal_zhifu = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # self.setWindowFlags(Qt.FramelessWindowHint)

        QApplication.setStyle("Fusion")

        self.data1 = "".encode("utf-8")
        self.data2 = ''.encode('utf-8')
        self.data3 = "".encode("utf-8")
        self.s = None
        self.c = None
        self.z = None
        self.f = None

        # 背景板
        self.beijingban = QLabel(self)
        self.beijingban.setGeometry(0, 0, 1900, 1050)
        picc = QPixmap("img/beijingban.jpg")
        self.beijingban.setPixmap(picc)
        self.beijingban.setScaledContents(True)

        # 桌面共享控件
        self.pictureLabel = QLabel(self)
        self.pictureLabel.setScaledContents(True)
        self.pictureLabel.setGeometry(10, 10, 1480, 930)
        init_image = QPixmap(
            "img/tongbu.png").scaled(self.width(), self.height())
        self.pictureLabel.setPixmap(init_image)
        # self.pictureLabel.showFullScreen()

        # 摄像头控件
        self.pictureLabel_tou = QLabel(self)
        self.pictureLabel_tou.setScaledContents(True)
        self.pictureLabel_tou.setGeometry(990, 740, 300, 200)
        init_image = QPixmap(
            "img/tongbu.png").scaled(self.width(), self.height())
        self.pictureLabel_tou.setPixmap(init_image)

        # self.sld = QSlider(Qt.Horizontal, self)
        # self.sld.setFocusPolicy(Qt.NoFocus)
        # self.sld.setGeometry(1260, 970, 80, 20)
        # self.sld.valueChanged[int].connect(self.changeValue)

        # self.sld_label = QLabel(self)
        # self.sld_label.setPixmap(QPixmap('img/mute.png'))
        # self.sld_label.setGeometry(1350, 970, 80, 20)

        # 金币标签
        self.money = 0
        self.label_money = QLabel("金币:", self)
        self.label_money.setGeometry(1260, 960, 50, 20)
        self.label_money.setFont(QFont("Microsoft YaHei", 12))
        self.label_money.setStyleSheet("QLabel{color: #FF6600}")

        self.label_money_sql = QLabel(str(0), self)
        self.label_money_sql.setGeometry(1305, 960, 150, 20)
        self.label_money_sql.setFont(QFont("Microsoft YaHei", 12))
        self.label_money_sql.setStyleSheet("QLabel{color: #FF6600}")

        # 充值按钮
        self.rechargeButton = QPushButton(self)
        self.rechargeButton.setText("充值")
        # self.rechargeButton.setIcon(QIcon("img/进.png"))
        self.rechargeButton.setGeometry(220, 960, 80, 30)
        self.rechargeButton.setFont(QFont("Microsoft YaHei", 12))
        self.rechargeButton.setStyleSheet("QPushButton{color:#00FFFF}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:#FF6600}"
                                          "QPushButton{border:2px}"
                                          # "QPushButton{border-radius:10px}"
                                          "QPushButton{padding:2px 4px}")
        self.gold = QLineEdit(self)
        self.gold.setGeometry(149, 960, 71, 30)
        self.gold.setStyleSheet("QLineEdit{color:#CC6633}"
                                "QLineEdit:hover{color:#FF6600}"
                                "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                "QLineEdit{padding:2px 4px}")
        self.jine = self.gold.text()

        # 礼物按钮

        self.liwu_gif_1 = QLabel(self)
        self.liwu_gif_1.setGeometry(750, 855, 0, 0)
        self.liwu_gif_1.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_1 = QMovie('img/suphuojian.gif')
        self.liwu_gif_1.setMovie(self.gif_1)
        self.gif_1.start()
        self.Button_liwu1 = MyBtn_1(self)
        # self.Button_liwu1 = MyBtn(1)
        self.Button_liwu1.setToolTip("点击送主播超级火箭(2000金币)")
        self.Button_liwu1.setStyleSheet(
            "QPushButton{border-image:url(img/超级火箭.png);}")
        self.Button_liwu1.setGeometry(700, 945, 50, 50)

        self.liwu_gif_2 = QLabel(self)
        self.liwu_gif_2.setGeometry(810, 855, 0, 0)
        self.liwu_gif_2.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_2 = QMovie('img/huojian.gif')
        self.liwu_gif_2.setMovie(self.gif_2)
        self.gif_2.start()
        self.Button_liwu2 = MyBtn_2(self)
        self.Button_liwu2.setToolTip("点击送主播火箭(100金币)")
        self.Button_liwu2.setStyleSheet(
            "QPushButton{border-image:url(img/火箭.png)};}")
        self.Button_liwu2.setGeometry(760, 945, 50, 50)

        self.liwu_gif_3 = QLabel(self)
        self.liwu_gif_3.setGeometry(870, 855, 0, 0)
        self.liwu_gif_3.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_3 = QMovie('img/feiji.gif')
        self.liwu_gif_3.setMovie(self.gif_3)
        self.gif_3.start()
        self.Button_liwu3 = MyBtn_3(self)
        self.Button_liwu3.setToolTip("点击送主播飞机(100金币)")
        self.Button_liwu3.setStyleSheet(
            "QPushButton{border-image:url(img/飞机.png)};}")
        self.Button_liwu3.setGeometry(820, 945, 50, 50)

        self.liwu_gif_4 = QLabel(self)
        self.liwu_gif_4.setGeometry(930, 855, 0, 0)
        self.liwu_gif_4.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_4 = QMovie('img/banka.gif')
        self.liwu_gif_4.setMovie(self.gif_4)
        self.gif_4.start()
        self.Button_liwu4 = MyBtn_4(self)
        self.Button_liwu4.setToolTip("点击送主播办卡(6金币)")
        self.Button_liwu4.setStyleSheet(
            "QPushButton{border-image:url(img/办卡.png);}")
        self.Button_liwu4.setGeometry(880, 945, 50, 50)

        self.liwu_gif_5 = QLabel(self)
        self.liwu_gif_5.setGeometry(990, 855, 0, 0)
        self.liwu_gif_5.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_5 = QMovie('img/feidie.gif')
        self.liwu_gif_5.setMovie(self.gif_5)
        self.gif_5.start()
        self.Button_liwu5 = MyBtn_5(self)
        self.Button_liwu5.setToolTip("点击送主播飞碟(1金币)")
        self.Button_liwu5.setStyleSheet(
            "QPushButton{border-image:url(img/飞碟.png);}")
        self.Button_liwu5.setGeometry(940, 945, 50, 50)

        self.liwu_gif_6 = QLabel(self)
        self.liwu_gif_6.setGeometry(1050, 855, 0, 0)
        self.liwu_gif_6.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_6 = QMovie('img/ruoji.gif')
        self.liwu_gif_6.setMovie(self.gif_6)
        self.gif_6.start()
        self.Button_liwu6 = MyBtn_6(self)
        self.Button_liwu6.setToolTip("点击送主播弱鸡(0.2金币)")
        self.Button_liwu6.setStyleSheet(
            "QPushButton{border-image:url(img/弱鸡.png);}")
        self.Button_liwu6.setGeometry(1000, 945, 50, 50)

        self.liwu_gif_7 = QLabel(self)
        self.liwu_gif_7.setGeometry(1100, 855, 0, 0)
        self.liwu_gif_7.setStyleSheet(
            "QLabel{background-color:rgb(255,255,255);}")
        self.gif_7 = QMovie('img/zan.gif')
        self.liwu_gif_7.setMovie(self.gif_7)
        self.gif_7.start()
        self.Button_liwu7 = MyBtn_7(self)
        self.Button_liwu7.setToolTip("点击送主播赞(0.1金币)")
        self.Button_liwu7.setStyleSheet(
            "QPushButton{border-image:url(img/赞.png);}")
        self.Button_liwu7.setGeometry(1060, 945, 50, 50)

        # 礼物按钮
        self.Button_liwu1.clicked.connect(self.suphuojian)
        self.Button_liwu2.clicked.connect(self.huojian)
        self.Button_liwu3.clicked.connect(self.feiji)
        self.Button_liwu4.clicked.connect(self.banka)
        self.Button_liwu5.clicked.connect(self.youting)
        self.Button_liwu6.clicked.connect(self.ruoji)
        self.Button_liwu7.clicked.connect(self.zan)
        self.rechargeButton.clicked.connect(self.chongzhi)

        # 发送文字的文本框
        self.send_edit = QTextEdit(self)
        self.send_edit.setFont(QFont("Microsoft YaHei", 15))
        self.send_edit.setGeometry(1495, 910, 320, 80)
        self.send_edit.setStyleSheet(
            "QTextEdit{background-image:url(img/聊天背景.jpg)}"
            "QTextEdit{padding:2px 4px #CC6600}")

        # 发送消息按钮
        self.sendButton = QPushButton(self)
        self.sendButton.setText("发送")
        # self.sendButton.setIcon(QIcon("img/进.png"))
        self.sendButton.setGeometry(1815, 910, 80, 80)
        self.sendButton.setStyleSheet("QPushButton{color:white}"
                                      "QPushButton:hover{color:black}"
                                      "QPushButton{background-color:#CC6600}"
                                      "QPushButton{border:2px}"
                                      "QPushButton{padding:2px 4px}")
        self.sendButton.setFont(QFont("Microsoft YaHei", 17))

        # 设置窗口大小
        self.setGeometry(0, 0, 1905, 1000)

        # 设置标题
        self.setWindowTitle("斗鱼直播")
        self.nicheng = ""
        self.uname = ""

        # 二维码标签
        self.erweima = QLabel(self)
        self.erweima.setGeometry(500, 200, 300, 300)

        # 弹幕标签设置
        self.label1 = QLabel(self)
        self.label1.setFont(QFont("Microsoft YaHei", 25))
        self.label1.setStyleSheet("color: white")
        self.label1.setGeometry(1200, 960, 400, 50)

        self.label2 = QLabel(self)
        self.label2.setFont(QFont("Microsoft YaHei", 25))
        self.label2.setStyleSheet("color: white")
        self.label2.setGeometry(1200, 960, 400, 50)

        self.label3 = QLabel(self)
        self.label3.setFont(QFont("Microsoft YaHei", 25))
        self.label3.setStyleSheet("color: white")
        self.label3.setGeometry(1200, 960, 400, 50)

        self.label4 = QLabel(self)
        self.label4.setFont(QFont("Microsoft YaHei", 25))
        self.label4.setStyleSheet("color: white")
        self.label4.setGeometry(1200, 960, 400, 50)

        self.label5 = QLabel(self)
        self.label5.setFont(QFont("Microsoft YaHei", 25))
        self.label5.setStyleSheet("color: white")
        self.label5.setGeometry(1200, 960, 400, 50)

        self.label6 = QLabel(self)
        self.label6.setFont(QFont("Microsoft YaHei", 25))
        self.label6.setStyleSheet("color: white")
        self.label6.setGeometry(1200, 960, 400, 50)

        self.label7 = QLabel(self)
        self.label7.setFont(QFont("Microsoft YaHei", 25))
        self.label7.setStyleSheet("color: white")
        self.label7.setGeometry(1200, 960, 400, 50)

        self.label8 = QLabel(self)
        self.label8.setFont(QFont("Microsoft YaHei", 25))
        self.label8.setStyleSheet("color: white")
        self.label8.setGeometry(1200, 960, 400, 50)

        self.label9 = QLabel(self)
        self.label9.setFont(QFont("Microsoft YaHei", 25))
        self.label9.setStyleSheet("color: white")
        self.label9.setGeometry(1200, 960, 400, 50)

        self.label10 = QLabel(self)
        self.label10.setFont(QFont("Microsoft YaHei", 25))
        self.label10.setStyleSheet("color: white")
        self.label10.setGeometry(1200, 960, 400, 50)

        self.label11 = QLabel(self)
        self.label11.setFont(QFont("Microsoft YaHei", 25))
        self.label11.setStyleSheet("color: white")
        self.label11.setGeometry(1200, 960, 400, 50)

        self.label12 = QLabel(self)
        self.label12.setFont(QFont("Microsoft YaHei", 25))
        self.label12.setStyleSheet("color: white")
        self.label12.setGeometry(1200, 960, 400, 50)

        self.label13 = QLabel(self)
        self.label13.setFont(QFont("Microsoft YaHei", 25))
        self.label13.setStyleSheet("color: white")
        self.label13.setGeometry(1200, 960, 400, 50)

        self.label14 = QLabel(self)
        self.label14.setFont(QFont("Microsoft YaHei", 25))
        self.label14.setStyleSheet("color: white")
        self.label14.setGeometry(1200, 960, 400, 50)

        self.label15 = QLabel(self)
        self.label15.setFont(QFont("Microsoft YaHei", 25))
        self.label15.setStyleSheet("color: white")
        self.label15.setGeometry(1200, 960, 400, 50)

        self.label16 = QLabel(self)
        self.label16.setFont(QFont("Microsoft YaHei", 25))
        self.label16.setStyleSheet("color: white")
        self.label16.setGeometry(1200, 960, 400, 50)

        self.label17 = QLabel(self)
        self.label17.setFont(QFont("Microsoft YaHei", 25))
        self.label17.setStyleSheet("color: white")
        self.label17.setGeometry(1200, 960, 400, 50)

        self.label18 = QLabel(self)
        self.label18.setFont(QFont("Microsoft YaHei", 25))
        self.label18.setStyleSheet("color: white")
        self.label18.setGeometry(1200, 960, 400, 50)

        self.label19 = QLabel(self)
        self.label19.setFont(QFont("Microsoft YaHei", 25))
        self.label19.setStyleSheet("color: white")
        self.label19.setGeometry(1200, 960, 400, 50)

        self.label20 = QLabel(self)
        self.label20.setFont(QFont("Microsoft YaHei", 25))
        self.label20.setStyleSheet("color: white")
        self.label20.setGeometry(1200, 960, 400, 50)

        # 主播弹幕标签
        self.labelz1 = QLabel(self)
        self.labelz1.setFont(QFont("Microsoft YaHei", 25))
        self.labelz1.setStyleSheet("color: red")
        self.labelz1.setGeometry(1200, 960, 400, 50)

        self.labelz2 = QLabel(self)
        self.labelz2.setFont(QFont("Microsoft YaHei", 25))
        self.labelz2.setStyleSheet("color: red")
        self.labelz2.setGeometry(1200, 960, 400, 50)

        # 弹幕计时器
        self.time1 = QTimer(self)
        self.time2 = QTimer(self)
        self.time3 = QTimer(self)
        self.time4 = QTimer(self)
        self.time5 = QTimer(self)
        self.time6 = QTimer(self)
        self.time7 = QTimer(self)
        self.time8 = QTimer(self)
        self.time9 = QTimer(self)
        self.time10 = QTimer(self)
        self.time11 = QTimer(self)
        self.time12 = QTimer(self)
        self.time13 = QTimer(self)
        self.time14 = QTimer(self)
        self.time15 = QTimer(self)
        self.time16 = QTimer(self)
        self.time17 = QTimer(self)
        self.time18 = QTimer(self)
        self.time19 = QTimer(self)
        self.time20 = QTimer(self)

        # 主播弹幕计时器
        self.timez1 = QTimer(self)
        self.timez2 = QTimer(self)

        # 计时器连接主播弹幕释放函数
        self.timez1.timeout.connect(self.zshifang1)
        self.timez2.timeout.connect(self.zshifang2)

        # 计时器连接释放函数
        self.time1.timeout.connect(self.shifang1)
        self.time2.timeout.connect(self.shifang2)
        self.time3.timeout.connect(self.shifang3)
        self.time4.timeout.connect(self.shifang4)
        self.time5.timeout.connect(self.shifang5)
        self.time6.timeout.connect(self.shifang6)
        self.time7.timeout.connect(self.shifang7)
        self.time8.timeout.connect(self.shifang8)
        self.time9.timeout.connect(self.shifang9)
        self.time10.timeout.connect(self.shifang10)
        self.time11.timeout.connect(self.shifang11)
        self.time12.timeout.connect(self.shifang12)
        self.time13.timeout.connect(self.shifang13)
        self.time14.timeout.connect(self.shifang14)
        self.time15.timeout.connect(self.shifang15)
        self.time16.timeout.connect(self.shifang16)
        self.time17.timeout.connect(self.shifang17)
        self.time18.timeout.connect(self.shifang18)
        self.time19.timeout.connect(self.shifang19)
        self.time20.timeout.connect(self.shifang20)

        # 火箭通道1
        self.labelh1 = QLabel(self)
        self.labelh2 = QLabel(self)
        self.labelh3 = QLabel(self)
        self.labelh1.setPixmap(QPixmap('img/name2.png'))
        self.labelh3.setPixmap(QPixmap('img/name1.png'))
        self.labelh2.setPixmap(QPixmap(''))
        self.labelh1.setGeometry(1530, 30, 210, 103)
        self.labelh2.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh3.setGeometry(
            1690 + QPixmap('img/10.png').width() + 150, 40, 190, 36)

        # 火箭通道2
        self.labelh4 = QLabel(self)
        self.labelh5 = QLabel(self)
        self.labelh6 = QLabel(self)
        self.labelh4.setPixmap(QPixmap('img/name2.png'))
        self.labelh6.setPixmap(QPixmap('img/name1.png'))
        self.labelh5.setPixmap(QPixmap(''))
        self.labelh4.setGeometry(1530, 30, 210, 103)
        self.labelh5.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh6.setGeometry(
            1690 + QPixmap('img/10.png').width() + 150, 40, 190, 36)

        # 火箭通道3
        self.labelh7 = QLabel(self)
        self.labelh8 = QLabel(self)
        self.labelh9 = QLabel(self)
        self.labelh7.setPixmap(QPixmap('img/name2.png'))
        self.labelh9.setPixmap(QPixmap('img/name1.png'))
        self.labelh8.setPixmap(QPixmap(''))
        self.labelh7.setGeometry(1530, 30, 210, 103)
        self.labelh8.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh9.setGeometry(
            1690 + QPixmap('img/10.png').width() + 150, 40, 190, 36)

        # 火箭通道4
        self.labelh10 = QLabel(self)
        self.labelh11 = QLabel(self)
        self.labelh12 = QLabel(self)
        self.labelh10.setPixmap(QPixmap('img/name2.png'))
        self.labelh12.setPixmap(QPixmap('img/name1.png'))
        self.labelh11.setPixmap(QPixmap(''))
        self.labelh10.setGeometry(1530, 30, 210, 103)
        self.labelh11.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh12.setGeometry(
            1690 + QPixmap('img/10.png').width() + 150, 40, 190, 36)

        # 火箭通道5
        self.labelh13 = QLabel(self)
        self.labelh14 = QLabel(self)
        self.labelh15 = QLabel(self)
        self.labelh13.setPixmap(QPixmap('img/name2.png'))
        self.labelh15.setPixmap(QPixmap('img/name1.png'))
        self.labelh14.setPixmap(QPixmap(''))
        self.labelh13.setGeometry(1530, 30, 210, 103)
        self.labelh14.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh15.setGeometry(
            1690 + QPixmap('img/10.png').width() + 150, 40, 190, 36)

        # 火箭通道6
        self.labelh16 = QLabel(self)
        self.labelh17 = QLabel(self)
        self.labelh18 = QLabel(self)
        self.labelh16.setPixmap(QPixmap('img/name2.png'))
        self.labelh18.setPixmap(QPixmap('img/name1.png'))
        self.labelh17.setPixmap(QPixmap(''))
        self.labelh16.setGeometry(1530, 30, 210, 103)
        self.labelh17.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh18.setGeometry(
            1690 + QPixmap('img/10.png').width() + 150, 40, 190, 36)

        # 火箭计时器
        self.timeh1 = QTimer(self)
        self.timeh2 = QTimer(self)
        self.timeh3 = QTimer(self)
        self.timeh4 = QTimer(self)
        self.timeh5 = QTimer(self)
        self.timeh6 = QTimer(self)

        # 计时器连接火箭通道释放函数
        self.timeh1.timeout.connect(self.shifangh1)
        self.timeh2.timeout.connect(self.shifangh2)
        self.timeh3.timeout.connect(self.shifangh3)
        self.timeh4.timeout.connect(self.shifangh4)
        self.timeh5.timeout.connect(self.shifangh5)
        self.timeh6.timeout.connect(self.shifangh6)

        # 超级火箭通道1
        self.labelc1 = QLabel(self)
        self.labelc2 = QLabel(self)
        self.labelc3 = QLabel(self)
        self.labelc1.setPixmap(QPixmap('img/name.png'))
        self.labelc3.setPixmap(QPixmap('img/name5.png'))
        self.labelc1.setGeometry(1530, 30, 156, 110)
        self.labelc2.setGeometry(
            1636, 42, QPixmap('img/10.png').width() + 150, 36)
        self.labelc3.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)

        # 超级火箭通道2
        self.labelc4 = QLabel(self)
        self.labelc5 = QLabel(self)
        self.labelc6 = QLabel(self)
        self.labelc4.setPixmap(QPixmap('img/name.png'))
        self.labelc6.setPixmap(QPixmap('img/name5.png'))
        self.labelc4.setGeometry(1530, 30, 156, 110)
        self.labelc5.setGeometry(
            1636, 42, QPixmap('img/10.png').width() + 150, 36)
        self.labelc6.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)

        # 超级火箭通道3
        self.labelc7 = QLabel(self)
        self.labelc8 = QLabel(self)
        self.labelc9 = QLabel(self)
        self.labelc7.setPixmap(QPixmap('img/name.png'))
        self.labelc9.setPixmap(QPixmap('img/name5.png'))
        self.labelc7.setGeometry(1530, 30, 156, 110)
        self.labelc8.setGeometry(
            1636, 42, QPixmap('img/10.png').width() + 150, 36)
        self.labelc9.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)

        # 超级火箭通道4
        self.labelc10 = QLabel(self)
        self.labelc11 = QLabel(self)
        self.labelc12 = QLabel(self)
        self.labelc10.setPixmap(QPixmap('img/name.png'))
        self.labelc12.setPixmap(QPixmap('img/name5.png'))
        self.labelc10.setGeometry(1530, 30, 156, 110)
        self.labelc11.setGeometry(
            1636, 42, QPixmap('img/10.png').width() + 150, 36)
        self.labelc12.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)

        # 超级火箭通道5
        self.labelc13 = QLabel(self)
        self.labelc14 = QLabel(self)
        self.labelc15 = QLabel(self)
        self.labelc13.setPixmap(QPixmap('img/name.png'))
        self.labelc15.setPixmap(QPixmap('img/name5.png'))
        self.labelc13.setGeometry(1530, 30, 156, 110)
        self.labelc14.setGeometry(
            1636, 42, QPixmap('img/10.png').width() + 150, 36)
        self.labelc15.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)

        # 超级火箭通道6
        self.labelc16 = QLabel(self)
        self.labelc17 = QLabel(self)
        self.labelc18 = QLabel(self)
        self.labelc16.setPixmap(QPixmap('img/name.png'))
        self.labelc18.setPixmap(QPixmap('img/name5.png'))
        self.labelc16.setGeometry(1530, 30, 156, 110)
        self.labelc17.setGeometry(
            1636, 42, QPixmap('img/10.png').width() + 150, 36)
        self.labelc18.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)

        # 超级火箭计时器
        self.timec1 = QTimer(self)
        self.timec2 = QTimer(self)
        self.timec3 = QTimer(self)
        self.timec4 = QTimer(self)
        self.timec5 = QTimer(self)
        self.timec6 = QTimer(self)

        # 计时器连接超级火箭通道释放函数
        self.timec1.timeout.connect(self.shifangc1)
        self.timec2.timeout.connect(self.shifangc2)
        self.timec3.timeout.connect(self.shifangc3)
        self.timec4.timeout.connect(self.shifangc4)
        self.timec5.timeout.connect(self.shifangc5)
        self.timec6.timeout.connect(self.shifangc6)

        # 火箭连接
        self.signal_huojian.connect(self.huojiang)

        # 超级火箭信号连接
        self.signal_chaohuo.connect(self.chaohuo)

        # 支付信号连接
        self.signal_zhifu.connect(self.zhifutishi)

        # 定义订单号
        self.out_trade_no = 1

        # 接受消息的文本框
        self.browser = QTextBrowser(self)
        self.browser.setFont(QFont("Microsoft YaHei", 16))
        self.browser.setGeometry(1495, 10, 400, 905)
        self.browser.setStyleSheet("QTextBrowser{background-image: url(img/聊天背景.jpg)}"
                                   "QTextBrowser{padding:2px 4px #CC6600}")

        # self._CloseButton = QPushButton(b'\xef\x81\xb2'.decode("utf-8"), self)
        # self._CloseButton.move(1850, 0)
        # self._CloseButton.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        # self._CloseButton.setFixedWidth(40)
        # # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        # self._CloseButton.setObjectName("CloseButton")
        # self._CloseButton.setToolTip("关闭窗口")
        # self._CloseButton.setStyleSheet("QPushButton{color:#CC6633}"
        #                                 "QPushButton:hover{color:#99FFCC}"
        #                                 "QPushButton{background-color:#262626}"
        #                                 "QPushButton{padding:2px 4px}")
        # # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        # self._CloseButton.setMouseTracking(True)
        # self._CloseButton.clicked.connect(self.close)

        # self._MinimumButton = QPushButton(
        #     b'\xef\x80\xb0'.decode("utf-8"), self)
        # self._MinimumButton.move(1812, 0)
        # # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        # self._MinimumButton.setFont(QFont("Webdings"))
        # self._MinimumButton.setFixedWidth(40)
        # # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        # self._MinimumButton.setObjectName("CloseButton")
        # self._MinimumButton.setToolTip("最小化窗口")
        # self._MinimumButton.setStyleSheet("QPushButton{color:#CC6633}"
        #                                   "QPushButton:hover{color:#99FFCC}"
        #                                   "QPushButton{background-color:#262626}"
        #                                   "QPushButton{padding:2px 4px}")
        # # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        # self._MinimumButton.setMouseTracking(True)
        # self._MinimumButton.clicked.connect(self.showMinimized)

    def addSystemTray(self):
        minimizeAction = QAction("最小化至托盘", self, triggered=self.hide)
        maximizeAction = QAction("最大化", self,
                                 triggered=self.showMaximized)
        restoreAction = QAction("还原", self,
                                triggered=self.showNormal)
        quitAction = QAction("退出", self,
                             triggered=self.close)
        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(minimizeAction)
        self.trayIconMenu.addAction(maximizeAction)
        self.trayIconMenu.addAction(restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(quitAction)
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("img/图标.jpg"))
        self.setWindowIcon(QIcon("img/图标.jpg"))
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.show()
        # sys.exit(self.exec_())

    def closeEvent(self, event):
        if self.trayIcon.isVisible():
            self.trayIcon.hide()

    def __call__(self, host, money, addr):
        self.addSystemTray()
        time.sleep(0.5)
        self.money = money
        self.ADDR5 = addr
        HOST = host
        PORT1 = 7781
        PORT2 = 7777
        PORT3 = 7776
        PORT4 = 7779
        ADDR1 = (HOST, PORT1)
        ADDR2 = (HOST, PORT2)
        ADDR4 = (HOST, PORT4)
        self.ADDR3 = (HOST, PORT3)
        self.c = socket(AF_INET, SOCK_STREAM)
        self.z = socket(AF_INET, SOCK_DGRAM)
        self.s = socket(AF_INET, SOCK_STREAM)
        self.f = socket(AF_INET, SOCK_STREAM)
        try:
            self.s.connect(ADDR1)
        except:
            print('桌面未开放')

        try:
            self.c.connect(ADDR2)
        except:
            print('视频未开放')
        try:
            self.f.connect(ADDR4)
        except:
            print('音频未开放')
        sever_th = threading.Thread(target=self.do_parent, args=(self.ADDR3,))
        client_desk = threading.Thread(target=self.show_video_images)
        client_video = threading.Thread(target=self.show_video_images_tou)
        client_a = threading.Thread(target=self.audio)
        sever_th.setDaemon(True)
        client_desk.setDaemon(True)
        client_video.setDaemon(True)
        client_a.setDaemon(True)
        sever_th.start()
        client_desk.start()
        client_video.start()
        client_a.start()
        self.signal_write_msg.connect(self.write_msg)
        self.signal_tou.connect(self.video_images_tou)
        self.signal.connect(self.video_images)
        self.signal_gift.connect(self.gift)
        self.signal_buzu.connect(self.kejin)
        self.signal_yue.connect(self.yue)
        self.signal_danmu.connect(self.danmu)
        self.signal_zhubodanmu.connect(self.zhubodanmu)
        self.signal_yue.emit(self.money)
        # 弹幕通道列表
        self.l3 = [self.tongdao1, self.tongdao2, self.tongdao3,
                   self.tongdao4, self.tongdao5, self.tongdao6,
                   self.tongdao7, self.tongdao8, self.tongdao9,
                   self.tongdao10, self.tongdao11, self.tongdao12,
                   self.tongdao13, self.tongdao14, self.tongdao15,
                   self.tongdao16, self.tongdao17, self.tongdao18,
                   self.tongdao19, self.tongdao20]
        # 弹幕被占用通道列表
        self.l4 = []
        # 主播弹幕通道列表
        self.zhubo = [self.tongdaoz1, self.tongdaoz2]
        # 主播弹幕通道被占用列表
        self.zhubos = []
        # 火箭通道列表
        self.lht = [self.tongdaoh1, self.tongdaoh2, self.tongdaoh3,
                    self.tongdaoh4, self.tongdaoh5, self.tongdaoh6]
        # 火箭被占用通道列表
        self.lhs = []
        # 超级火箭通道列表
        self.lct = [self.tongdaoc1, self.tongdaoc2, self.tongdaoc3,
                    self.tongdaoc4, self.tongdaoc5, self.tongdaoc6]
        # 超级火箭被占用通道列表
        self.lcs = []

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.m_flag = True
    #         self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
    #         event.accept()
    #         self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    # def mouseMoveEvent(self, QMouseEvent):
    #     if Qt.LeftButton and self.m_flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
    #         QMouseEvent.accept()

    # def mouseReleaseEvent(self, QMouseEvent):
    #     self.m_flag = False
    #     self.setCursor(QCursor(Qt.ArrowCursor))

    def audio(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        # RECORD_SECONDS = 0.5
        if self.f != None:
            payload_size = struct.calcsize("L")
            p = pyaudio.PyAudio()
            try:
                output_index = p.get_default_output_device_info()['index']
            except OSError:
                print('没有音频设备,请检查设备')
                self.f.close()
                return
            stream = None
            try:
                stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                                output=True, frames_per_buffer=CHUNK, output_device_index=output_index)
            except:
                print('设备索引有误，音频退出')
                self.f.close()
            while stream.is_active():
                while True:
                    try:
                        self.data3 += self.f.recv(80000)
                    except:
                        pass
                    p1 = self.data3.find(b'A')
                    if p1 >= 0:
                        packed_size = self.data3[p1 + 1:p1 + payload_size + 1]
                        msg_size = struct.unpack("L", packed_size)[0]
                        msg = self.data3[p1 + payload_size + 1:]
                        if len(msg) < msg_size:
                            while len(msg) < msg_size:
                                msg += self.f.recv(80000)
                            frame_data = msg[:msg_size]
                            self.data3 = msg[msg_size:]
                            frames = pickle.loads(frame_data)
                        else:
                            frame_data = msg[:msg_size]
                            self.data3 = msg[msg_size:]
                            frames = pickle.loads(frame_data)
                        for frame in frames:
                            stream.write(frame, CHUNK)
                if stream is not None:
                    stream.stop_stream()
                    stream.close()
                p.terminate()

    def do_parent(self, ADDR):
        if self.z != None:
            self.z.sendto(b'A ' + self.nicheng.encode(), ADDR)
            while True:
                msg, addr = self.z.recvfrom(1024)
                msg = msg.decode()
                msg = msg.replace("\n", "")
                if msg[0] == "+":
                    msg = '\n' + msg[1:]
                    self.signal_write_msg.emit(msg)
                if msg[0] == "#":
                    msg = '\n' + msg[1:]
                    self.signal_write_msg.emit(msg)
                    msg2 = msg.split(' ')
                    if msg2[1] == "主播":
                        self.signal_zhubodanmu.emit(msg2[-1])
                    else:
                        self.signal_danmu.emit(msg2[-1])
                if msg[0] == '*':
                    self.money = msg[1:]
                    self.signal_yue.emit(self.money)
                if msg == "余额不足":
                    self.signal_buzu.emit(msg)
                if msg == 'Hello':
                    self.z.sendto(b'Hi ' + self.nicheng.encode(), self.ADDR3)
                if msg[0] == "G":
                    msg3 = '\n' + msg[1:]
                    self.signal_write_msg.emit(msg3)
                    msg2 = msg.split(' ')
                    if msg2[-1] == "火箭":
                        print(msg)
                        self.signal_huojian.emit(msg2[1])
                    if msg2[-1] == "超级火箭":
                        self.signal_chaohuo.emit(msg2[1])

    def yue(self, money):
        self.label_money_sql.setText(money)

    def kejin(self):
        ject = QMessageBox.warning(
            self, "!", "余额不足", QMessageBox.Yes)

    def send_msg(self):
        text = self.send_edit.toPlainText()
        if text:
            s = self.z
            addr = self.ADDR3
            name = self.nicheng
            send_message(s, name, addr, text)
            self.send_edit.clear()

    # def connect(self):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # self.comboBox_tcp.currentIndexChanged.connect(self.combobox_change)

    def video_images_tou(self, zframe_data):
        frame_data = zlib.decompress(zframe_data)
        frame = pickle.loads(frame_data)
        height, width = frame.shape[:2]
        if frame.ndim == 3:
            rgb = cvtColor(frame, COLOR_BGR2RGB)
        elif frame.ndim == 2:
            rgb = cvtColor(frame, COLOR_GRAY2BGR)

        temp_image = QImage(rgb.flatten(), width,
                            height, QImage.Format_RGB888)
        temp_pixmap = QPixmap.fromImage(temp_image)
        img = temp_pixmap
        self.pictureLabel_tou.setPixmap(img)

    def video_images(self, zframe_data):
        frame_data = zlib.decompress(zframe_data)
        frame = pickle.loads(frame_data)
        height, width = frame.shape[:2]
        if frame.ndim == 3:
            rgb = cvtColor(frame, COLOR_BGR2RGB)
        elif frame.ndim == 2:
            rgb = cvtColor(frame, COLOR_GRAY2BGR)

        temp_image = QImage(rgb.flatten(), width,
                            height, QImage.Format_RGB888)
        temp_pixmap = QPixmap.fromImage(temp_image)
        img = temp_pixmap
        self.pictureLabel.setPixmap(img)

    def write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        """
        功能函数，向接收区写入数据的方法
        信号-槽触发
        tip：PyQt程序的子线程中，直接向主线程的界面传输字符是不符合安全原则的
        :return: None
        """
        self.browser.insertPlainText(msg)
        # 滚动条移动到结尾
        self.browser.moveCursor(QTextCursor.End)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "是否退出?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.z.sendto(b'Q ' + self.nicheng.encode(), self.ADDR3)
            time.sleep(0.5)
            self.c.close()
            self.s.close()
            self.f.close()
            self.z.close()
            sys.exit(0)
            event.accept()
        else:
            event.ignore()

    def changeValue(self, value):

        if value == 0:
            self.sld_label.setPixmap(QPixmap('img/mute.png'))
        elif value > 0 and value <= 30:
            self.sld_label.setPixmap(QPixmap('img/min.png'))
        elif value > 30 and value < 80:
            self.sld_label.setPixmap(QPixmap('img/med.png'))
        else:
            self.sld_label.setPixmap(QPixmap('img/max.png'))

    def show_video_images(self):
        if self.s != None:
            payload_size = struct.calcsize("L")
            while True:
                try:
                    self.data1 += self.s.recv(80000)
                except:
                    pass
                p = self.data1.find(b'D')
                if p >= 0:
                    packed_size = self.data1[p + 1:p + payload_size + 1]
                    msg_size = struct.unpack("L", packed_size)[0]
                    msg = self.data1[p + payload_size + 1:]
                    if len(msg) < msg_size:
                        while len(msg) < msg_size:
                            msg += self.s.recv(80000)
                        zframe_data = msg[:msg_size]
                        self.data1 = msg[msg_size:]
                        self.signal.emit(zframe_data)
                    else:
                        zframe_data = msg[:msg_size]
                        self.data1 = msg[msg_size:]
                        self.signal[bytes].emit(zframe_data)

    def show_video_images_tou(self):
        if self.c != None:
            payload_size = struct.calcsize("L")
            while True:
                try:
                    self.data2 += self.c.recv(80000)
                except:
                    pass
                p = self.data2.find(b'V')
                if p >= 0:
                    packed_size = self.data2[p + 1:p + payload_size + 1]
                    msg_size = struct.unpack("L", packed_size)[0]
                    msg = self.data2[p + payload_size + 1:]
                    if len(msg) < msg_size:
                        while len(msg) < msg_size:
                            msg += self.c.recv(80000)
                        zframe_data = msg[:msg_size]
                        self.data2 = msg[msg_size:]
                        self.signal_tou.emit(zframe_data)
                    else:
                        zframe_data = msg[:msg_size]
                        self.data2 = msg[msg_size:]
                        self.signal_tou[bytes].emit(zframe_data)

    def chongzhi(self):
        chongzhi_ = threading.Thread(target=self.chongzhihanshu)
        chongzhi_.setDaemon(True)
        chongzhi_.start()

    def zhifutishi(self, sig):
        if sig == '支付成功':
            QMessageBox.question(self, 'Message',
                                 "支付成功!", QMessageBox.Yes)
        if sig == '支付超时':
            QMessageBox.question(self, 'Message',
                                 "支付超时,请重试!", QMessageBox.Yes)
        if sig == '支付失败':
            QMessageBox.question(self, 'Message',
                                 "支付失败,请重试!", QMessageBox.Yes)

    def chongzhihanshu(self):
        jine = self.gold.text()
        if jine:
            try:
                subject = "充值金币"
                total_amount = jine
                self.out_trade_no = int(time.time())
                self.preCreateOrder(subject, self.out_trade_no, total_amount)
                # 按指定路径找到图片，注意路径必须用双引号包围，不能用单引号
                pic = QPixmap("img/erweima.png")
                self.erweima.setPixmap(pic)  # 在label上显示图片
                self.erweima.setScaledContents(True)
                self.query_order()
                # self.zhifutime.start(1000)
            except:
                self.signal_zhifu.emit('支付失败')

    def query_order(self):
        '''
        :param out_trade_no: 商户订单号
        :return: None
        '''
        jine = self.gold.text()
        s = self.z
        addr = self.ADDR3
        uname = self.uname
        subject = "充值金币"
        out_trade_no = self.out_trade_no
        # out_trade_no = int(time.time())
        # print('预付订单已创建,请在120秒内扫码支付,过期订单将被取消！')
        # check order status
        _time = 0
        while True:
            # check every 3s, and 10 times in all

            print("now sleep 1s")
            time.sleep(1)

            result = self.init_alipay_cfg().api_alipay_trade_query(out_trade_no=out_trade_no)
            _time += 1
            if result.get("trade_status", "") == "TRADE_SUCCESS":
                print('订单已支付!')
                print('订单查询返回值：', result)
                self.signal_zhifu.emit('支付成功')
                # self.zhifutime.stop()
                do_chongzhi(s, addr, uname, jine)
                self.erweima.setPixmap(QPixmap(""))

                # time.sleep(1)
                break

            if _time >= 120:
                # cancel_order(out_trade_no, cancel_time)
                self.zhifutime.stop()
                # self.result = "支付超时"
                # self.zhifutime.stop()
                self.erweima.setPixmap(QPixmap(""))
                # QMessageBox.question(self, 'Message',
                #                      "支付超时,请重试!", QMessageBox.Yes)
                self.signal_zhifu.emit('支付超时')
                break

    def preCreateOrder(self, subject: 'order_desc', out_trade_no: int, total_amount: (float, 'eg:0.01')):
        '''
        创建预付订单
        :return None：表示预付订单创建失败  [或]  code_url：二维码url
        '''
        result = self.init_alipay_cfg().api_alipay_trade_precreate(
            subject=subject,
            out_trade_no=out_trade_no,
            total_amount=total_amount)
        print('返回值：', result)
        code_url = result.get('qr_code')
        if not code_url:
            print(result.get('预付订单创建失败：', 'msg'))
            return
        else:
            self.get_qr_code(code_url)

    def init_alipay_cfg(self):
        '''
        初始化alipay配置
        :return: alipay 对象
        '''
        alipay = AliPay(
            appid=APP_ID,
            app_notify_url=NOTIFY_URL,  # 默认回调url
            app_private_key_string=app_private_key_string,
            alipay_public_key_string=alipay_public_key_string,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False ,若开启则使用沙盒环境的支付宝公钥
        )
        return alipay

    def get_qr_code(self, code_url):
        '''
        生成二维码
        :return None
        '''
        # print(code_url)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=1
        )
        qr.add_data(code_url)  # 二维码所含信息
        img = qr.make_image()  # 生成二维码图片
        img.save(r'img/erweima.png')
        print('二维码保存成功！')

    def gift(self, gift):
        s = self.z
        addr = self.ADDR3
        uname = self.uname
        do_gift(s, addr, uname, gift, self.nicheng)

    def suphuojian(self):
        self.signal_gift.emit("超级火箭")

    def huojian(self):
        self.signal_gift.emit("火箭")

    def feiji(self):
        self.signal_gift.emit("飞机")

    def youting(self):
        self.signal_gift.emit("飞碟")

    def zan(self):
        self.signal_gift.emit("赞")

    def ruoji(self):
        self.signal_gift.emit("弱鸡")

    def banka(self):
        self.signal_gift.emit("办卡")

    def danmu(self, text):
        for x in self.l3:
            if x not in self.l4:
                self.l4.append(x)
                x(text)
                print(x(text))
                break

    def zhubodanmu(self, text):
        for x in self.zhubo:
            if x not in self.zhubos:
                self.zhubos.append(x)
                x(text)
                print(x(text))
                break

    def tongdaoz1(self,  text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.labelz1.setText(text)
        self.labelz1.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.labelz1.setPalette(palette)
        self.animz1 = QPropertyAnimation(self.labelz1, b'pos')
        self.animz1.setDuration(20000)
        self.animz1.setStartValue(QPointF(1150 + self.labelz1.width(), x))
        self.animz1.setEndValue(QPointF(-self.labelz1.width(), x))
        self.animz1.start()
        self.timez1.start(20000)

    def tongdaoz2(self,  text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.labelz2.setText(text)
        self.labelz2.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.labelz2.setPalette(palette)
        self.animz2 = QPropertyAnimation(self.labelz2, b'pos')
        self.animz2.setDuration(20000)
        self.animz2.setStartValue(QPointF(1150 + self.labelz2.width(), x))
        self.animz2.setEndValue(QPointF(-self.labelz2.width(), x))
        self.animz2.start()
        self.timez2.start(20000)

    def tongdao1(self,  text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label1.setText(text)
        self.label1.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label1.setPalette(palette)
        self.anim1 = QPropertyAnimation(self.label1, b'pos')
        self.anim1.setDuration(20000)
        self.anim1.setStartValue(QPointF(1150 + self.label1.width(), x))
        self.anim1.setEndValue(QPointF(-self.label1.width(), x))
        self.anim1.start()
        self.time1.start(20000)

    def tongdao2(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label2.setText(text)
        print(self.label2.width())
        # self.label2.setScaledContents(True)
        self.label2.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label2.setPalette(palette)
        self.anim2 = QPropertyAnimation(self.label2, b'pos')
        self.anim2.setDuration(20000)
        self.anim2.setStartValue(QPointF(1150 + self.label2.width(), x))
        self.anim2.setEndValue(QPointF(-self.label2.width(), x))
        self.anim2.start()
        self.time2.start(20000)

    def tongdao3(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label3.setText(text)
        print(self.label3.width())
        # self.label3.setScaledContents(True)
        self.label3.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label3.setPalette(palette)
        self.anim3 = QPropertyAnimation(self.label3, b'pos')
        self.anim3.setDuration(20000)
        self.anim3.setStartValue(QPointF(1150 + self.label3.width(), x))
        self.anim3.setEndValue(QPointF(-self.label3.width(), x))
        self.anim3.start()
        print("chengong")
        self.time3.start(20000)

    def tongdao4(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label4.setText(text)
        print(self.label4.width())
        # self.label4.setScaledContents(True)
        self.label4.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label4.setPalette(palette)
        self.anim4 = QPropertyAnimation(self.label4, b'pos')
        self.anim4.setDuration(20000)
        self.anim4.setStartValue(QPointF(1150 + self.label4.width(), x))
        self.anim4.setEndValue(QPointF(-self.label4.width(), x))
        self.anim4.start()
        print("chengong")
        self.time4.start(20000)

    def tongdao5(self,  text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label5.setText(text)
        print(self.label5.width())
        # self.label5.setScaledContents(True)
        self.label5.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label5.setPalette(palette)
        self.anim5 = QPropertyAnimation(self.label5, b'pos')
        self.anim5.setDuration(20000)
        self.anim5.setStartValue(QPointF(1150 + self.label5.width(), x))
        self.anim5.setEndValue(QPointF(-self.label5.width(), x))
        self.anim5.start()
        self.time5.start(20000)

    def tongdao6(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label6.setText(text)
        print(self.label6.width())
        # self.label6.setScaledContents(True)
        self.label6.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label6.setPalette(palette)
        self.anim6 = QPropertyAnimation(self.label6, b'pos')
        self.anim6.setDuration(20000)
        self.anim6.setStartValue(QPointF(1150 + self.label6.width(), x))
        self.anim6.setEndValue(QPointF(-self.label6.width(), x))
        self.anim6.start()
        self.time6.start(20000)

    def tongdao7(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label7.setText(text)
        print(self.label7.width())
        # self.label7.setScaledContents(True)
        self.label7.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label7.setPalette(palette)
        self.anim7 = QPropertyAnimation(self.label7, b'pos')
        self.anim7.setDuration(20000)
        self.anim7.setStartValue(QPointF(1150 + self.label7.width(), x))
        self.anim7.setEndValue(QPointF(-self.label7.width(), x))
        self.anim7.start()
        self.time7.start(20000)

    def tongdao8(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label8.setText(text)
        print(self.label8.width())
        # self.label8.setScaledContents(True)
        self.label8.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label8.setPalette(palette)
        self.anim8 = QPropertyAnimation(self.label8, b'pos')
        self.anim8.setDuration(20000)
        self.anim8.setStartValue(QPointF(1150 + self.label8.width(), x))
        self.anim8.setEndValue(QPointF(-self.label8.width(), x))
        self.anim8.start()
        self.time8.start(20000)

    def tongdao9(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label9.setText(text)
        print(self.label9.width())
        # self.label9.setScaledContents(True)
        self.label9.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label9.setPalette(palette)
        self.anim9 = QPropertyAnimation(self.label9, b'pos')
        self.anim9.setDuration(20000)
        self.anim9.setStartValue(QPointF(1150 + self.label9.width(), x))
        self.anim9.setEndValue(QPointF(-self.label9.width(), x))
        self.anim9.start()
        self.time9.start(20000)

    def tongdao10(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label10.setText(text)
        print(self.label10.width())
        # self.label10.setScaledContents(True)
        self.label10.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label10.setPalette(palette)
        self.anim10 = QPropertyAnimation(self.label10, b'pos')
        self.anim10.setDuration(20000)
        self.anim10.setStartValue(QPointF(1150 + self.label10.width(), x))
        self.anim10.setEndValue(QPointF(-self.label10.width(), x))
        self.anim10.start()
        self.time10.start(20000)

    def tongdao11(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label11.setText(text)
        print(self.label11.width())
        # self.label11.setScaledContents(True)
        self.label11.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label11.setPalette(palette)
        self.anim11 = QPropertyAnimation(self.label11, b'pos')
        self.anim11.setDuration(20000)
        self.anim11.setStartValue(QPointF(1150 + self.label11.width(), x))
        self.anim11.setEndValue(QPointF(-self.label11.width(), x))
        self.anim11.start()
        self.time6.start(20000)

    def tongdao12(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label12.setText(text)
        print(self.label12.width())
        # self.label12.setScaledContents(True)
        self.label12.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label12.setPalette(palette)
        self.anim12 = QPropertyAnimation(self.label12, b'pos')
        self.anim12.setDuration(20000)
        self.anim12.setStartValue(QPointF(1150 + self.label12.width(), x))
        self.anim12.setEndValue(QPointF(-self.label12.width(), x))
        self.anim12.start()
        self.time12.start(20000)

    def tongdao13(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label13.setText(text)
        print(self.label13.width())
        # self.label13.setScaledContents(True)
        self.label13.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label13.setPalette(palette)
        self.anim13 = QPropertyAnimation(self.label13, b'pos')
        self.anim13.setDuration(20000)
        self.anim13.setStartValue(QPointF(1150 + self.label13.width(), x))
        self.anim13.setEndValue(QPointF(-self.label13.width(), x))
        self.anim13.start()
        self.time13.start(20000)

    def tongdao14(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label14.setText(text)
        print(self.label14.width())
        # self.label14.setScaledContents(True)
        self.label14.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label14.setPalette(palette)
        self.anim14 = QPropertyAnimation(self.label14, b'pos')
        self.anim14.setDuration(20000)
        self.anim14.setStartValue(QPointF(1150 + self.label14.width(), x))
        self.anim14.setEndValue(QPointF(-self.label14.width(), x))
        self.anim14.start()
        self.time14.start(20000)

    def tongdao15(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label15.setText(text)
        print(self.label15.width())
        # self.label15.setScaledContents(True)
        self.label15.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label15.setPalette(palette)
        self.anim15 = QPropertyAnimation(self.label15, b'pos')
        self.anim15.setDuration(20000)
        self.anim15.setStartValue(QPointF(1150 + self.label15.width(), x))
        self.anim15.setEndValue(QPointF(-self.label15.width(), x))
        self.anim15.start()
        self.time15.start(20000)

    def tongdao16(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label16.setText(text)
        print(self.label16.width())
        # self.label16.setScaledContents(True)
        self.label16.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label16.setPalette(palette)
        self.anim16 = QPropertyAnimation(self.label16, b'pos')
        self.anim16.setDuration(20000)
        self.anim16.setStartValue(QPointF(1150 + self.label16.width(), x))
        self.anim16.setEndValue(QPointF(-self.label16.width(), x))
        self.anim16.start()
        self.time16.start(20000)

    def tongdao17(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label17.setText(text)
        print(self.label17.width())
        # self.label17.setScaledContents(True)
        self.label17.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label17.setPalette(palette)
        self.anim17 = QPropertyAnimation(self.label17, b'pos')
        self.anim17.setDuration(20000)
        self.anim17.setStartValue(QPointF(1150 + self.label17.width(), x))
        self.anim17.setEndValue(QPointF(-self.label17.width(), x))
        self.anim17.start()
        self.time17.start(20000)

    def tongdao18(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label18.setText(text)
        print(self.label18.width())
        # self.label18.setScaledContents(True)
        self.label18.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label18.setPalette(palette)
        self.anim18 = QPropertyAnimation(self.label18, b'pos')
        self.anim18.setDuration(20000)
        self.anim18.setStartValue(QPointF(1150 + self.label18.width(), x))
        self.anim18.setEndValue(QPointF(-self.label18.width(), x))
        self.anim18.start()
        self.time18.start(20000)

    def tongdao19(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label19.setText(text)
        print(self.label19.width())
        # self.label19.setScaledContents(True)
        self.label19.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label19.setPalette(palette)
        self.anim19 = QPropertyAnimation(self.label19, b'pos')
        self.anim19.setDuration(20000)
        self.anim19.setStartValue(QPointF(1150 + self.label19.width(), x))
        self.anim19.setEndValue(QPointF(-self.label19.width(), x))
        self.anim19.start()
        self.time19.start(20000)

    def tongdao20(self, text):
        x = random.uniform(0, 915)
        # label.setGeometry(400, 960, 200, 30)
        self.label20.setText(text)
        print(self.label20.width())
        # self.label20.setScaledContents(True)
        self.label20.setAutoFillBackground(True)
        palette = QPalette()  # 新建一个调色板
        palette.setColor(QPalette.Window, Qt.transparent)  # 　设置颜色
        self.label20.setPalette(palette)
        self.anim20 = QPropertyAnimation(self.label20, b'pos')
        self.anim20.setDuration(20000)
        self.anim20.setStartValue(QPointF(1150 + self.label20.width(), x))
        self.anim20.setEndValue(QPointF(-self.label20.width(), x))
        self.anim20.start()
        self.time20.start(20000)

    def shifang1(self):
        try:
            self.l4.remove(self.tongdao1)
        except:
            pass

    def shifang2(self):
        try:
            self.l4.remove(self.tongdao2)
        except:
            pass

    def shifang3(self):
        try:
            self.l4.remove(self.tongdao3)
        except:
            pass

    def shifang4(self):
        try:
            self.l4.remove(self.tongdao4)
        except:
            pass

    def shifang5(self):
        try:
            self.l4.remove(self.tongdao5)
        except:
            pass

    def shifang6(self):
        try:
            self.l4.remove(self.tongdao6)
        except:
            pass

    def shifang7(self):
        try:
            self.l4.remove(self.tongdao7)
        except:
            pass

    def shifang8(self):
        try:
            self.l4.remove(self.tongdao8)
        except:
            pass

    def shifang9(self):
        try:
            self.l4.remove(self.tongdao9)
        except:
            pass

    def shifang10(self):
        try:
            self.l4.remove(self.tongdao10)
        except:
            pass

    def shifang11(self):
        try:
            self.l4.remove(self.tongdao11)
        except:
            pass

    def shifang12(self):
        try:
            self.l4.remove(self.tongdao12)
        except:
            pass

    def shifang13(self):
        try:
            self.l4.remove(self.tongdao13)
        except:
            pass

    def shifang14(self):
        try:
            self.l4.remove(self.tongdao14)
        except:
            pass

    def shifang15(self):
        try:
            self.l4.remove(self.tongdao15)
        except:
            pass

    def shifang16(self):
        try:
            self.l4.remove(self.tongdao16)
        except:
            pass

    def shifang17(self):
        try:
            self.l4.remove(self.tongdao17)
        except:
            pass

    def shifang18(self):
        try:
            self.l4.remove(self.tongdao18)
        except:
            pass

    def shifang19(self):
        try:
            self.l4.remove(self.tongdao19)
        except:
            pass

    def shifang20(self):
        try:
            self.l4.remove(self.tongdao20)
        except:
            pass

    def zshifang1(self):
        try:
            self.zhubos.remove(self.tongdaoz1)
        except:
            pass

    def zshifang2(self):
        try:
            self.zhubos.remove(self.tongdaoz2)
        except:
            pass

    def shifangh1(self):
        try:
            self.lhs.remove(self.tongdaoh1)
        except:
            pass

    def shifangh2(self):
        try:
            self.lhs.remove(self.tongdaoh2)
        except:
            pass

    def shifangh3(self):
        try:
            self.lhs.remove(self.tongdaoh3)
        except:
            pass

    def shifangh4(self):
        try:
            self.lhs.remove(self.tongdaoh4)
        except:
            pass

    def shifangh5(self):
        try:
            self.lhs.remove(self.tongdaoh5)
        except:
            pass

    def shifangh6(self):
        try:
            self.lhs.remove(self.tongdaoh6)
        except:
            pass

    def shifangc1(self):
        try:
            self.lcs.remove(self.tongdaoc1)
        except:
            pass

    def shifangc2(self):
        try:
            self.lcs.remove(self.tongdaoc2)
        except:
            pass

    def shifangc3(self):
        try:
            self.lcs.remove(self.tongdaoc3)
        except:
            pass

    def shifangc4(self):
        try:
            self.lcs.remove(self.tongdaoc4)
        except:
            pass

    def shifangc5(self):
        try:
            self.lcs.remove(self.tongdaoc5)
        except:
            pass

    def shifangc6(self):
        try:
            self.lcs.remove(self.tongdaoc6)
        except:
            pass

    def huojiang(self, text):
        print(2)
        for x in self.lht:
            if x not in self.lhs:
                self.lhs.append(x)
                x(text)
            # print(x(text))
                break

    def chaohuo(self, text):
        for x in self.lct:
            if x not in self.lcs:
                self.lcs.append(x)
                x(text)
                # print(x(text))
                break

    def tongdaoh1(self, text):
            # text = '789'
        print(1)
        tp(text)
        self.labelh1.setPixmap(QPixmap('img/name2.png'))
        self.labelh2.setPixmap(QPixmap('img/10.png'))
        self.labelh2.setStyleSheet(
            "QLabel{border-image:url(img/name3.png); color:red; }")
        self.labelh2.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh3.setPixmap(QPixmap('img/name1.png'))
        self.labelh3.setGeometry(
            1690 + QPixmap('img/10.png').width(), 40, 190, 36)
        self.anima1 = QPropertyAnimation(self.labelh2, b'pos')
        self.anima1.setDuration(20000)  # 20秒完成移动
        self.anima1.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anima1.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 40))  # 结束位置
        self.anima1.start()  # 弹幕开始移动
        self.animb1 = QPropertyAnimation(self.labelh1, b'pos')
        self.animb1.setDuration(20000)  # 20秒完成移动
        self.animb1.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animb1.setEndValue(
            QPointF(-400 - 210 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animb1.start()  # 弹幕开始移动
        self.animc1 = QPropertyAnimation(self.labelh3, b'pos')
        self.animc1.setDuration(20000)  # 20秒完成移动
        self.animc1.setStartValue(
            QPointF(1480 + 210 + QPixmap('img/10.png').width(), 40))  # 开始位置
        self.animc1.setEndValue(QPointF(-400, 40))  # 结束位置
        self.animc1.start()  # 弹幕开始移动
        self.timeh1.start(20000)

    def tongdaoh2(self, text):
            # text = '789'
        tp(text)
        print("h2")
        self.labelh4.setPixmap(QPixmap('img/name2.png'))
        self.labelh5.setPixmap(QPixmap('img/10.png'))
        self.labelh5.setStyleSheet(
            "QLabel{border-image:url(img/name3.png); color:red; }")
        self.labelh5.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh6.setPixmap(QPixmap('img/name1.png'))
        self.labelh6.setGeometry(
            1690 + QPixmap('img/10.png').width(), 40, 190, 36)
        self.anima2 = QPropertyAnimation(self.labelh5, b'pos')
        self.anima2.setDuration(20000)  # 20秒完成移动
        self.anima2.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anima2.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 40))  # 结束位置
        self.anima2.start()  # 弹幕开始移动
        self.animb2 = QPropertyAnimation(self.labelh4, b'pos')
        self.animb2.setDuration(20000)  # 20秒完成移动
        self.animb2.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animb2.setEndValue(
            QPointF(-400 - 210 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animb2.start()  # 弹幕开始移动
        self.animc2 = QPropertyAnimation(self.labelh6, b'pos')
        self.animc2.setDuration(20000)  # 20秒完成移动
        self.animc2.setStartValue(
            QPointF(1480 + 210 + QPixmap('img/10.png').width(), 40))  # 开始位置
        self.animc2.setEndValue(QPointF(-400, 40))  # 结束位置
        self.animc2.start()  # 弹幕开始移动
        self.timeh2.start(20000)

    def tongdaoh3(self, text):
            # text = '789'
        print("h3")
        tp(text)
        self.labelh7.setPixmap(QPixmap('img/name2.png'))
        self.labelh8.setPixmap(QPixmap('img/10.png'))
        self.labelh8.setStyleSheet(
            "QLabel{border-image:url(img/name3.png); color:red; }")
        self.labelh8.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh9.setPixmap(QPixmap('img/name1.png'))
        self.labelh9.setGeometry(
            1690 + QPixmap('img/10.png').width(), 40, 190, 36)
        self.anima3 = QPropertyAnimation(self.labelh8, b'pos')
        self.anima3.setDuration(20000)  # 20秒完成移动
        self.anima3.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anima3.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 40))  # 结束位置
        self.anima3.start()  # 弹幕开始移动
        self.animb3 = QPropertyAnimation(self.labelh7, b'pos')
        self.animb3.setDuration(20000)  # 20秒完成移动
        self.animb3.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animb3.setEndValue(
            QPointF(-400 - 210 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animb3.start()  # 弹幕开始移动
        self.animc3 = QPropertyAnimation(self.labelh9, b'pos')
        self.animc3.setDuration(20000)  # 20秒完成移动
        self.animc3.setStartValue(
            QPointF(1480 + 210 + QPixmap('img/10.png').width(), 40))  # 开始位置
        self.animc3.setEndValue(QPointF(-400, 40))  # 结束位置
        self.animc3.start()  # 弹幕开始移动
        self.timeh3.start(20000)

    def tongdaoh4(self, text):
            # text = '789'
        print("h4")
        tp(text)
        self.labelh10.setPixmap(QPixmap('img/name2.png'))
        self.labelh11.setPixmap(QPixmap('img/10.png'))
        self.labelh11.setStyleSheet(
            "QLabel{border-image:url(img/name3.png); color:red; }")
        self.labelh11.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh12.setPixmap(QPixmap('img/name1.png'))
        self.labelh12.setGeometry(
            1690 + QPixmap('img/10.png').width(), 40, 190, 36)
        self.anima4 = QPropertyAnimation(self.labelh11, b'pos')
        self.anima4.setDuration(20000)  # 20秒完成移动
        self.anima4.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anima4.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 40))  # 结束位置
        self.anima4.start()  # 弹幕开始移动
        self.animb4 = QPropertyAnimation(self.labelh10, b'pos')
        self.animb4.setDuration(20000)  # 20秒完成移动
        self.animb4.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animb4.setEndValue(
            QPointF(-400 - 210 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animb4.start()  # 弹幕开始移动
        self.animc4 = QPropertyAnimation(self.labelh12, b'pos')
        self.animc4.setDuration(20000)  # 20秒完成移动
        self.animc4.setStartValue(
            QPointF(1480 + 210 + QPixmap('img/10.png').width(), 40))  # 开始位置
        self.animc4.setEndValue(QPointF(-400, 40))  # 结束位置
        self.animc4.start()  # 弹幕开始移动
        self.timeh4.start(20000)

    def tongdaoh5(self, text):
            # text = '789'
        tp(text)
        self.labelh13.setPixmap(QPixmap('img/name2.png'))
        self.labelh14.setPixmap(QPixmap('img/10.png'))
        self.labelh14.setStyleSheet(
            "QLabel{border-image:url(img/name3.png); color:red; }")
        self.labelh14.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh15.setPixmap(QPixmap('img/name1.png'))
        self.labelh15.setGeometry(
            1690 + QPixmap('img/10.png').width(), 40, 190, 36)
        self.anima5 = QPropertyAnimation(self.labelh14, b'pos')
        self.anima5.setDuration(20000)  # 20秒完成移动
        self.anima5.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anima5.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 40))  # 结束位置
        self.anima5.start()  # 弹幕开始移动
        self.animb5 = QPropertyAnimation(self.labelh13, b'pos')
        self.animb5.setDuration(20000)  # 20秒完成移动
        self.animb5.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animb5.setEndValue(
            QPointF(-400 - 210 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animb5.start()  # 弹幕开始移动
        self.animc5 = QPropertyAnimation(self.labelh15, b'pos')
        self.animc5.setDuration(20000)  # 20秒完成移动
        self.animc5.setStartValue(
            QPointF(1480 + 210 + QPixmap('img/10.png').width(), 40))  # 开始位置
        self.animc5.setEndValue(QPointF(-400, 40))  # 结束位置
        self.animc5.start()  # 弹幕开始移动
        self.timeh5.start(20000)

    def tongdaoh6(self, text):
            # text = '789'
        tp(text)
        self.labelh16.setPixmap(QPixmap('img/name2.png'))
        self.labelh17.setPixmap(QPixmap('img/10.png'))
        self.labelh17.setStyleSheet(
            "QLabel{border-image:url(img/name3.png); color:red; }")
        self.labelh17.setGeometry(1690, 40, QPixmap('img/10.png').width(), 36)
        self.labelh18.setPixmap(QPixmap('img/name1.png'))
        self.labelh18.setGeometry(
            1690 + QPixmap('img/10.png').width(), 40, 190, 36)
        self.anima6 = QPropertyAnimation(self.labelh17, b'pos')
        self.anima6.setDuration(20000)  # 20秒完成移动
        self.anima6.setStartValue(QPointF(1480 + 210, 40))  # 开始位置
        self.anima6.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 40))  # 结束位置
        self.anima6.start()  # 弹幕开始移动
        self.animb6 = QPropertyAnimation(self.labelh16, b'pos')
        self.animb6.setDuration(20000)  # 20秒完成移动
        self.animb6.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animb6.setEndValue(
            QPointF(-400 - 210 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animb6.start()  # 弹幕开始移动
        self.animc6 = QPropertyAnimation(self.labelh18, b'pos')
        self.animc6.setDuration(20000)  # 20秒完成移动
        self.animc6.setStartValue(
            QPointF(1480 + 210 + QPixmap('img/10.png').width(), 40))  # 开始位置
        self.animc6.setEndValue(QPointF(-400, 40))  # 结束位置
        self.animc6.start()  # 弹幕开始移动
        self.timeh6.start(20000)

    def tongdaoc1(self, text):
        tp1(text)
        self.labelc1.setPixmap(QPixmap('img/name.png'))
        self.labelc2.setPixmap(QPixmap('img/10.png'))
        self.labelc2.setStyleSheet(
            "QLabel{border-image:url(img/name4.png)}")
        self.labelc2.setGeometry(
            1636, 42, QPixmap('img/10.png').width(), 36)
        self.labelc3.setPixmap(QPixmap('img/name5.png'))
        self.labelc3.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)
        self.animx1 = QPropertyAnimation(self.labelc2, b'pos')
        self.animx1.setDuration(20000)  # 20秒完成移动
        self.animx1.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.animx1.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 42))  # 结束位置
        self.animx1.start()  # 弹幕开始移动
        self.animy1 = QPropertyAnimation(self.labelc1, b'pos')
        self.animy1.setDuration(20000)  # 20秒完成移动
        self.animy1.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animy1.setEndValue(
            QPointF(-400 - 156 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animy1.start()  # 弹幕开始移动
        self.animz1 = QPropertyAnimation(self.labelc3, b'pos')
        self.animz1.setDuration(20000)  # 20秒完成移动
        self.animz1.setStartValue(
            QPointF(1480 + 156 + QPixmap('img/10.png').width(), 42))  # 开始位置
        self.animz1.setEndValue(QPointF(-400, 42))  # 结束位置
        self.animz1.start()  # 弹幕开始移动
        self.timec1.start(20000)

    def tongdaoc2(self, text):
        tp1(text)
        self.labelc4.setPixmap(QPixmap('img/name.png'))
        self.labelc5.setPixmap(QPixmap('img/10.png'))
        self.labelc5.setStyleSheet(
            "QLabel{border-image:url(img/name4.png)}")
        self.labelc5.setGeometry(
            1636, 42, QPixmap('img/10.png').width(), 36)
        self.labelc6.setPixmap(QPixmap('img/name5.png'))
        self.labelc6.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)
        self.animx2 = QPropertyAnimation(self.labelc5, b'pos')
        self.animx2.setDuration(20000)  # 20秒完成移动
        self.animx2.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.animx2.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 42))  # 结束位置
        self.animx2.start()  # 弹幕开始移动
        self.animy2 = QPropertyAnimation(self.labelc4, b'pos')
        self.animy2.setDuration(20000)  # 20秒完成移动
        self.animy2.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animy2.setEndValue(
            QPointF(-400 - 156 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animy2.start()  # 弹幕开始移动
        self.animz2 = QPropertyAnimation(self.labelc6, b'pos')
        self.animz2.setDuration(20000)  # 20秒完成移动
        self.animz2.setStartValue(
            QPointF(1480 + 156 + QPixmap('img/10.png').width(), 42))  # 开始位置
        self.animz2.setEndValue(QPointF(-400, 42))  # 结束位置
        self.animz2.start()  # 弹幕开始移动
        self.timec2.start(20000)

    def tongdaoc3(self, text):
        tp1(text)
        self.labelc7.setPixmap(QPixmap('img/name.png'))
        self.labelc8.setPixmap(QPixmap('img/10.png'))
        self.labelc8.setStyleSheet(
            "QLabel{border-image:url(img/name4.png)}")
        self.labelc8.setGeometry(
            1636, 42, QPixmap('img/10.png').width(), 36)
        self.labelc9.setPixmap(QPixmap('img/name5.png'))
        self.labelc9.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)
        self.animx3 = QPropertyAnimation(self.labelc8, b'pos')
        self.animx3.setDuration(20000)  # 20秒完成移动
        self.animx3.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.animx3.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 42))  # 结束位置
        self.animx3.start()  # 弹幕开始移动
        self.animy3 = QPropertyAnimation(self.labelc7, b'pos')
        self.animy3.setDuration(20000)  # 20秒完成移动
        self.animy3.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animy3.setEndValue(
            QPointF(-400 - 156 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animy3.start()  # 弹幕开始移动
        self.animz3 = QPropertyAnimation(self.labelc9, b'pos')
        self.animz3.setDuration(20000)  # 20秒完成移动
        self.animz3.setStartValue(
            QPointF(1480 + 156 + QPixmap('img/10.png').width(), 42))  # 开始位置
        self.animz3.setEndValue(QPointF(-400, 42))  # 结束位置
        self.animz3.start()  # 弹幕开始移动
        self.timec3.start(20000)

    def tongdaoc4(self, text):
        tp1(text)
        self.labelc10.setPixmap(QPixmap('img/name.png'))
        self.labelc11.setPixmap(QPixmap('img/10.png'))
        self.labelc11.setStyleSheet(
            "QLabel{border-image:url(img/name4.png)}")
        self.labelc11.setGeometry(
            1636, 42, QPixmap('img/10.png').width(), 36)
        self.labelc12.setPixmap(QPixmap('img/name5.png'))
        self.labelc12.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)
        self.animx4 = QPropertyAnimation(self.labelc11, b'pos')
        self.animx4.setDuration(20000)  # 20秒完成移动
        self.animx4.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.animx4.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 42))  # 结束位置
        self.animx4.start()  # 弹幕开始移动
        self.animy4 = QPropertyAnimation(self.labelc10, b'pos')
        self.animy4.setDuration(20000)  # 20秒完成移动
        self.animy4.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animy4.setEndValue(
            QPointF(-400 - 156 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animy4.start()  # 弹幕开始移动
        self.animz4 = QPropertyAnimation(self.labelc12, b'pos')
        self.animz4.setDuration(20000)  # 20秒完成移动
        self.animz4.setStartValue(
            QPointF(1480 + 156 + QPixmap('img/10.png').width(), 42))  # 开始位置
        self.animz4.setEndValue(QPointF(-400, 42))  # 结束位置
        self.animz4.start()  # 弹幕开始移动
        self.timec4.start(20000)

    def tongdaoc5(self, text):
        tp1(text)
        self.labelc13.setPixmap(QPixmap('img/name.png'))
        self.labelc14.setPixmap(QPixmap('img/10.png'))
        self.labelc14.setStyleSheet(
            "QLabel{border-image:url(img/name4.png)}")
        self.labelc14.setGeometry(
            1636, 42, QPixmap('img/10.png').width(), 36)
        self.labelc15.setPixmap(QPixmap('img/name5.png'))
        self.labelc15.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)
        self.animx5 = QPropertyAnimation(self.labelc14, b'pos')
        self.animx5.setDuration(20000)  # 20秒完成移动
        self.animx5.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.animx5.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 42))  # 结束位置
        self.animx5.start()  # 弹幕开始移动
        self.animy5 = QPropertyAnimation(self.labelc13, b'pos')
        self.animy5.setDuration(20000)  # 20秒完成移动
        self.animy5.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animy5.setEndValue(
            QPointF(-400 - 156 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animy5.start()  # 弹幕开始移动
        self.animz5 = QPropertyAnimation(self.labelc15, b'pos')
        self.animz5.setDuration(20000)  # 20秒完成移动
        self.animz5.setStartValue(
            QPointF(1480 + 156 + QPixmap('img/10.png').width(), 42))  # 开始位置
        self.animz5.setEndValue(QPointF(-400, 42))  # 结束位置
        self.animz5.start()  # 弹幕开始移动
        self.timec5.start(20000)

    def tongdaoc6(self, text):
        tp1(text)
        self.labelc16.setPixmap(QPixmap('img/name.png'))
        self.labelc17.setPixmap(QPixmap('img/10.png'))
        self.labelc17.setStyleSheet(
            "QLabel{border-image:url(img/name4.png)}")
        self.labelc17.setGeometry(
            1636, 42, QPixmap('img/10.png').width(), 36)
        self.labelc18.setPixmap(QPixmap('img/name5.png'))
        self.labelc18.setGeometry(
            1636 + QPixmap('img/10.png').width(), 42, 166, 36)
        self.animx6 = QPropertyAnimation(self.labelc17, b'pos')
        self.animx6.setDuration(20000)  # 20秒完成移动
        self.animx6.setStartValue(QPointF(1480 + 156, 42))  # 开始位置
        self.animx6.setEndValue(
            QPointF(-400 - QPixmap('img/10.png').width(), 42))  # 结束位置
        self.animx6.start()  # 弹幕开始移动
        self.animy6 = QPropertyAnimation(self.labelc16, b'pos')
        self.animy6.setDuration(20000)  # 20秒完成移动
        self.animy6.setStartValue(QPointF(1480, 0))  # 开始位置
        self.animy6.setEndValue(
            QPointF(-400 - 156 - QPixmap('img/10.png').width(), 0))  # 结束位置
        self.animy6.start()  # 弹幕开始移动
        self.animz6 = QPropertyAnimation(self.labelc18, b'pos')
        self.animz6.setDuration(20000)  # 20秒完成移动
        self.animz6.setStartValue(
            QPointF(1480 + 156 + QPixmap('img/10.png').width(), 42))  # 开始位置
        self.animz6.setEndValue(QPointF(-400, 42))  # 结束位置
        self.animz6.start()  # 弹幕开始移动
        self.timec6.start(20000)


def cli_show(a):
    global ni
    ni = a
