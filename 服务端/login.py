# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mysqlpython1 import Mysqlpython
from hashlib import sha1

# 登录操作


def Login(uname, pwd):
    # 用sha1给pwd加密

    s1 = sha1()  # 创建sha1加密对象
    s1.update(pwd.encode("utf8"))  # 指定编码
    pwd2 = s1.hexdigest()  # 返回16进制加密结果

    sqlh = Mysqlpython("db1")
    select = "select password from user where user=%s;"
    result = sqlh.all(select, [uname])
    # (('7c4a8d09ca3762af61e59520943dc26494f8941b',),)

    if len(result) == 0:
        return 3  # 用户名不存在
    elif result[0][0] == pwd2:
        return 2  # 登录成功
    else:
        return 1  # 密码错误

# 注册操作


def Register(uname, nkname, phone, pwd):
    s1 = sha1()
    s1.update(pwd.encode('utf8'))
    pwd1 = s1.hexdigest()

    sqlh = Mysqlpython('db1')
    select = "select id from user where user=%s;"
    select1 = "select id from user where nickname=%s;"
    select2 = "select id from user where phone=%s;"
    insert1 = 'insert into user(user,nickname,phone,password) values(%s,%s,%s,%s);'
    insert2 = 'insert into balance(b_id,user,balance) values(%s,%s,3000)'

    result = sqlh.all(select, [uname])
    result1 = sqlh.all(select1, [nkname])
    result2 = sqlh.all(select2, [phone])
    if len(result) >= 1:
        return 4  # 用户已注册
    elif len(result1) >= 1:
        return 16  # 昵称重名
    elif len(result2) >= 1:
        return 17  # 电话号码已注册
    elif pwd == '':
        return 11  # 密码不能为空
    elif uname == '':
        return 14  # 用户名不能为空
    elif nkname == '':
        return 12  # 昵称不能为空
    elif phone == "":
        return 18  # 　电话号码为空
    else:
        sqlh.zhixing(insert1, [uname, nkname, phone, pwd1])
        result3 = sqlh.all(select, [uname])
        sqlh.zhixing(insert2, [result3[0][0], uname])
        return 5  # 注册成功

# 修改昵称


def amend_n(yname, nkname):
    sqlh = Mysqlpython('db1')
    select = "select nickname from user where nickname=%s;"
    u = "update user set nickname = %s where nickname = %s;"
    result = sqlh.all(select, [yname])
    if len(result) == 0:
        return 3  # 用户名不存在
    elif nkname == '':
        return 12  # 昵称不能为空
    else:
        sqlh.zhixing(u, [nkname, yname])
        return 7  # 昵称修改成功

# 修改密码


def amend_p(npwd, user):
    s1 = sha1()
    s1.update(npwd.encode('utf8'))
    pwd1 = s1.hexdigest()

    sqlh = Mysqlpython('db1')
    u = "update user set password = %s where user = %s;"
    sqlh.zhixing(u, [pwd1, user])
    return "修改密码成功"

    # 充值


def chongzhi(name, bal):
    sqlh = Mysqlpython('db1')
    select = "select user from user where user = %s;"
    insert1 = 'update balance set balance = balance + %s where user=%s;'
    result = sqlh.all(select, [name])
    if len(result) == 0:
        return 3  # 用户名不存在
    else:
        sqlh.zhixing(insert1, [bal, name])
        return 9  # 充值成功

# 消费


def xiaofei(name, gift):
    sqlh = Mysqlpython('db1')
    select = "select money from gift where gift = %s;"
    select1 = "select balance from balance where user = %s;"
    insert1 = "update balance set balance = balance - %s where user = %s;"
    result = sqlh.all(select, [gift])
    result1 = sqlh.all(select1, [name])
    money = result[0][0]
    if len(result1) == 0:
        return 3  # 用户名不存在
    elif result1[0][0] >= money:
        sqlh.zhixing(insert1, [money, name])
        return 0  # 执行发送礼物操作
    else:
        return 13  # 余额不足

# 提取昵称


def nick(uname):
    sqlh = Mysqlpython('db1')
    select = "select nickname from user where user = %s;"
    result = sqlh.all(select, [uname])
    return result[0][0]


def select_yue(uname):
    sqlh = Mysqlpython('db1')
    select = "select balance from balance where user = %s;"
    result = sqlh.all(select, [uname])
    return result[0][0]


def cphone(uname):
    sqlh = Mysqlpython('db1')
    select = "select phone from user where user = %s;"
    result = sqlh.all(select, [uname])
    return result[0][0]  # 电话号码


def slogin(phone):
    sqlh = Mysqlpython('db1')
    select = "select nickname from user where phone = %s;"
    result = sqlh.all(select, [phone])
    if len(result) == 0:
        return "手机号不存在"
    else:
        return result[0][0]


def cuser(phone):
    sqlh = Mysqlpython('db1')
    select = "select user from user where phone = %s;"
    result = sqlh.all(select, [phone])
    if len(result) == 0:
        return "手机号未绑定"
    else:
        return result[0][0]
