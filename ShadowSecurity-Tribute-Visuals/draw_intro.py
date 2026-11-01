#!/usr/bin/env python3
"""ShadowSecurity-Tribute intro banner: the meter cupboard under the stairs, scenery
only. No letters, signs, logos, or interface marks anywhere; the meter dials carry
their own printed figures as part of the object, as the prose allows. The open
cupboard mouth fills the lower left, a torch left switched on lights dust and a
paint tin, the meter board stands at centre with glass dials and fuse carriers,
cables drop into shadow, a folded stepladder carries work gloves, and behind the
board the cupboard widens into the triangle under the stairs: hoover, shoe rack,
coats, a bicycle wheel. Stair treads cross the top diagonally and banister
spindles cast thin bars of hallway light. The needle has crept a hair forward."""
import sys, math, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
random.seed(71)
W, H = 1600, 900
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
SOOT = (18, 16, 14); CHAR = (38, 34, 30); CREAM = (240, 230, 200)
AMBER = (232, 164, 62); GREY = (118, 116, 110)
img = Image.new("RGB", (W, H), (26, 24, 22)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(34 - 14 * t), int(31 - 12 * t), int(27 - 10 * t)))
# sloped underside of the stairs crossing the top diagonally
d.polygon([(0, 0), (1600, 0), (1600, 120), (420, 470), (0, 560)], fill=(44, 40, 36))
for i in range(7):  # actual steps: tread and riser pairs stepping down the slope
    x0, y0 = 1330 - i * 150, 60 + i * 52
    d.polygon([(x0, y0), (x0 + 150, y0), (x0 + 150, y0 + 52), (x0, y0 + 52)], fill=(52, 47, 41))
    d.line([(x0, y0), (x0 + 150, y0)], fill=(84, 76, 64), width=6)
    d.line([(x0, y0), (x0, y0 + 52)], fill=(30, 27, 24), width=5)
# banister spindle light bars falling into the dark
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
for i in range(6):
    sx = 980 + i * 105
    ld.polygon([(sx, 60), (sx + 16, 60), (sx - 120, 620), (sx - 150, 620)], fill=(214, 208, 188, 26))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(7))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
for i in range(6):  # the spindles themselves, dark against the light
    sx = 980 + i * 105
    d.line([(sx + 6, 30), (sx - 30, 300)], fill=(12, 11, 10), width=7)
# the wider triangle of stored house, dimmer than the board
d.polygon([(760, 470), (1600, 300), (1600, 900), (760, 900)], fill=(30, 28, 25))
# coats on hooks
for cx, col in ((1330, (52, 50, 58)), (1430, (64, 54, 44)), (1520, (48, 56, 50))):
    d.ellipse([cx - 7, 428, cx + 7, 442], fill=(150, 148, 140))
    d.polygon([(cx - 42, 448), (cx + 42, 448), (cx + 52, 640), (cx - 52, 640)], fill=col)
# bicycle wheel, just visible
d.ellipse([1150, 560, 1420, 830], outline=(86, 84, 78), width=6)
d.ellipse([1272, 682, 1298, 708], fill=(86, 84, 78))
for a in range(0, 360, 45):
    d.line([(1285, 695), (1285 + 128 * math.cos(math.radians(a)), 695 + 128 * math.sin(math.radians(a)))], fill=(70, 68, 62), width=2)
# hoover at the far right under the coats: body low, handle leaning up to the wall
d.rounded_rectangle([1462, 700, 1562, 836], 24, fill=(62, 60, 64))
d.line([(1476, 706), (1396, 560)], fill=(96, 94, 90), width=10)
d.line([(1396, 560), (1426, 556)], fill=(96, 94, 90), width=10)
# shoes in pairs on the floor under the wheel, no rack crossing it
for sx in range(1170, 1420, 92):
    d.polygon([(sx, 862), (sx + 58, 862), (sx + 66, 842), (sx + 8, 846)], fill=(36, 32, 28))
# cupboard mouth, lower left, black inside
d.polygon([(0, 380), (430, 330), (430, 900), (0, 900)], fill=(8, 7, 6))
d.line([(430, 330), (430, 900)], fill=(70, 58, 40), width=10)  # door edge
d.line([(452, 318), (452, 900)], fill=(96, 78, 50), width=6)   # door face sliver
# paint tin at the cupboard mouth, standing on the floor, edge lit
d.ellipse([322, 812, 424, 834], fill=(6, 5, 4))
d.rectangle([330, 742, 414, 822], fill=(104, 102, 96)); d.ellipse([330, 730, 414, 756], fill=(140, 136, 126))
d.arc([336, 700, 408, 760], 180, 360, fill=(120, 116, 108), width=4)
d.rectangle([0, 836, 1600, 900], fill=(16, 14, 12))  # floor band the stored things stand on
# meter board at centre
bx, by, bw, bh = 470, 350, 430, 400
d.rectangle([bx - 14, by - 14, bx + bw + 14, by + bh + 14], fill=(52, 42, 30))
d.rectangle([bx, by, bx + bw, by + bh], fill=CREAM)
for sx, sy in ((bx + 16, by + 16), (bx + bw - 16, by + 16), (bx + 16, by + bh - 16), (bx + bw - 16, by + bh - 16)):
    d.ellipse([sx - 6, sy - 6, sx + 6, sy + 6], fill=(120, 112, 96), outline=SOOT, width=2)
try:
    fnum = ImageFont.truetype("fonts/AnekTamil.ttf", 30)
    fsmall = ImageFont.truetype("fonts/AnekTamil.ttf", 22)
except Exception:
    fnum = ImageFont.load_default(); fsmall = fnum
# main meter: glass disc, dials row, needle a hair past a mark
cx, cy, r = bx + 150, by + 130, 96
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(248, 242, 222), outline=SOOT, width=10)
for i in range(11):
    a = math.radians(135 + i * 27)
    x1, y1 = cx + (r - 16) * math.cos(a), cy + (r - 16) * math.sin(a)
    x2, y2 = cx + (r - 4) * math.cos(a), cy + (r - 4) * math.sin(a)
    d.line([(x1, y1), (x2, y2)], fill=SOOT, width=4)
    tx, ty = cx + (r - 40) * math.cos(a), cy + (r - 40) * math.sin(a)
    d.text((tx - 8, ty - 11), str(i), font=fsmall, fill=SOOT)
na = math.radians(135 + 6.18 * 27)  # crept a hair past the 6 mark
d.line([(cx, cy), (cx + (r - 22) * math.cos(na), cy + (r - 22) * math.sin(na))], fill=(196, 118, 26), width=7)
d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=SOOT)
# small dials in a row behind the glass, lower on the board
for i, val in enumerate((3, 7, 1, 9)):
    dx, dy, dr = bx + 62 + i * 88, by + 268, 34
    d.ellipse([dx - dr, dy - dr, dx + dr, dy + dr], fill=(248, 242, 222), outline=SOOT, width=5)
    a = math.radians(-90 + val * 36)
    d.line([(dx, dy), (dx + 22 * math.cos(a), dy + 22 * math.sin(a))], fill=SOOT, width=4)
    d.text((dx - 7, dy + 12), str(val), font=fsmall, fill=SOOT)
# glass glare catching the torch beam
d.polygon([(cx - 70, cy - 78), (cx - 18, cy - 84), (cx - 62, cy + 30), (cx - 92, cy + 10)], fill=(255, 255, 255, 46))
# fuse box with lid open and carriers in a row, right of the meter
fx, fy = bx + 288, by + 52
d.rectangle([fx, fy, fx + 118, fy + 150], fill=(226, 218, 192), outline=SOOT, width=4)
d.polygon([(fx + 118, fy + 6), (fx + 152, fy - 16), (fx + 152, fy + 128), (fx + 118, fy + 150)], fill=(206, 198, 172), outline=SOOT, width=3)
for i in range(4):
    d.rectangle([fx + 12, fy + 14 + i * 34, fx + 106, fy + 40 + i * 34], fill=(244, 238, 216), outline=SOOT, width=3)
    d.line([(fx + 12, fy + 44 + i * 34), (fx + 106, fy + 44 + i * 34)], fill=(196, 118, 26) if v == "v1" else SOOT, width=2)
# cables dropping straight down into shadow
for i, cxx in enumerate((bx + 60, bx + 150, bx + 250, bx + 350)):
    d.line([(cxx, by + bh), (cxx, 900)], fill=(12, 11, 10), width=6 if i % 2 else 8)
# folded stepladder flat against the wall, gloves on its top step
lx, ly = 950, 470
for i in range(5):
    d.rectangle([lx, ly + i * 62, lx + 150, ly + i * 62 + 16], fill=(88, 74, 54))
d.rectangle([lx, ly, lx + 18, ly + 320], fill=(70, 58, 42)); d.rectangle([lx + 132, ly, lx + 150, ly + 320], fill=(70, 58, 42))
for gx in (lx + 28, lx + 84):  # gloves: palm and finger stubs
    d.rounded_rectangle([gx, ly - 44, gx + 44, ly - 2], 12, fill=(150, 128, 84))
    for fi in range(4):
        d.rounded_rectangle([gx + 3 + fi * 10, ly - 62, gx + 11 + fi * 10, ly - 40], 3, fill=(150, 128, 84))
# torch on its nail inside the cupboard mouth, beam resting on the board
tx0, ty0 = 120, 470
d.polygon([(tx0, ty0 - 12), (tx0 + 74, ty0 - 20), (tx0 + 74, ty0 + 20), (tx0, ty0 + 12)], fill=(54, 54, 58), outline=(140, 138, 130), width=3)
d.ellipse([tx0 - 4, ty0 - 30, tx0 + 10, ty0 - 16], outline=(150, 148, 140), width=3)  # nail loop
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.polygon([(tx0 + 78, ty0), (700, 330), (760, 640)], fill=(255, 178, 74, 62 if v != "v1" else 34))
for _ in range(46):  # dust in the beam
    px, py = random.randint(220, 660), random.randint(360, 620)
    ld.ellipse([px, py, px + 3, py + 3], fill=(255, 220, 160, 150))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(12))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
d.ellipse([tx0 + 66, ty0 - 13, tx0 + 80, ty0 + 13], fill=(255, 196, 92))  # lit torch face
rng = np.random.default_rng(11); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "intro-banner.png" if v == "ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
