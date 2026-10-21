"""Make QR codes and a printable A4 sheet for the Organ AR Atlas.

Usage: python3 make_qr.py <app link> <output folder>
Example: python3 make_qr.py https://yourname.github.io/organ-ar qr
"""
import sys
from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

ORGANS = [("brain", "Brain"), ("heart", "Heart"), ("lungs", "Lungs"), ("liver", "Liver"),
          ("kidneys", "Kidneys"), ("stomach", "Stomach"), ("intestines", "Intestines")]

base = sys.argv[1].split("#")[0].rstrip("/") if len(sys.argv) > 1 else ""
out = Path(sys.argv[2] if len(sys.argv) > 2 else "qr")
if not base:
    sys.exit("Give the app link, e.g. python3 make_qr.py https://yourname.github.io/organ-ar")
out.mkdir(parents=True, exist_ok=True)


def font(size, bold=False):
    names = ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", "Arial Bold.ttf" if bold else "Arial.ttf"]
    for n in names:
        for d in ["/usr/share/fonts/truetype/dejavu/", "/Library/Fonts/", "C:/Windows/Fonts/", ""]:
            try:
                return ImageFont.truetype(d + n, size)
            except OSError:
                pass
    return ImageFont.load_default()


def qr_img(url, px):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2, box_size=10)
    q.add_data(url)
    q.make(fit=True)
    return q.make_image(fill_color="black", back_color="white").convert("RGB").resize((px, px), Image.NEAREST)


items = [("all", "Whole body", base)] + [(slug, name, f"{base}#{slug}") for slug, name in ORGANS]
for slug, name, url in items:
    qr_img(url, 800).save(out / f"qr-{slug}.png")

# A4 at 150 dpi: 1240 x 1754 px, 2 columns x 4 rows
W, H = 1240, 1754
sheet = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(sheet)
d.text((80, 60), "BioAR", font=font(54, True), fill="#1d2626")
d.text((80, 128), "Scan with your phone camera, then tap View in AR.", font=font(26), fill="#5c6967")
cw, ch, top = (W - 160) // 2, 360, 190
for i, (slug, name, url) in enumerate(items):
    c, r = i % 2, i // 2
    x, y = 80 + c * cw, top + r * ch
    d.rounded_rectangle([x + 10, y + 10, x + cw - 10, y + ch - 10], radius=18, outline="#d3dbd8", width=3)
    sheet.paste(qr_img(url, 270), (x + 30, y + 45))
    d.text((x + 315, y + 140), name, font=font(34, True), fill="#8c2b2b")
    d.text((x + 315, y + 190), "Life-size AR" if slug != "all" else "Start here", font=font(20), fill="#5c6967")
d.text((80, H - 60), "Models: BodyParts3D (DBCLS) and Human Reference Atlas (HuBMAP), CC BY 4.0. For learning only.",
       font=font(20), fill="#5c6967")
sheet.save(out / "qr-sheet.pdf", resolution=150)
sheet.save(out / "qr-sheet.png")
print(f"Made {len(items)} QR codes and qr-sheet.pdf in {out}/")
