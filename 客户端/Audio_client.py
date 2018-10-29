# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from socket import *
import pyaudio
import wave
import sys
import zlib
import struct
import pickle
import time
import numpy as np

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.5


def audio(s):
    data = "".encode("utf-8")
    payload_size = struct.calcsize("L")
    p = pyaudio.PyAudio()
    stream = None
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        output=True, frames_per_buffer=CHUNK, output_device_index=0)
    except:
        print('设备索引有误，音频退出')
        return
    while True:
        while len(data) < payload_size:
            data += s.recv(81920)
        packed_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_size)[0]
        while len(data) < msg_size:
            data += s.recv(81920)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        frames = pickle.loads(frame_data)
        for frame in frames:
            stream.write(frame, CHUNK)
    sock.close()
    if stream is not None:
        stream.stop_stream()
        stream.close()
    p.terminate()


def audio_c(host, port):
    HOST = host
    PORT = port
    ADDR = (HOST, PORT)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(ADDR)
    audio(s)
