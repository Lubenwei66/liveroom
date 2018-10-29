# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
from threading import *
import pyaudio
import wave
import sys
import zlib
import struct
import pickle
import numpy as np

# rate - 取样频率
# channels - 声道数
# format - 取样值的量化格式 (paFloat32, paInt32, paInt24, paInt16, paInt8
# ...)。在上面的例子中，使用get_format_from_width方法将wf.sampwidth()的返回值2转换为paInt16
# input - 输入流标志，如果为True的话则开启输入流
# output - 输出流标志，如果为True的话则开启输出流
# input_device_index - 输入流所使用的设备的编号，如果不指定的话，则使用系统的缺省设备
# output_device_index - 输出流所使用的设备的编号，如果不指定的话，则使用系统的缺省设备
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.5


def handler(connfd):
    print('已连接音频')
    p = pyaudio.PyAudio()
    try:
        input_index = p.get_default_input_device_info()['index']
    except OSError:
        print('没有音频设备')
        connfd.close()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK, input_device_index=input_index)
    while stream.is_active():
        frames = []
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        sdata = pickle.dumps(frames)
        try:
            connfd.sendall('A'.encode() + struct.pack("L", len(sdata)) + sdata)
        except:
            connfd.close()
            break
    if stream is not None:
        stream.stop_stream()
        stream.close()
    p.terminate()


def audio_s(s):
    while True:
        try:
            connfd, addr = s.accept()
        except KeyboardInterrupt:
            s.close()
            sys.exit("音频退出")
        except Exception as e:
            print(e)
            continue
        t = Thread(target=handler, args=(connfd,))
        t.setDaemon(True)
        t.start()
