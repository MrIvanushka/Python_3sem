import matplotlib.pyplot as plt
from numpy import *

try:
    with open(input(),'r', encoding = "utf-8") as f:
        data = f.read().split('\n')
except:
    pass
for i in range(1, len(data)):
    data[i] = (data[i]).split(' ')
x = []
y = []
for i in range(1, int(data[0]) + 1):
    x.append(float(data[i][0]))
    y.append(float(data[i][1]))
N = (max(x) - min(x))/(max(y) - min(y))
plt.plot(N,1,1)
plt.scatter(x, y, s=1)
plt.axis([min(x) - 10, max(x) + 10, min(y) - 10, max(y) + 10])
plt.title(f'Number of points: {data[0]}')
plt.show()
print(x, y)
