# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from PIL import Image
from PIL.ImageOps import invert
import re

with open("C:\\Users\\kennethlao\\Desktop\\ctf training\\xy") as f:
    s = f.read().split("\n")

#res = max(s)
print(len(s))

img = Image.new("RGB", (275, 275))
for xy in s:
    x, y = re.findall("\d+", xy)
    #print(x[0], x[1])
    img.putpixel([int(x), int(y)], (255, 255, 255))
img = invert(img)
img.show()

#  dd if=./paintpaintpaint.jpg skip=21238 bs=1c of=xy