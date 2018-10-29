# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from login import *
from dx import dxyz
from yydx import yyyz


def do_login(s, user,  uname, pwd, addr):
    a = Login(uname, pwd)
    if a == 3:
        s.sendto("NO".encode(), addr)
        return False
    if a == 1:
        s.sendto("16".encode(), addr)
        return False
    name = nick(uname)
    if name in user:
        s.sendto("17".encode(), addr)
        return False
    c = 'OK %s' % name
    s.sendto(c.encode(), addr)
    user[name] = addr
    return True


def huoqu_yanzhengma1(s, addr, shoujihao):
    a = dxyz(shoujihao)
    yzm = str(a[2])
    print(yzm, shoujihao)
    return yzm, shoujihao


def huoqu_yanzhengma2(s, addr, shoujihao):
    a = yyyz(shoujihao)
    yzm = str(a[2])
    print(yzm, shoujihao)
    return yzm, shoujihao


def shouji_login(s, user, phone, yanzhengma, yzm,  shoujihao, addr, iphone):
    if yanzhengma == yzm:
        name = slogin(phone)
        if name == "手机号不存在":
            s.sendto("手机号不存在".encode(), addr)
            return False
        if name in user:
            s.sendto("17".encode(), addr)
            return False
        uname = cuser(phone)
        c = 'OK %s %s' % (name, uname)
        s.sendto(c.encode(), addr)
        user[name] = addr
        del iphone[shoujihao]
        return True
    else:
        s.sendto('验证码错误'.encode(), addr)


def do_zhucelogin(s, name, uname, pwd, phone, yanzheng, yzm, shoujihao, addr, iphone):
    if yanzheng == yzm:
        a = Register(uname, name, phone, pwd)
        if a == 4:
            s.sendto("4".encode(), addr)
        if a == 5:
            s.sendto(b'OK', addr)
            del (iphone[shoujihao])
        if a == 16:
            s.sendto("16".encode(), addr)
        if a == 17:
            s.sendto("17".encode(), addr)
    else:
        s.sendto('验证码错误'.encode(), addr)


def do_yue1(s, uname, addr):
    yue = select_yue(uname)
    msg = 'P ' + str(yue)
    s.sendto(msg.encode(), addr)


def shouji_gaimi(s, user, uname, newpwd, yanzheng, yzm, shoujihao, addr, iphone):
    if yanzheng == yzm:
        a = amend_p(newpwd, uname)
        if a == "修改密码成功":
            s.sendto('修改密码成功'.encode(), addr)
            del iphone[shoujihao]
    else:
        s.sendto('验证码错误'.encode(), addr)


def do_parent(s, user):
    # 用于存储用户 {'Alex':('127.0.0.1',8888)}
    iphone = {}
    while True:
        msg, addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        if msgList[0] == 'L':
            do_login(s, user, msgList[1], msgList[2],  addr)
        elif msgList[0] == 'Z':
            for i in iphone.keys():
                if i == msgList[4]:
                    do_zhucelogin(s, msgList[1], msgList[2], msgList[3],
                                  msgList[4], msgList[5], iphone[i], i, addr, iphone)
                    break
            else:
                s.sendto('手机号不一致'.encode(), addr)
        elif msgList[0] == 'Y':
            do_yue1(s, msgList[1], addr)
        elif msgList[0] == 'hq':
            yzm, shoujihao = huoqu_yanzhengma1(s, addr, msgList[1])
            iphone[shoujihao] = yzm
        elif msgList[0] == 'HQ':
            yzm, shoujihao = huoqu_yanzhengma2(s, addr, msgList[1])
            iphone[shoujihao] = yzm
        elif msgList[0] == 'sj':
            for i in iphone.keys():
                if i == msgList[1]:
                    shouji_login(s, user, msgList[1], msgList[
                                 2], yzm, shoujihao, addr, iphone)
                else:
                    s.sendto('手机号不一致'.encode(), addr)
        elif msgList[0] == 'GM':
            for i in list(iphone.keys()):
                if i == msgList[3]:
                    shouji_gaimi(s, user, msgList[1], msgList[
                                 2], msgList[4], yzm, shoujihao, addr, iphone)
                else:
                    s.sendto('手机号不一致'.encode(), addr)
