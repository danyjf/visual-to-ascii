import sys
from PIL import Image
import math

im = Image.open(sys.argv[1])
height = 57
width = math.floor((im.size[0]*(height/im.size[1]))*2.1)
im_resized = im.resize((width, height))
symb = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
# symb = [' ', '.', '^', ':', '!', '-', '=', '+', '0', '*', '#', '&', '%', '@', '$']
# symb = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+',\
#     '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x',\
#     'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q',\
#     'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
line = ""
lines = []

pix = im_resized.load()

for i in range(im_resized.size[1]):
    for j in range(im_resized.size[0]):
        h = math.floor(pix[j, i][0]*0.30 + pix[j, i][1]*0.59 + pix[j, i][2]*0.11)
        pix[j, i] = (h, h, h)
        idx = math.floor((h*len(symb))/256)
        line += symb[idx]
    lines.append(line)
    line = ""

for i in range(len(lines)):
    print(lines[i])
    