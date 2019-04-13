# picture_convert_char.py
# -----------------------------
# 将图片转换为字符
# cmd中进入目录然后输入python ascii.py test2.jpg
# -----------------------------
# Jackkii    2019/04/13
#

# -*- coding=utf-8 -*-

from PIL import Image
# argparse库，用来管理命令行参数输入
import argparse

# 命令行输入参数处理，构建实例
parser = argparse.ArgumentParser()

parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

# 解析并获取参数
args = parser.parse_args()
# 输入的图片文件路径
IMG = args.file
# 输出字符画宽度
WIDTH = args.width
# 输出字符画高度
HEIGHT = args.height
# 输出字符画路径
OUTPUT = args.output

# 定义字符画所使用的字符集
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上【灰度值：0(黑)~255(白)】
def get_char(r, g, b, alpha=256):
    # 判断alpha值，若为0, 则表示图片中该位置为0
    if alpha == 0:
        return ' '

    # 灰度值公式，将像素的RGB值映射到灰度值上
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    # 映射
    length = len(ascii_char)        # 获取字符集长度，70
    unit = (256.0 + 1) / length

    return ascii_char[int(gray / unit)]     # 返回灰度值对映字符


# 主函数，如果ascii.py被当作python模块import时，这部分代码不会被执行
if __name__ == '__main__':
    # 打开图片文件，获取对象im
    im = Image.open(IMG)
    # 调整图片大小对应输出字符画高和宽，Image.NEAREST表示输出低质量图片
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""
    # 遍历提取图片每行像素的RGB值，调用getchar生成对应字符
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
            # im.getpixel((j,i))获取坐标（i，j)位置的RGB像素值，返回一个元组
            # 有时会包含alpha值，使用*可将元组作为参数传递给getchar,元组中每个元素对应函数每个参数
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        # 若定义了输出文件
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
