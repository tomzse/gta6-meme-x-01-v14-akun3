#!/usr/bin/env python3
"""Render meme #14 untuk gta6-meme-x-01 (akun 3, SLOT TERAKHIR armada):
iOS SCREEN TIME WEEKLY REPORT. Format segar terverifikasi NOL di seluruh
leaderboard (2.827 entri, cek judul 20 Nov 18:39 WIB) dan bukan format kita
(v1-v13). Mesin lelucon pemenang: penantian 13 tahun DITAGIH sebagai data
pemakaian layar (4.811 hari trailer, Patience 0 menit tersisa, tidur -98%),
lalu AGEN AI yang MEMBAYAR di banner bawah. Beda dari #13 (phone bill):
laporan screen time + grafik batang harian + daftar most-used.
Angka: 4.811 hari = 17 Sep 2013 -> 19 Nov 2026; launch day Kamis 19 Nov.
Teks tajam via PIL (bukan AI image) supaya terbaca di 480px.
Output: meme14.png (1080x1080). Logo hantu dari press kit resmi make.fun.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1080, 1080
ASSETS = os.path.expanduser('~/workspace/makefun/meme-x-assets')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'meme14.png')

BG = (242, 242, 247)      # iOS grouped background
CARD = (255, 255, 255)
INK = (28, 28, 30)
GRAY = (142, 142, 147)
LINE = (229, 229, 234)
PURPLE = (88, 86, 214)    # iOS purple
BLUE = (0, 122, 255)
RED = (255, 59, 48)
GREEN = (52, 199, 89)
ORANGE = (255, 149, 0)
DARKPURPLE = (46, 26, 71)  # make.fun banner


def sans(name, size):
    paths = [
        f'/usr/share/fonts/truetype/noto/NotoSans-{name}.ttf',
        f'/usr/share/fonts/truetype/dejavu/DejaVuSans-{name}.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


img = Image.new('RGB', (W, H), BG)
d = ImageDraw.Draw(img)

MX = 60
RX = W - MX  # right edge of content (1020)


def card(y0, y1):
    d.rounded_rectangle([(MX, y0), (RX, y1)], radius=28, fill=CARD)


# --- header ---
d.text((MX, 44), 'SCREEN TIME', font=sans('Bold', 30), fill=GRAY)
d.text((MX, 82), 'Weekly Report', font=sans('Bold', 62), fill=INK)
d.text((MX, 156), 'Week of Nov 16 – 22, 2026  •  All Devices', font=sans('', 26), fill=GRAY)

# --- daily average card ---
card(204, 348)
d.text((MX + 28, 226), 'DAILY AVERAGE', font=sans('Bold', 24), fill=GRAY)
d.text((MX + 28, 252), '13y 2m', font=sans('Bold', 84), fill=INK)
d.text((RX - 28, 228), 'TOTAL TIME WAITING', font=sans('Bold', 22), fill=GRAY, anchor='ra')
d.text((RX - 28, 254), '4,811 days', font=sans('Bold', 40), fill=PURPLE, anchor='ra')
d.text((RX - 28, 306), 'since 17 Sep 2013', font=sans('', 24), fill=GRAY, anchor='ra')

# --- bar chart card ---
card(366, 584)
d.text((MX + 28, 386), 'SCREEN TIME PER DAY', font=sans('Bold', 24), fill=GRAY)
days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
heights = [84, 90, 98, 112, 106, 110, 100]  # Thu 19 Nov = launch, tallest
base_y = 536
slot_w = (RX - MX - 56) / 7
bar_w = 72
for i, (day, hgt) in enumerate(zip(days, heights)):
    cx = MX + 28 + slot_w * i + slot_w / 2
    x0 = cx - bar_w / 2
    color = PURPLE if i == 3 else BLUE
    d.rounded_rectangle([(x0, base_y - hgt), (x0 + bar_w, base_y)], radius=10, fill=color)
    d.text((cx, base_y + 10), day, font=sans('Bold', 24), fill=INK if i != 3 else PURPLE, anchor='ma')
d.text((MX + 28 + slot_w * 3 + slot_w / 2, base_y - 112 - 30), 'LAUNCH', font=sans('Bold', 20), fill=PURPLE, anchor='ma')

# --- most used card ---
card(600, 896)
d.text((MX + 28, 620), 'MOST USED', font=sans('Bold', 24), fill=GRAY)
rows = [
    ('GTA VI Trailer', '4,811 days', PURPLE, 1.00, None),
    ('Patience', '0 min left', RED, 0.02, 'LIMIT REACHED'),
    ('Sleep', 'down 98%', BLUE, 0.06, None),
    ('Rockstar Newswire', '0 updates', GRAY, 0.00, None),
]
y = 662
bar_x0 = MX + 28
bar_x1 = RX - 28
for name, val, color, frac, tag in rows:
    d.text((bar_x0, y), name, font=sans('Bold', 28), fill=INK)
    vw = d.textlength(val, font=sans('Bold', 28))
    d.text((bar_x1, y), val, font=sans('Bold', 28), fill=INK, anchor='ra')
    if tag:
        tw = d.textlength(tag, font=sans('Bold', 20))
        tx1 = bar_x1 - vw - 18
        d.rounded_rectangle([(tx1 - tw - 18, y + 2), (tx1, y + 30)], radius=12, fill=RED)
        d.text((tx1 - 9, y + 4), tag, font=sans('Bold', 20), fill=(255, 255, 255), anchor='ra')
    # track + fill
    d.rounded_rectangle([(bar_x0, y + 42), (bar_x1, y + 52)], radius=5, fill=LINE)
    if frac > 0:
        fw = max(10, (bar_x1 - bar_x0) * frac)
        d.rounded_rectangle([(bar_x0, y + 42), (bar_x0 + fw, y + 52)], radius=5, fill=color)
    y += 58

# --- pickups + notifications strip ---
card(912, 968)
d.text((MX + 28, 924), 'PICKUPS', font=sans('Bold', 22), fill=GRAY)
d.text((MX + 150, 920), '214 / day — checking for GTA VI news', font=sans('', 26), fill=INK)

# --- make.fun banner ---
d.rounded_rectangle([(MX, 984), (RX, 1060)], radius=24, fill=DARKPURPLE)
ghost = Image.open(os.path.join(ASSETS, 'mark-1024.png')).convert('RGBA')
ghost = ghost.resize((56, 56), Image.LANCZOS)
img.paste(ghost, (MX + 24, 996), ghost)
d.text((MX + 96, 994), 'Paid in full by my AI agent', font=sans('Bold', 30), fill=(255, 255, 255))
d.text((MX + 96, 1028), 'on make.fun — it earned while I waited', font=sans('', 24), fill=(200, 190, 220))

img.save(OUT, 'PNG')
print('saved', OUT, img.size, os.path.getsize(OUT), 'bytes')
