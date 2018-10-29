#-*- coding:utf-8 -*-
from __future__ import unicode_literals


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import *
from chat_client import *
import sys
# from yzm import *
from chat_client import *


class forget_interface(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.pictureLabel = QLabel('', self)
        self.pictureLabel.setGeometry(0, 0, 600, 600)
        self.gif = QMovie('img/p12.gif')
        self.pictureLabel.setMovie(self.gif)
        self.gif.start()
        self.pictureLabel.setScaledContents(True)

        self.id_edit = QLineEdit(self)
        self.id_edit.move(250, 100)
        self.id_edit.setStyleSheet("QLineEdit{color:#CC6633}"
                                   "QLineEdit:hover{color:#00BFFF}"
                                   "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                   "QLineEdit{padding:2px 4px}")

        self.pass_edit = QLineEdit(self)
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.pass_edit.setStyleSheet("QLineEdit{color:#CC6633}"
                                     "QLineEdit:hover{color:#00BFFF}"
                                     "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                     "QLineEdit{padding:2px 4px}")

        self.pass_edit.move(250, 150)
        self.pass_edit_q = QLineEdit(self)
        self.pass_edit_q.setEchoMode(QLineEdit.Password)
        self.pass_edit_q.setStyleSheet("QLineEdit{color:#CC6633}"
                                       "QLineEdit:hover{color:#00BFFF}"
                                       "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                       "QLineEdit{padding:2px 4px}")
        self.pass_edit_q.move(250, 200)

        self.phnumber_edit = QLineEdit(self)
        self.phnumber_edit.move(250, 250)
        self.phnumber_edit.setStyleSheet("QLineEdit{color:#CC6633}"
                                         "QLineEdit:hover{color:#00BFFF}"
                                         "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                         "QLineEdit{padding:2px 4px}")

        self.yanzheng_edit = QLineEdit(self)
        self.yanzheng_edit.move(250, 300)
        self.yanzheng_edit.setStyleSheet("QLineEdit{color:#CC6633}"
                                         "QLineEdit:hover{color:#00BFFF}"
                                         "QLineEdit{background-color:rgba(255, 255, 255, 10%)}"
                                         "QLineEdit{padding:2px 4px}")

        self.btn_check = QRadioButton(self)
        self.btn_check.setText("显示密码")
        self.btn_check.setStyleSheet(" QRadioButton{color: #00FF99}")
        self.btn_check.move(410, 205)
        self.btn_check.clicked.connect(self.yanma)

        self.HOST = '176.215.99.164'
        self.PORT = 8888
        self.ADDR = (self.HOST, self.PORT)
        self.s = socket(AF_INET, SOCK_DGRAM)

        self.label_id = QLabel("输入您的账号:", self)
        self.label_id.move(149, 105)
        self.label_id.setFont(QFont("Microsoft YaHei"))
        self.label_id.setStyleSheet("QLabel{color: #00FF99}")

        self.label_pass = QLabel("输入您的密码:", self)
        self.label_pass.move(149, 155)
        self.label_pass.setFont(QFont("Microsoft YaHei"))
        self.label_pass.setStyleSheet("QLabel{color: #00FF99}")

        self.label_pass_q = QLabel("确认您的密码:", self)
        self.label_pass_q.move(149, 205)
        self.label_pass_q.setFont(QFont("Microsoft YaHei"))
        self.label_pass_q.setStyleSheet("QLabel{color: #00FF99}")

        self.label_shouji = QLabel("请输入手机号:", self)
        self.label_shouji.move(149, 255)
        self.label_shouji.setFont(QFont("Microsoft YaHei"))
        self.label_shouji.setStyleSheet("QLabel{color: #00FF99}")

        self.label_yanzheng = QLabel("请输入验证码:", self)
        self.label_yanzheng.move(149, 305)
        self.label_yanzheng.setFont(QFont("Microsoft YaHei"))
        self.label_yanzheng.setStyleSheet("QLabel{color: #00FF99}")

        self.loadingButton = QPushButton(self)
        self.loadingButton.setText("修改密码")
        # loadingButton.setIcon(QIcon("img/进.png"))
        self.loadingButton.move(410, 500)
        self.loadingButton.setStyleSheet("QPushButton{color:black}"
                                         "QPushButton:hover{color:red}"
                                         "QPushButton{background-color:#00FFFF}"
                                         "QPushButton{border:2px}"
                                         "QPushButton{border-radius:2px}"
                                         "QPushButton{padding:2px 4px}")
        self.loadingButton.setFixedSize(90, 30)
        self.loadingButton.clicked.connect(self.xiugaimima)

        self.yanzhengButton = QPushButton(self)
        self.yanzhengButton.setText("获取验证码")
        self.yanzhengButton.setStyleSheet("QPushButton{color:black}"
                                          "QPushButton:hover{color:red}"
                                          "QPushButton{background-color:#00FFFF}"
                                          "QPushButton{border:2px}"
                                          "QPushButton{border-radius:2px}"
                                          "QPushButton{padding:2px 4px}"
                                          )
        self.yanzhengButton.setFixedSize(90, 22)
        self.yanzhengButton.move(410, 300)
        self.yanzhengButton.clicked.connect(self.shouji)

        self.retreat = QPushButton(self)
        self.retreat.setText("后退")
        self.retreat.setStyleSheet("QPushButton{color:black}"
                                   "QPushButton:hover{color:red}"
                                   "QPushButton{background-color:#00FFFF}"
                                   "QPushButton{border:2px}"
                                   "QPushButton{border-radius:2px}"
                                   "QPushButton{padding:2px 25px}")
        # retreat.setIcon(QIcon("img/进.png"))
        self.retreat.setFixedSize(90, 30)
        self.retreat.move(310, 500)

        self.retreat.clicked.connect(self.quit)

        self.resize(600, 600)
        self.center()
        self.setWindowTitle("注册界面")

        self.sjyanzheng = ""

        self.time = QTimer(self)
        self.time.setInterval(1000)
        self.time.timeout.connect(self.Refresh)

        self.ex = None

        self.count = 60

        QApplication.setStyle("Fusion")

        self._CloseButton = QPushButton(b'\xef\x81\xb2'.decode("utf-8"), self)
        self._CloseButton.move(560, 0)
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
        self._MinimumButton.move(522, 0)
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

    def yanma(self):
        if self.btn_check.isChecked():
            self.pass_edit.setEchoMode(QLineEdit.Normal)
            self.pass_edit_q.setEchoMode(QLineEdit.Normal)
        else:
            self.pass_edit.setEchoMode(QLineEdit.Password)
            self.pass_edit_q.setEchoMode(QLineEdit.Password)

    def quit(self):
        self.hide()
        self.ex.show()

    def Refresh(self):
        if self.count > 0:
            self.yanzhengButton.setText(str(self.count) + '秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.yanzhengButton.setEnabled(True)
            self.yanzhengButton.setText('发送验证码')
            self.count = 60

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def shouji(self):
        # print(1)
        if self.yanzhengButton.isEnabled():
            self.time.start()
            self.yanzhengButton.setEnabled(False)
            HUOQU_yanzhengma(self.s, self.ADDR, self.phnumber_edit.text())

    def xiugaimima(self):
        uname = self.id_edit.text()
        P1 = self.pass_edit.text()
        P2 = self.pass_edit_q.text()
        phone = self.phnumber_edit.text()
        yanzhengma = self.yanzheng_edit.text()
        if P1 == P2 and bool(P1) == True and bool(uname) == True and bool(yanzhengma) == True and bool(phone) == True:
            result = gaimi(self.s, self.ADDR, uname, P1, phone, yanzhengma)
            if result == '修改密码成功':
                replay = QMessageBox.warning(
                    self, "!", '修改密码成功', QMessageBox.Yes)
                self.ex.show()
                self.close()
            if result == '验证码错误':
                replay = QMessageBox.warning(
                    self, "!", '验证码错误', QMessageBox.Yes)
            if result == '手机号不一致':
                replay = QMessageBox.warning(
                    self, "!", '手机号不一致', QMessageBox.Yes)
        if P1 != P2:
            replay = QMessageBox.warning(
                self, "!", "两次密码输入不一致", QMessageBox.Yes)
        if bool(P1) == False:
            replay = QMessageBox.warning(
                self, "!", "密码不能为空", QMessageBox.Yes)
        if bool(uname) == False and bool(P1) == True:
            replay = QMessageBox.warning(
                self, "!", "用户名不能为空", QMessageBox.Yes)
