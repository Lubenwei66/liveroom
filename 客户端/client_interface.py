#-*- coding:utf-8 -*-
from __future__ import unicode_literals
# from C import desk
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
from threading import Thread
from socket import *


class MyBtn(QPushButton):

    def enterEvent(self, event):
        self.setStyleSheet("MyBtn{background-color:argb(0,0,0,0);}")
        # self.gif = QMovie('img/bg.gif')
        # self.setMovie(self.gif)
        # ex.gif.start()
        ex.ceshi.setGeometry(300, 545, 400, 400)

    def leaveEvent(self, event):
        self.setStyleSheet(
            "QPushButton{background-image:url(img/123.png);border:1px solid red;border-radius:5px;}")
        # ex.ceshi.setStyleSheet(
        #     "QLabel{background-color:argb(0,0,0,0);}")
        # ex.gif.stop()
        ex.ceshi.setGeometry(300, 545, 0, 0)


class client_interface(QWidget):

    def __init__(self):
        super().__init__()
        self.data1 = "".encode("utf-8")
        self.data2 = ''.encode('utf-8')
        # HOST = '176.215.201.145'
        # HOST = '127.0.0.1'
        # PORT1 = 8888
        # PORT2 = 8887
        # ADDR1 = (HOST, PORT1)
        # ADDR2 = (HOST, PORT2)
        # self.s = socket(AF_INET, SOCK_STREAM)
        # self.c = socket(AF_INET, SOCK_STREAM)
        # self.s.connect(ADDR1)
        # self.c.connect(ADDR2)
        self.pictureLabel = QLabel(self)
        self.pictureLabel.setGeometry(10, 10, 1480, 930)
        self.pictureLabel.setStyleSheet(
            "QLabel{border:5px solid black;border-radius:10%;}")
        self.pictureLabel.setScaledContents(True)
        init_image = QPixmap("tongbu.png").scaled(self.width(), self.height())
        self.pictureLabel.setPixmap(init_image)

        self.pictureLabel_tou = QLabel(self)
        self.pictureLabel_tou.setScaledContents(True)
        self.pictureLabel_tou.setGeometry(990, 740, 300, 195)
        init_image = QPixmap("tongbu.png").scaled(self.width(), self.height())
        self.pictureLabel_tou.setPixmap(init_image)

        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.setGeometry(1260, 970, 80, 20)
        # self.sld.valueChanged[int].connect(self.changeValue)

        self.sld_label = QLabel(self)
        self.sld_label.setPixmap(QPixmap('img/mute.png'))
        self.sld_label.setGeometry(1350, 970, 80, 20)

        # setGeometry(300, 300, 280, 170)

        money = 100
        self.label_money = QLabel("金币:", self)
        # self.label_money.setStyleSheet("QLabel{border-color:rgb(255,0,0)}")
        self.label_money.setStyleSheet("color:red")
        self.label_money.setGeometry(20, 970, 80, 20)
        self.label_money_sql = QLabel("%d" % money, self)
        self.label_money_sql.setGeometry(80, 970, 80, 20)

        self.rechargeButton = QPushButton(self)
        self.rechargeButton.setText("充值")
        self.rechargeButton.setIcon(QIcon("img/进.png"))
        self.rechargeButton.setGeometry(160, 960, 80, 30)

        BTN_style = "QPushButton{background-image:url(img/123.png);border:1px solid red;border-radius:5px;}QPushButton:hover{background-image:url(img/mute.png);}"

        # self.gif.start()
        self.Button_liwu1 = MyBtn(self)
        self.Button_liwu1.setToolTip("点击送主播大飞机")
        # self.Button_liwu1.setStyleSheet(BTN_style)
        self.Button_liwu1.setGeometry(250, 945, 50, 50)

        self.Button_liwu2 = QPushButton(self)
        self.Button_liwu2.setToolTip("点击送主播大飞机")
        self.Button_liwu2.setStyleSheet(BTN_style)
        self.Button_liwu2.setGeometry(310, 945, 50, 50)

        self.Button_liwu3 = QPushButton(self)
        self.Button_liwu3.setToolTip("点击送主播大飞机")
        self.Button_liwu3.setStyleSheet(BTN_style)
        self.Button_liwu3.setGeometry(370, 945, 50, 50)

        self.Button_liwu4 = QPushButton(self)
        self.Button_liwu4.setToolTip("点击送主播大飞机")
        self.Button_liwu4.setStyleSheet(BTN_style)
        self.Button_liwu4.setGeometry(430, 945, 50, 50)

        self.Button_liwu5 = QPushButton(self)
        self.Button_liwu5.setToolTip("点击送主播大飞机")
        self.Button_liwu5.setStyleSheet(BTN_style)
        self.Button_liwu5.setGeometry(490, 945, 50, 50)

        self.Button_liwu6 = QPushButton(self)
        self.Button_liwu6.setToolTip("点击送主播大飞机")
        self.Button_liwu6.setStyleSheet(BTN_style)
        self.Button_liwu6.setGeometry(550, 945, 50, 50)

        self.Button_liwu7 = QPushButton(self)
        self.Button_liwu7.setToolTip("点击送主播大飞机")
        self.Button_liwu7.setStyleSheet(BTN_style)
        self.Button_liwu7.setGeometry(610, 945, 50, 50)

        self.browser = QTextBrowser(self)
        self.browser.setStyleSheet(
            "QTextBrowser{border:5px solid black;border-radius:10%;}")
        self.browser.setGeometry(1495, 10, 400, 900)

        self.Button_liwu1.clicked.connect(self.liwu)
        self.Button_liwu2.clicked.connect(self.liwu)
        self.Button_liwu3.clicked.connect(self.liwu)
        self.Button_liwu4.clicked.connect(self.liwu)
        self.Button_liwu5.clicked.connect(self.liwu)
        self.Button_liwu6.clicked.connect(self.liwu)
        self.Button_liwu7.clicked.connect(self.liwu)

        # 发送文字的文本框
        self.send_edit = QTextEdit(self)
        self.send_edit.setGeometry(1495, 910, 320, 80)
        self.send_edit.setStyleSheet(
            "QTextEdit{border:5px solid black;border-radius:10%;}")

        # 发送消息按钮
        self.sendButton = QPushButton(self)
        self.sendButton.setText("发送")
        self.sendButton.setIcon(QIcon("img/进.png"))
        self.sendButton.setGeometry(1815, 910, 80, 80)
        self.setGeometry(0, 0, 1905, 1000)

        self.setWindowTitle("直播界面")
        # self.timer = VideoTimer()
        # self.timer.start()
        # self.playCapture = VideoCapture()
        # self.set_timer_fps()
        # self.timer.timeSignal.signal[str].connect(self.show_video_images)
        # self.timer.timeSignal.signal[str].connect(self.show_video_images_tou)
        self.liwu_gif()

    def liwu_gif(self):
        self.ceshi = QLabel(self)
        # self.ceshi.setStyleSheet("QLabel{background-color:red;}")
        self.ceshi.setGeometry(300, 545, 0, 0)
        self.ceshi.setStyleSheet(
            "QLabel{border:1px solid red;border-radius:5px;background-color:argb(0,0,0,0);}")
        self.gif = QMovie('img/bg.gif')
        self.ceshi.setMovie(self.gif)
        self.gif.start()

    def liwu(self):
        QMessageBox.question(self, 'Message', "Are you sure to quit?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

#     def closeEvent(self, event):

#         reply = QMessageBox.question(self, 'Message',
#                                      "Are you sure to quit?", QMessageBox.Yes |
#                                      QMessageBox.No, QMessageBox.No)

#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()

    def changeValue(self, value):

        if value == 0:
            self.sld_label.setPixmap(QPixmap('img/mute.png'))
        elif value > 0 and value <= 30:
            self.sld_label.setPixmap(QPixmap('img/min.png'))
        elif value > 30 and value < 80:
            self.sld_label.setPixmap(QPixmap('img/med.png'))
        else:
            self.sld_label.setPixmap(QPixmap('img/max.png'))

#     def set_timer_fps(self):
#         fps = 4
#         self.timer.set_fps(fps)
#         self.playCapture.release()

#     def show_video_images(self):
#         payload_size = struct.calcsize("L")
#         self.data1 += self.s.recv(80000)
#         p = self.data1.find(b'V')
#         if p >= 0:
#             packed_size = self.data1[p + 1:p + payload_size + 1]
#             msg_size = struct.unpack("L", packed_size)[0]
#             msg = self.data1[p + payload_size + 1:]
#             if len(msg) < msg_size:
#                 while len(msg) < msg_size:
#                     msg += self.s.recv(80000)
#                 zframe_data = msg[:msg_size]
#                 self.data1 = msg[msg_size:]
#                 frame_data = zlib.decompress(zframe_data)
#                 frame = pickle.loads(frame_data)
#             else:
#                 zframe_data = msg[:msg_size]
#                 self.data1 = msg[msg_size:]
#                 frame_data = zlib.decompress(zframe_data)
#                 frame = pickle.loads(frame_data)
#             height, width = frame.shape[:2]
#             if frame.ndim == 3:
#                 rgb = cvtColor(frame, COLOR_BGR2RGB)
#             elif frame.ndim == 2:
#                 rgb = cvtColor(frame, COLOR_GRAY2BGR)

#             temp_image = QImage(rgb.flatten(), width,
#                                 height, QImage.Format_RGB888)
#             temp_pixmap = QPixmap.fromImage(temp_image)
#         # if x > 0:
#             img = temp_pixmap
#             if img:
#                 self.pictureLabel.setPixmap(img)

#     def show_video_images_tou(self):
#         payload_size = struct.calcsize("L")
#         self.data2 += self.c.recv(80000)
#         p = self.data2.find(b'D')
#         if p >= 0:
#             packed_size = self.data2[p + 1:p + payload_size + 1]
#             msg_size = struct.unpack("L", packed_size)[0]
#             msg = self.data2[p + payload_size + 1:]
#             if len(msg) < msg_size:
#                 while len(msg) < msg_size:
#                     msg += self.c.recv(80000)
#                 zframe_data = msg[:msg_size]
#                 self.data2 = msg[msg_size:]
#                 frame_data = zlib.decompress(zframe_data)
#                 frame = pickle.loads(frame_data)
#             else:
#                 zframe_data = msg[:msg_size]
#                 self.data2 = msg[msg_size:]
#                 frame_data = zlib.decompress(zframe_data)
#                 frame = pickle.loads(frame_data)
#             height, width = frame.shape[:2]
#             if frame.ndim == 3:
#                 rgb = cvtColor(frame, COLOR_BGR2RGB)
#             elif frame.ndim == 2:
#                 rgb = cvtColor(frame, COLOR_GRAY2BGR)

#             temp_image = QImage(rgb.flatten(), width,
#                                 height, QImage.Format_RGB888)
#             temp_pixmap = QPixmap.fromImage(temp_image)
#             img = temp_pixmap
#             if img:
#                 self.pictureLabel_tou.setPixmap(img)


# class Communicate(QObject):

#     signal = pyqtSignal(str)


# class VideoTimer(QThread):

#     def __init__(self, frequent=5):
#         QThread.__init__(self)
#         self.stopped = False
#         self.frequent = frequent
#         self.timeSignal = Communicate()
#         self.mutex = QMutex()

#     def run(self):
#         with QMutexLocker(self.mutex):
#             self.stopped = False
#         while True:
#             # if self.stopped:
#             #     return
#             self.timeSignal.signal.emit("1")
#             time.sleep(1 / self.frequent)

#     def set_fps(self, fps):
#         self.frequent = fps

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = client_interface()
    # ex.setFixedSize(ex.width(), ex.height())
    ex.show()
    sys.exit(app.exec_())
