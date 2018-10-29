#-*- coding:utf-8 -*-
from __future__ import unicode_literals
from registration_interface import registration_interface
from client1 import *
from chat_client import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
# from reset import *
import sys
from multiprocessing import Process
from socket import *
import threading
from cv2 import *
from forget_interface import *


class login_interface(QMainWindow):

    STATUS_INIT = 0
    STATUS_PAUSE = 1
    signal_replay = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.video_url = "img/home.mp4"
        self.status = self.STATUS_INIT

        self.pictureLabel = QLabel('', self)
        init_image = QPixmap(
            "img/办卡.png").scaled(self.width(), self.height())
        self.pictureLabel.setPixmap(init_image)
        self.pictureLabel.setGeometry(0, 0, 320, 400)
        self.pictureLabel.setScaledContents(True)
        # self.gif = QMovie('img/p1.gif')
        # self.pictureLabel.setMovie(self.gif)
        # self.gif.start()

        self.registeredButton = QPushButton(self)
        self.registeredButton.setText("注册")
        self.registeredButton.setStyleSheet("QPushButton{color:black}"
                                            "QPushButton:hover{color:red}"
                                            "QPushButton{background-color:#00FFFF}"
                                            "QPushButton{border:2px}"
                                            "QPushButton{border-radius:10px}"
                                            "QPushButton{padding:2px 4px}")
        self.registeredButton.move(50, 300)

        self.loadingButton = QPushButton(self)
        self.loadingButton.setText("登录")
        # self.loadingButton.setIcon(QIcon("img/进.png"))
        self.loadingButton.setStyleSheet("QPushButton{color:black}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#00FFFF}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:10px}"
                                         "QPushButton{padding:2px 4px}")
        self.loadingButton.move(160, 300)

        self.forgetButton = QPushButton(self)
        self.forgetButton.setText("忘记密码")
        # self.forgetButton.setIcon(QIcon("img/进.png"))
        self.forgetButton.setStyleSheet("QPushButton{color:#00FFFF}"
                                        "QPushButton:hover{color:blue}"
                                        "QPushButton{background-color:rgba(255,255,255,0%)}"
                                        "QPushButton{border:2px}"
                                        "QPushButton{border-radius:10px}"
                                        "QPushButton{padding:2px 4px}")
        self.forgetButton.move(200, 350)
        self.forgetButton.clicked.connect(self.forget)

        # self.forgetButton = QPushButton(self)
        # self.forgetButton.setText("忘记密码")
        # self.forgetButton.move(320, 300)

        self.label_id = QLabel("账号", self)
        self.label_id.setGeometry(40, 69, 100, 100)
        self.label_id.setFont(QFont("Microsoft YaHei", 12))
        self.label_id.setStyleSheet("QLabel{color: #00FF99}")

        self.label_pwd = QLabel("密码", self)
        self.label_pwd.setGeometry(40, 120, 100, 100)
        self.label_pwd.setFont(QFont("Microsoft YaHei", 12))
        self.label_pwd.setStyleSheet("QLabel{color: #00FF99}")

        self.id_edit = QLineEdit(self)
        self.id_edit.move(95, 105)
        self.id_edit.setFixedWidth(170)
        self.id_edit.setStyleSheet("QLineEdit{color:#CC6633}"
                                   "QLineEdit:hover{color:#00BFFF}"
                                   "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                   "QLineEdit{padding:2px 4px}")

        self.pass_edit = QLineEdit(self)
        self.pass_edit.move(95, 155)
        # self.pass_edit.setFrame(False)
        self.pass_edit.setFixedWidth(170)
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.pass_edit.setStyleSheet("QLineEdit{color:#CC6633}"
                                     "QLineEdit:hover{color:#00BFFF}"
                                     "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                     "QLineEdit{padding:2px 4px}")

        self.resize(320, 400)
        self.center()
        self.setWindowTitle("登录界面")

        self.HOST = '176.215.99.164'
        self.PORT = 8888
        self.ADDR = (self.HOST, self.PORT)
        self.s = socket(AF_INET, SOCK_DGRAM)

        QApplication.setStyle("Fusion")

        self._CloseButton = QPushButton(b'\xef\x81\xb2'.decode("utf-8"), self)
        self._CloseButton.move(280, 0)
        self._CloseButton.setFont(QFont("Webdings"))  # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self._CloseButton.setFixedWidth(40)
        # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        self._CloseButton.setObjectName("CloseButton")
        self._CloseButton.setToolTip("关闭窗口")
        self._CloseButton.setStyleSheet("QPushButton{color:#CC6633}"
                                        "QPushButton:hover{color:#99FFCC}"
                                        "QPushButton{background-color:#262626}"
                                        "QPushButton{padding:2px 4px}")
        # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        self._CloseButton.setMouseTracking(True)
        self._CloseButton.clicked.connect(self.close)

        self._MinimumButton = QPushButton(
            b'\xef\x80\xb0'.decode("utf-8"), self)
        self._MinimumButton.move(242, 0)
        # 特殊字体以不借助图片实现最小化最大化和关闭按钮
        self._MinimumButton.setFont(QFont("Webdings"))
        self._MinimumButton.setFixedWidth(40)
        # 设置按钮的ObjectName以在qss样式表内定义不同的按钮样式
        self._MinimumButton.setObjectName("CloseButton")
        self._MinimumButton.setToolTip("最小化窗口")
        self._MinimumButton.setStyleSheet("QPushButton{color:#CC6633}"
                                          "QPushButton:hover{color:#99FFCC}"
                                          "QPushButton{background-color:#262626}"
                                          "QPushButton{padding:2px 4px}")
        # 设置按钮鼠标跟踪（如不设，则按钮在widget上层，无法实现跟踪）
        self._MinimumButton.setMouseTracking(True)
        self._MinimumButton.clicked.connect(self.showMinimized)

        self.timer = VideoTimer()
        self.timer.timeSignal.signal[str].connect(self.show_video_images)

        self.registeredButton.clicked.connect(self.zhuce)
        self.loadingButton.clicked.connect(self.loadingButton_check)

        # video 初始设置
        self.playCapture = VideoCapture()
        if self.video_url != "":
            self.playCapture.open(self.video_url)
            fps = self.playCapture.get(CAP_PROP_FPS)
            self.timer.set_fps(fps)
            self.playCapture.release()
            self.switch_video()

        self.signal_replay.connect(self.switch_video)

    def zhuce(self):
        b.show()
        self.hide()
        b.ex = ex

    def forget(self):
        fo.show()
        self.hide()
        fo.ex = ex

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def loadingButton_check(self):
        l_id = ex.id_edit.text()
        p_pass = ex.pass_edit.text()
        img_p = login(ex.s, ex.ADDR, l_id, p_pass)
        if img_p == '密码错误':
            replay = QMessageBox.warning(self, "!", "密码输入错误", QMessageBox.Yes)
        elif img_p == '用户名不存在':
            replay = QMessageBox.warning(self, "!", "用户名不存在", QMessageBox.Yes)
        elif img_p == '用户名已存在':
            replay = QMessageBox.warning(self, "!", "用户名已存在", QMessageBox.Yes)
        else:
            ni.uname = l_id
            ni.nicheng = img_p[0]
            ni('176.215.99.164', img_p[1], self.ADDR)
            ni.show()
            self.close()

    def show_video_images(self):
        if self.playCapture.isOpened():
            success, frame = self.playCapture.read()
            if success:
                height, width = frame.shape[:2]
                if frame.ndim == 3:
                    rgb = cvtColor(frame, COLOR_BGR2RGB)
                elif frame.ndim == 2:
                    rgb = cvtColor(frame, COLOR_GRAY2BGR)

                temp_image = QImage(rgb.flatten(), width,
                                    height, QImage.Format_RGB888)
                temp_pixmap = QPixmap.fromImage(temp_image)
                self.pictureLabel.setPixmap(temp_pixmap)
            else:
                success, frame = self.playCapture.read()
                if not success:
                    self.reset()  # 判断本地文件播放完毕
                return

    def switch_video(self):
        if self.status is login_interface.STATUS_INIT:
            self.playCapture.open(self.video_url)
            self.timer.start()
        else:
            self.playCapture.release()
            self.playCapture.open(self.video_url)
            self.timer.start()

    def reset(self):
        # self.timer.stop()
        self.playCapture.release()
        self.status = login_interface.STATUS_PAUSE
        self.signal_replay.emit("replay")


class Communicate(QObject):

    signal = pyqtSignal(str)


class VideoTimer(QThread):

    def __init__(self, frequent=20):
        QThread.__init__(self)
        self.frequent = frequent
        self.timeSignal = Communicate()

    def run(self):
        while True:
            self.timeSignal.signal.emit("1")
            time.sleep(1 / self.frequent)

    def set_fps(self, fps):
        self.frequent = fps


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fo = forget_interface()
    ex = login_interface()
    ex.setFixedSize(ex.width(), ex.height())
    b = registration_interface()
    b.setFixedSize(b.width(), b.height())
    ni = client_interface()
    cli_show(ni)
    ni.sendButton.clicked.connect(ni.send_msg)
    ex.show()
    sys.exit(app.exec_())
