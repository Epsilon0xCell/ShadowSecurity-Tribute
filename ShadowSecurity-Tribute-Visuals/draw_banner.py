#!/usr/bin/env python3
"""ShadowSecurity-Tribute wordmark banner: a hallway in an ordinary house seen along
its length. Left foreground the understairs door stands ajar and inside the dark the
meter board shows dials, an open fuse box, and a torch on its nail. The stair runner
climbs out of shot, a coat hangs on the newel post, the hall narrows to a kitchen
doorway spilling warm light, and the far front door has frosted glass with grey
daylight behind it. The title is written on the meter board itself, in small hand
lettering on the card slotted above the dials, in Anek Tamil."""
import sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
W, H = 2560, 640
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
SOOT = (20, 18, 16); CREAM = (240, 230, 200); AMBER = (232, 164, 62)
img = Image.new("RGB", (W, H), (74, 68, 60)); d = ImageDraw.Draw(img, "RGBA")
for y in range(H):  # hallway wall and floorboards in perspective
    t = y / H
    col = (int(96 - 30 * t), int(88 - 26 * t), int(76 - 22 * t)) if y < 430 else (int(88 - 20 * t), int(70 - 16 * t), int(50 - 10 * t))
    d.line([(0, y), (W, y)], fill=col)
for i in range(9):  # floorboard seams converging
    d.line([(i * 160, 640), (900 + i * 90, 430)], fill=(52, 40, 28), width=3)
# front door far end with frosted glass, grey daylight
d.rectangle([2260, 90, 2470, 470], fill=(44, 42, 40))
d.rectangle([2284, 114, 2446, 300], fill=(164, 172, 170))
d.rectangle([2284, 324, 2446, 446], fill=(58, 54, 50))
d.ellipse([2418, 330, 2436, 348], fill=(170, 150, 90))
# kitchen doorway mid right spilling warm light
d.rectangle([1760, 130, 2020, 470], fill=(58, 44, 30))
d.rectangle([1784, 154, 1996, 470], fill=(255, 190, 96))
layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
ld.polygon([(1784, 470), (1996, 470), (2180, 640), (1620, 640)], fill=(255, 178, 74, 66))
img = Image.alpha_composite(img.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(14))).convert("RGB")
d = ImageDraw.Draw(img, "RGBA")
# stair runner climbing out of shot, centre
d.polygon([(940, 640), (1300, 170), (1470, 170), (1150, 640)], fill=(122, 52, 44))
d.polygon([(1022, 640), (1352, 204), (1418, 204), (1132, 640)], fill=(140, 64, 52))
for i in range(6):  # banister spindles and rail
    x = 1330 + i * 6
    d.line([(880 + i * 78, 620 - i * 78), (880 + i * 78, 470 - i * 78)], fill=(30, 26, 22), width=8)
d.line([(850, 640), (1330, 130)], fill=(36, 30, 24), width=14)
# newel post with a coat hanging on it
d.rectangle([806, 380, 862, 640], fill=(40, 34, 26))
d.ellipse([812, 356, 856, 400], fill=(52, 44, 34))
d.polygon([(790, 420), (880, 420), (896, 600), (776, 600)], fill=(54, 58, 66))
# understairs door ajar, left foreground, dark triangle inside
d.polygon([(70, 640), (70, 150), (560, 300), (560, 640)], fill=(10, 9, 8))
d.polygon([(560, 300), (700, 250), (700, 640), (560, 640)], fill=(88, 70, 46))  # door face
d.line([(676, 420), (676, 460)], fill=(180, 156, 92), width=6)  # handle
# meter board inside the dark
bx, by = 130, 330
d.rectangle([bx, by, bx + 330, by + 270], fill=CREAM)
try:
    fcard = ImageFont.truetype("fonts/AnekTamil.ttf", 23 if v != "v1" else 20)
    fsmall = ImageFont.truetype("fonts/AnekTamil.ttf", 17)
except Exception:
    fcard = ImageFont.load_default(); fsmall = fcard
# the slotted card above the dials carries the title
d.rectangle([bx + 18, by + 12, bx + 312, by + 56], fill=(250, 245, 226), outline=SOOT, width=2)
txt = "ShadowSecurity-Tribute"; tw = d.textlength(txt, font=fcard)
d.text((bx + 165 - tw / 2, by + 18), txt, font=fcard, fill=(52, 44, 30))
cx, cy, r = bx + 105, by + 140, 62
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(248, 242, 222), outline=SOOT, width=7)
for i in range(11):
    a = math.radians(135 + i * 27)
    d.line([(cx + (r - 12) * math.cos(a), cy + (r - 12) * math.sin(a)), (cx + (r - 3) * math.cos(a), cy + (r - 3) * math.sin(a))], fill=SOOT, width=3)
na = math.radians(135 + 6.18 * 27)
d.line([(cx, cy), (cx + (r - 16) * math.cos(na), cy + (r - 16) * math.sin(na))], fill=(198, 116, 24), width=5)
d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=SOOT)
for i, val in enumerate((3, 7, 1, 9)):  # small dials row
    dx, dy = bx + 42 + i * 82, by + 224
    d.ellipse([dx - 24, dy - 24, dx + 24, dy + 24], fill=(248, 242, 222), outline=SOOT, width=3)
    a = math.radians(-90 + val * 36)
    d.line([(dx, dy), (dx + 15 * math.cos(a), dy + 15 * math.sin(a))], fill=SOOT, width=3)
# fuse box, lid open, right of the dial
fx, fy = bx + 196, by + 74
d.rectangle([fx, fy, fx + 84, fy + 108], fill=(226, 218, 192), outline=SOOT, width=3)
d.polygon([(fx + 84, fy + 4), (fx + 108, fy - 10), (fx + 108, fy + 92), (fx + 84, fy + 108)], fill=(206, 198, 172), outline=SOOT, width=2)
for i in range(3):
    d.rectangle([fx + 8, fy + 10 + i * 32, fx + 76, fy + 32 + i * 32], fill=(244, 238, 216), outline=SOOT, width=2)
# torch on its nail, beam resting low
d.polygon([(492, 372), (540, 366), (540, 390), (492, 384)], fill=(54, 54, 58), outline=(140, 138, 130), width=2)
d.ellipse([534, 368, 544, 388], fill=(255, 196, 92))
for cxx in (bx + 50, bx + 165, bx + 280):  # cables down
    d.line([(cxx, by + 270), (cxx, 640)], fill=(12, 11, 10), width=5)
rng = np.random.default_rng(5); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "banner.png" if v == "ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
