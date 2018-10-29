# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from socket import *
from multiprocessing import Process
from threading import Thread
from denglu import do_parent
from video_server import video_s
from Audio_server import audio_s
from desk_server import desk_s
from chat_server import chat_s
from cv2 import *
import pickle
import sys
import os
import time

# self.signal_browser.emit(msg)


class zhubo_interface(QWidget):
    signal_browser = pyqtSignal(str)
    signal_tou = pyqtSignal(bytes)

    def __init__(self):
        super().__init__()
        self.starButton = QPushButton(self)
        self.starButton.setGeometry(0, 0, 400, 50)
        self.starButton.setToolTip("开始直播")
        self.starButton.setIcon(QIcon("img/进.png"))
        self.starButton.setText("开始直播")
        self.starButton.clicked.connect(self.start)

        self.endButton = QPushButton(self)
        self.endButton.setGeometry(400, 0, 400, 50)
        self.endButton.setToolTip("结束直播")
        self.endButton.setIcon(QIcon("img/进.png"))
        self.endButton.setText("结束直播")
        self.endButton.clicked.connect(self.quit)

        # 摄像头控件
        self.labelcam = QLabel(self)
        self.labelcam = QLabel(self)
        self.labelcam.setScaledContents(True)
        self.labelcam.setGeometry(10, 60, 485, 530)
        init_image = QPixmap("tongbu.png").scaled(self.width(), self.height())
        self.labelcam.setPixmap(init_image)
        self.cap = cv2.VideoCapture(0)
        self.signal_tou.connect(self.video_images_tou)

        # 接收信息文本
        self.browser = QTextBrowser(self)
        self.browser.setGeometry(500, 60, 290, 510)
        # 发送文字的文本框
        self.send_edit = QTextEdit(self)
        self.send_edit.setGeometry(500, 530, 210, 60)

        # 发送消息按钮
        self.sendButton = QPushButton(self)
        self.sendButton.setText("喊话")
        self.sendButton.clicked.connect(self.send_msg)
        self.sendButton.setGeometry(720, 530, 70, 60)
        self.sendButton.setIcon(QIcon("img/进.png"))

        # 发送按钮连接
        self.sendButton.clicked.connect(self.send_msg)

        # 写入聊天按钮
        self.signal_browser.connect(self.write_msg)

        self.resize(800, 600)
        self.center()
        self.setWindowTitle("直播界面")

        self.user = {}

        self.host = '0.0.0.0'
        self.ADDR1 = (self.host, 8888)  # 登录
        self.ADDR2 = (self.host, 7777)  # 视频
        self.ADDR3 = (self.host, 7779)  # 音频
        self.ADDR4 = (self.host, 7781)  # 桌面
        self.ADDR5 = (self.host, 7776)  # 聊天
        self.ADDR6 = (self.host, 7788)  # 服务器内部连接
        self.pa = socket(AF_INET, SOCK_DGRAM)  # 登录
        self.vi = socket(AF_INET, SOCK_STREAM)  # 视频
        self.au = socket(AF_INET, SOCK_STREAM)  # 音频
        self.de = socket(AF_INET, SOCK_STREAM)  # 桌面
        self.ch = socket(AF_INET, SOCK_DGRAM)  # 聊天
        self.lj = socket(AF_INET, SOCK_DGRAM)  # 连接
        self.pa.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.de.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.au.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.vi.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.ch.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.lj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.pa.bind(self.ADDR1)
        self.vi.bind(self.ADDR2)
        self.au.bind(self.ADDR3)
        self.de.bind(self.ADDR4)
        self.ch.bind(self.ADDR5)
        self.lj.bind(self.ADDR6)
        self.au.listen(10)
        self.de.listen(10)
        self.vi.listen(10)

    def start(self):
        print('开启')
        z = Thread(target=do_parent, args=(self.pa, self.user,))
        x = Process(target=video_s, args=(self.vi,))
        y = Process(target=audio_s, args=(self.au,))
        t = Process(target=desk_s, args=(self.de,))
        p = Thread(target=chat_s, args=(self.ch, self.user,))
        o = Thread(target=self.rcv_msg)
        q = Thread(target=self.show_video)
        z.setDaemon(True)
        x.Daemon = True
        y.Daemon = True
        t.Daemon = True
        p.setDaemon(True)
        o.setDaemon(True)
        q.Daemon = True
        z.start()
        x.start()
        y.start()
        t.start()
        p.start()
        o.start()
        q.start()

    def show_video(self):
        while True:
            ret, frame = self.cap.read()
            frame = pickle.dumps(frame)
            self.signal_tou[bytes].emit(frame)

    def video_images_tou(self, frame):
        frame = pickle.loads(frame)
        height, width = frame.shape[:2]
        if frame.ndim == 3:
            rgb = cvtColor(frame, COLOR_BGR2RGB)
        elif frame.ndim == 2:
            rgb = cvtColor(frame, COLOR_GRAY2BGR)

        temp_image = QImage(rgb.flatten(), width,
                            height, QImage.Format_RGB888)
        temp_pixmap = QPixmap.fromImage(temp_image)
        img = temp_pixmap
        self.labelcam.setPixmap(img)

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

    def send_msg(self):
        user = self.user
        msg = self.send_edit.toPlainText()
        if msg:
            self.send_edit.clear()
            Msg = '# {} : {}'.format('主播', msg)
            for i in user:
                if i != 'me':
                    self.ch.sendto(Msg.encode(), (user[i][0], user[i][1] + 1))

    def rcv_msg(self):
        while True:
            msg, addr = self.lj.recvfrom(1024)
            msgList = msg.decode().replace("\n", "")
            msgList = msgList.split(' ')
            if msgList[0] == 'HI':
                self.user[msgList[1]] = addr
            elif msgList[0] == '+'or msgList[0] == '#'or msgList[0] == 'G':
                msg = '\n' + ''.join(msgList[1:])
                self.signal_browser.emit(msg)  # 文本框写入
            elif msgList[0] == 'A':
                self.user[msgList[1]] = addr

    def quit(self):
        tishi = QMessageBox.question(self, 'Message', "是否关闭直播并退出",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if tishi == QMessageBox.Yes:
            self.pa.close()
            self.vi.close()
            self.au.close()
            self.de.close()
            self.ch.close()
            os.popen("taskkill /im python.exe -f")
            sys.exit(0)

    def btn(self):
        QMessageBox.question(self, 'Message', "Are you sure to quit?",
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = zhubo_interface()
    ex.setFixedSize(ex.width(), ex.height())
    ex.show()
    sys.exit(app.exec_())
