#! usrbinenv python3
# -- coding utf-8 --
import pytesseract
from pytesseract import image_to_string
from PIL import Image, ImageDraw  #调用python的两个图像处理库


def get_qr_list():
    qr_list = list()  #初始化一个列表
    for a in range(5 * 9):  # 在一个列表中再构建59个列表
        qr_list.append(list())
        for b in range(5 * 9):  # 对应列表补0
            qr_list[a].append(0)
    for e in range(5):
        for f in range(5):
            fname = "C:\\Users\\kennethlao\\Desktop\\ctf training\\zip\\" + '%s.png' % (
                e * 5 + f + 1)

            img = Image.open(fname).convert('L')  #打开目标文件 L表示八位像素 黑白
            sx, sy, ex, ey, tx = 0, 0, 0, 0, 2
            for x in range(9):  #九行
                ty = 2
                tx += 1
                sx = x * 22 + tx + 1
                for y in range(9):  #九列
                    ty += 1
                    sy = y * 21 + ty + 1
                    ex, ey = sx + 20, sy + 19

                    img_temp = img.crop((sx, sy, ex, ey))  #对图像进行剪切

                    #code = pytesseract.image_to_string(
                    #    img_temp, config="-psm 5")  #获取剪切后图像的数字
                    #img_temp.show()
                    pw, ph = img_temp.size
                    #print(pw, ph)
                    code = 0
                    for k in range(pw):
                        for l in range(ph):
                            #print(k, l)
                            code += 255 - img_temp.getpixel((k, l))
                            #print(code)

                    if code > 0:
                        #print("yes")
                        qr_list[f * 9 + x][e * 9 + y] = 1  #有数字则将对应的qr_list赋值为1
                        print(qr_list)

                    #print(qr_list[f * 9 + x][e * 9 + y], (x, y),
                    #     (sx, sy, ex, ey), (e, f, x, y))
    return qr_list


def get_qr_image(qr_list):
    print(qr_list)
    img = Image.new('L', (10 * 47, 10 * 47), (255))  #创建一个图像
    draw = ImageDraw.Draw(img)
    for e in range(5 * 9):
        for f in range(5 * 9):
            if qr_list[f][e]:  #如果qr_list[f][e]为1
                draw.rectangle(
                    ((e + 1) * 10, (f + 1) * 10, (e + 2) * 10, (f + 2) * 10),
                    fill=(0))  #将对应区块涂黑

            #print(qr_list[f][e], ' ', end='')
        #print()
    img.show()


get_qr_image(get_qr_list())