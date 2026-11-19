"""Draw images/icon.png (128x128 Marketplace icon): an amber rosin drop on the Sea Salt background."""
import os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), 'images', 'icon.png')
N = 1024  # supersample, then downscale

def lerp(a, b, t): return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))
def hx(h): h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

img = Image.new('RGBA', (N, N), (0, 0, 0, 0))
# rounded-square tile with a soft vertical gradient
tile = Image.new('RGBA', (N, N))
top, bot = hx('#1B212A'), hx('#0D1117')
for y in range(N):
    ImageDraw.Draw(tile).line([(0, y), (N, y)], fill=lerp(top, bot, y / N) + (255,))
mask = Image.new('L', (N, N), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, N - 1, N - 1), radius=N * 0.22, fill=255)
img.paste(tile, (0, 0), mask)

# drop shape: circle bottom + pointed top (polygon of a teardrop curve)
import math
cx, cy, r = N * 0.5, N * 0.585, N * 0.25
pts = []
for i in range(361):
    a = math.radians(i)
    # teardrop: x = r*sin(a)*sin(a/2)^m, y = -r*cos(a)
    x = cx + r * math.sin(a) * (math.sin(a / 2) ** 1.25)
    y = cy - r * 1.55 * math.cos(a) * 0.82 + r * 0.18
    pts.append((x, y))
drop = Image.new('L', (N, N), 0)
ImageDraw.Draw(drop).polygon(pts, fill=255)
drop = drop.filter(ImageFilter.GaussianBlur(1.5))

# glow under the drop
glow = Image.new('RGBA', (N, N), (0, 0, 0, 0))
ImageDraw.Draw(glow).ellipse((cx - r * 1.25, cy - r * 0.8, cx + r * 1.25, cy + r * 1.45), fill=hx('#E59B5B') + (70,))
glow = glow.filter(ImageFilter.GaussianBlur(N * 0.06))
img = Image.alpha_composite(img, Image.composite(glow, Image.new('RGBA', (N, N), (0, 0, 0, 0)), mask))

# amber body with a diagonal gradient
body = Image.new('RGBA', (N, N))
c1, c2 = hx('#F2B877'), hx('#C9732F')
for y in range(N):
    ImageDraw.Draw(body).line([(0, y), (N, y)], fill=lerp(c1, c2, max(0, min(1, (y - N * 0.25) / (N * 0.55)))) + (255,))
img.paste(body, (0, 0), drop)

# highlight
hl = Image.new('L', (N, N), 0)
ImageDraw.Draw(hl).ellipse((cx - r * 0.55, cy - r * 0.15, cx - r * 0.18, cy + r * 0.42), fill=150)
hl = hl.filter(ImageFilter.GaussianBlur(N * 0.018))
img.paste(Image.new('RGBA', (N, N), (255, 236, 210, 255)), (0, 0), Image.composite(hl, Image.new('L', (N, N), 0), drop))

# small iris "spark" (the Sea Salt accent) top-right
sx, sy, s = N * 0.74, N * 0.27, N * 0.045
d = ImageDraw.Draw(img)
d.polygon([(sx, sy - s * 2), (sx + s * 0.45, sy - s * 0.45), (sx + s * 2, sy), (sx + s * 0.45, sy + s * 0.45),
           (sx, sy + s * 2), (sx - s * 0.45, sy + s * 0.45), (sx - s * 2, sy), (sx - s * 0.45, sy - s * 0.45)], fill=hx('#AEA7ED') + (255,))

os.makedirs(os.path.dirname(OUT), exist_ok=True)
img.resize((128, 128), Image.LANCZOS).save(OUT, optimize=True)
img.resize((512, 512), Image.LANCZOS).save(OUT.replace('icon.png', 'icon-512.png'), optimize=True)
print(OUT)
