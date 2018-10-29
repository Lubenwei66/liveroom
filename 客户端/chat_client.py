# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
import sys
import os


def get_zhuce(s, ADDR, uname, name, pwd, phone, ma):
    msg = "Z " + name + ' ' + uname + ' ' + pwd + ' ' + phone + " " + ma
    s.sendto(msg.encode(), ADDR)
    data, addr = s.recvfrom(1024)
    return data.decode()


def huoqu_yanzhengma(s, ADDR, shoujihao):
    msg = 'hq ' + shoujihao
    s.sendto(msg.encode(), ADDR)


def HUOQU_yanzhengma(s, ADDR, shoujihao):
    msg = 'HQ ' + shoujihao
    s.sendto(msg.encode(), ADDR)


def zhuce(s, ADDR, uname, name, pwd, phone, ma):  # 注册
    while True:
        data = get_zhuce(s, ADDR, uname, name, pwd, phone, ma)
        if data == 'OK':
            return "注册成功"
        elif data == '4':
            return '该用户已注册'
        elif data == '16':
            return '该昵称已注册'
        elif data == '17':
            return '该手机号已注册'
        elif data == '验证码错误':
            return '验证码错误'
        elif data == '手机号不一致':
            return '手机号不一致'


def get_gaimi(s, ADDR, uname, newpwd, phone, ma):
    msg = "GM " + uname + ' ' + newpwd + ' ' + phone + " " + ma
    s.sendto(msg.encode(), ADDR)
    data, addr = s.recvfrom(1024)
    return data.decode()


def gaimi(s, ADDR, uname, newpwd, phone, ma):
    data = get_gaimi(s, ADDR, uname, newpwd, phone, ma)
    if data == '修改密码成功':
        return "修改密码成功"
    elif data == '验证码错误':
        return '验证码错误'
    elif data == '手机号不一致':
        return '手机号不一致'


def get_denglu(s, ADDR, uname, pwd):
    msg = "L " + uname + ' ' + pwd
    s.sendto(msg.encode(), ADDR)
    # 接收登录结果
    data, addr = s.recvfrom(1024)
    msgList = data.decode().split(' ')
    return msgList


def login(s, ADDR, uname, pwd):  # 登录
    while True:
        msgList = get_denglu(s, ADDR, uname, pwd)
        print(msgList[0])
        if msgList[0] == 'OK':
            name = msgList[1]
            yue = get_yue(s, ADDR, uname)
            return (name, yue)
        elif msgList[0] == 'NO':
            return '用户名不存在'
        elif msgList[0] == '16':
            return '密码错误'
        elif msgList[0] == "17":
            return '用户名已存在'


def shouji_dl(s, ADDR, phone, yanzhengma):
    msg = "sj " + phone + ' ' + yanzhengma
    s.sendto(msg.encode(), ADDR)
    # 接收登录结果
    data, addr = s.recvfrom(1024)
    msgList = data.decode().split(' ')
    return msgList


def shouji_denlu(s, ADDR, phone, yanzhengma):
    while True:
        msgList = shouji_dl(s, ADDR, phone, yanzhengma)
        if msgList[0] == "手机号不存在":
            return "手机号不存在"
        elif msgList[0] == '17':
            return '用户名已存在'
        elif msgList[0] == '手机号不一致':
            return '手机号不一致'
        elif msgList[0] == '验证码错误':
            return '验证码错误'
        elif msgList[0] == 'OK':
            name = msgList[1]
            uname = msgList[2]
            yue = get_yue(s, ADDR, uname)
            return (name, yue)


def do_chongzhi(s, ADDR, uname, money):
    msg = "M " + uname + ' ' + money
    s.sendto(msg.encode(), ADDR)


def do_gift(s, ADDR, uname, gift, nicheng):
    msg = "gift " + uname + ' ' + gift + ' ' + nicheng
    s.sendto(msg.encode(), ADDR)


def get_yue(s, ADDR, uname):
    msg = "Y " + uname
    s.sendto(msg.encode(), ADDR)
    data, addr = s.recvfrom(1024)
    msgList = data.decode().split(' ')
    if msgList[0] == 'P':
        return msgList[1]


def send_message(s, name, addr, text):
    msg = "C %s %s" % (name, text)
    s.sendto(msg.encode(), addr)


def get_msg(s):
    msg, addr = s.recvfrom(1024)
    return msg.decode()
