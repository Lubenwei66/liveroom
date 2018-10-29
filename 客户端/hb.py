# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PIL import Image, ImageDraw, ImageFont


def tp(text):
    font = ImageFont.truetype('simsun.ttc', 30)
    a = text + '为主播送出火箭'
    h1, w1 = font.getsize(a)
    h2, w2 = font.getsize(text)
    img = Image.new('RGBA', (h1, w1), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (255, 0, 0), font=font)
    draw.text((h2, 0), '为主播送出火箭', (0, 0, 0), font=font)
    img.save("img/10.png")


def tp1(text):
    font = ImageFont.truetype('simsun.ttc', 30)
    a = text + '为主播送出超级火箭'
    h1, w1 = font.getsize(a)
    h2, w2 = font.getsize(text)
    img = Image.new('RGBA', (h1, w1), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, (255, 0, 0), font=font)
    draw.text((h2, 0), '为主播送出超级火箭', (255, 255, 255), font=font)
    img.save("img/10.png")
