# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PIL import ImageGrab, Image
from socket import *
from threading import Thread
import numpy as np
import zlib
import struct
import pickle
import sys


def desk():
    img = ImageGrab.grab()
    img = img.resize((1600, 900))
    sframe = np.array(img)
    sframe = sframe[:, :, ::-1]
    return sframe


def handler(connfd, desk):
    print("已连接桌面")
    while True:
        sframe = desk()
        data = pickle.dumps(sframe)
        zdata = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        try:
            connfd.sendall(
                'D'.encode() + struct.pack("L", len(zdata)) + zdata)
        except:
            connfd.close()
            break


def desk_s(s):
    while True:
        try:
            connfd, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("桌面退出")
        except Exception as e:
            print(e)
            continue
        t = Thread(target=handler, args=(connfd, desk,))
        t.setDaemon(True)
        t.start()
