import sys
import os
from PIL import Image
from PIL import GifImagePlugin
import math
import time

tmp_dir_name = "temp"
gif = Image.open(sys.argv[1])
symb = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
#symb = [' ', '.', "'", '`', '^', '"', ',', ':', ';', 'I', 'l', '!', 'i', '>', '<', '~', '+',\
#     '_', '-', '?', ']', '[', '}', '{', '1', ')', '(', '|', '\\', '/', 't', 'f', 'j', 'r', 'x',\
#     'n', 'u', 'v', 'c', 'z', 'X', 'Y', 'U', 'J', 'C', 'L', 'Q', '0', 'O', 'Z', 'm', 'w', 'q',\
#     'p', 'd', 'b', 'k', 'h', 'a', 'o', '*', '#', 'M', 'W', '&', '8', '%', 'B', '@', '$']
frames = []
line = ""
lines = []
height = 57
width = math.floor((gif.size[0]*(height/gif.size[1]))*2.1)
os.mkdir(tmp_dir_name)

# save each frame to png image
for frame in range(gif.n_frames):
    gif.seek(frame)
    gif.resize((width,height)).convert('RGB').save(tmp_dir_name+"/frame"+str(frame)+".png")

for frame in range(gif.n_frames):
    im = Image.open(tmp_dir_name+"/frame"+str(frame)+".png")
    pix = im.load()
    
    for i in range(im.size[1]):
        for j in range(im.size[0]):
            h = math.floor(pix[j, i][0]*0.30 + pix[j, i][1]*0.59 + pix[j, i][2]*0.11)
            pix[j, i] = (h, h, h)
            idx = math.floor((h*len(symb))/256)
            line += symb[idx]
        lines.append(line)
        line = ""
    frames.append(lines)
    lines = []
    
    os.remove(tmp_dir_name+"/frame"+str(frame)+".png")
    
os.rmdir(tmp_dir_name)

# frame_interval = 0.05
# frame_interval = 0.1
frame_interval = float(sys.argv[2])
print(frame_interval)
while True:
    for frame in range(gif.n_frames):
        for line in range(height):
            print(frames[frame][line])
        time.sleep(frame_interval)
