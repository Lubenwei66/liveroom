# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import string
import random


def myrandom(count=6):
    myList = list(string.digits)  # 指定要生成验证码的集合，数字，大小写字母
    # 在指定的mylist集合中随机取出count个集合
    lists = random.sample(myList, count)
    return "".join(lists)


def dxyz(mobile):
    y = myrandom()  # 生成验证码
    mobile = str(mobile)  # 电话号码
    text = "您的验证码是：{}。请不要把验证码泄露给其他人。".format(y)  # 短信，不管
    print(mobile, text)  # 打印短信，手机号,不管
    l = [2, '发送成功']  # [0,'发送失败']
    return (l[0], l[1], y)  # 返回码，返回内容，验证码
