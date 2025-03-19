import os
import qrcode ##need to pip install qrcode first

img = qrcode.make("https:...")

img.save("qr.png", "PNG")