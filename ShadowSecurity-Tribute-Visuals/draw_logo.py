#!/usr/bin/env python3
"""ShadowSecurity-Tribute logo: a round electricity meter face cut off from its box,
just the glass disc, the numbered dials in a row behind the glass, and one needle
resting a fraction past a mark. Soot rim and figures, cream dial plate, fireside
amber needle and single reading tick. Below, ShadowSecurity-Tribute in Anek Tamil,
spaced like a name pencilled on a fuse box label. At favicon size the lettering and
small dials drop away; the cream disc, black rim, and amber needle carry it."""
import sys, math
from PIL import Image, ImageDraw, ImageFont
import numpy as np
W = H = 1024
v = sys.argv[1] if len(sys.argv) > 1 else "ship"
SOOT = (20, 18, 16); CREAM = (244, 236, 206); AMBER = (198, 116, 24)
img = Image.new("RGB", (W, H), (238, 232, 210)); d = ImageDraw.Draw(img, "RGBA")
cx, cy, r = 512, 400, 268
d.ellipse([cx - r - 18, cy - r - 18, cx + r + 18, cy + r + 18], fill=SOOT)  # rim
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=CREAM)
try:
    fnum = ImageFont.truetype("fonts/AnekTamil.ttf", 44)
    fsmall = ImageFont.truetype("fonts/AnekTamil.ttf", 30)
except Exception:
    fnum = ImageFont.load_default(); fsmall = fnum
for i in range(11):
    a = math.radians(135 + i * 27)
    x1, y1 = cx + (r - 34) * math.cos(a), cy + (r - 34) * math.sin(a)
    x2, y2 = cx + (r - 10) * math.cos(a), cy + (r - 10) * math.sin(a)
    d.line([(x1, y1), (x2, y2)], fill=AMBER if i == 6 else SOOT, width=10 if i == 6 else 6)
    tx, ty = cx + (r - 78) * math.cos(a), cy + (r - 78) * math.sin(a)
    d.text((tx - 13, ty - 20), str(i), font=fnum, fill=SOOT)
# dials in a row behind the glass, lower arc of the face
for i, val in enumerate((3, 7, 1)):
    dx, dy, dr = cx - 105 + i * 105, cy + 142, 38
    d.ellipse([dx - dr, dy - dr, dx + dr, dy + dr], fill=(250, 245, 226), outline=SOOT, width=5)
    a = math.radians(-90 + val * 36)
    d.line([(dx, dy), (dx + 28 * math.cos(a), dy + 28 * math.sin(a))], fill=SOOT, width=5)
    d.text((dx - 8, dy - 30), str(val), font=fsmall, fill=SOOT)
na = math.radians(135 + 6.18 * 27)  # a fraction past the amber tick
lw = 15 if v != "v1" else 8
d.line([(cx, cy), (cx + (r - 52) * math.cos(na), cy + (r - 52) * math.sin(na))], fill=AMBER, width=lw)
d.ellipse([cx - 17, cy - 17, cx + 17, cy + 17], fill=SOOT)
d.polygon([(cx - 190, cy - 226), (cx - 96, cy - 238), (cx - 168, cy - 60), (cx - 224, cy - 96)], fill=(255, 255, 255, 42))  # glass glare
if v != "v1":
    f = ImageFont.truetype("fonts/AnekTamil.ttf", 62)
    txt = "ShadowSecurity-Tribute"; tw = d.textlength(txt, font=f)
    d.text(((W - tw) / 2, 800), txt, font=f, fill=(52, 44, 30))
rng = np.random.default_rng(3); a = np.asarray(img).astype(np.int16); n = rng.normal(0, 4, a.shape[:2])[..., None]
img = Image.fromarray(np.clip(a + n, 0, 255).astype(np.uint8))
out = "logo.png" if v == "ship" else f"scratch/logo-{v}.png"
img.save(out); print(out)
img.resize((64, 64), Image.LANCZOS).save(f"scratch/logo64-{v}.png"); print("64px saved")
