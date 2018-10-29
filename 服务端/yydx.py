# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import http.client
import urllib
import json
import string
import random

host = "api.voice.ihuyi.com"
sms_send_uri = "/webservice/voice.php?method=Submit"

# APIID
account = "V45163593"
# APIKEY
password = "9f54bedf4acb695300b540d9e5ec1f25"


def send_sms(text, mobile):
    params = urllib.parse.urlencode({'account': account, 'password': password,
                                     'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


def myrandom(count=4):
    myList = list(string.digits)  # 指定要生成验证码的集合，数字，大小写字母
    # 在指定的mylist集合中随机取出count个集合
    lists = random.sample(myList, count)
    return "".join(lists)


def yyyz(mobile):
    y = myrandom()
    mobile = str(mobile)
    text = str(y)
    x = send_sms(text, mobile)
    a = json.loads(x)
    l = list(a.values())
    print(l[0], l[1])
    return (l[0], l[1], y)  # 返回码，返回内容，验证码
