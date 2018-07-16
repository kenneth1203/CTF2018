# -*- coding: utf-8 -*-

from PIL import Image

f = open("C:\\Users\\kennethlao\\Desktop\\ctf training\\RGB")

#res = max(s)
line = f.readline()
#print(line)
img = Image.new("RGB", (503, 122))
for i in range(503):
    for j in range(122):
        #print(i, j)
        r, g, b = line.split(",")
        #print(r, g, b)
        img.putpixel([i, j], (int(r), int(g), int(b)))
        line = f.readline()
img.show()