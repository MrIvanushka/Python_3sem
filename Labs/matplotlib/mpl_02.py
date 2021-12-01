import matplotlib.pyplot as plt
from numpy import *
import time
import imageio 
import os

d = input()
try:
    with open(d,'r', encoding = "utf-8") as f:   
        data = (f.read().split('\n'))
except:
    pass

try:
    with open(d,'r', encoding = "utf-8") as f: 
        count = (f.read().split())
except:
    pass    
   
count_ = []
for i in count:
    count_.append(double(i))
x = []
y = []
for i in range (len(data)):
    if (i + 1) % 2 == 0:
        y += ([double(data[i].split())])
    else: 
        x += ([double(data[i].split())])
frame = []
for i in range(len(x) - 1):
    plt.axis([0, max(count_), min(count_) - abs(min(count_)/5), max(count_) + abs(max(count_)/5)])
    plt.plot(x[i],y[i], color = 'g')
    plt.grid(True)
    plt.title(f'Frame: {i + 1}') 
    plt.savefig(f'{i+1}.png')
    frame.append(f'{i+1}.png')
    plt.clf()

with imageio.get_writer('Graphics.gif', mode='I') as writer:
    for filename in frame:
        image = imageio.imread(filename)
        writer.append_data(image)
    for filename in frame:
        os.remove(filename)

os.startfile(r'Graphics.gif')
