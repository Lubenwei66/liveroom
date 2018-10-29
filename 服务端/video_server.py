# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
from threading import *
import numpy as np
import cv2
import zlib
import struct
import pickle
import sys


def handler(connfd, cap):
    print("已连接摄像头")
    while True:
        ret, sframe = cap.read()
        data = pickle.dumps(sframe)
        zdata = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        try:
            connfd.sendall('V'.encode() + struct.pack("L", len(zdata)) + zdata)
        except:
            connfd.close()
            break


def video_s(s):
    cap = cv2.VideoCapture(0)
    while True:
        try:
            connfd, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        t = Thread(target=handler, args=(connfd, cap,))
        t.setDaemon(True)
        t.start()
