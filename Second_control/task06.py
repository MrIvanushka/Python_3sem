import numpy as np
import numpy.linalg as lin
file = open(input(), "r")
n = int(file.readline())
k = []
for i in range(2 * n):
    k.append([float(i) for i in file.readline().split()])
k = np.array(k)
f = np.array([float(i) for i in file.readline().split()])
a = np.dot(lin.inv(k), f)
a = a.tolist()[::2]
ans = min(a)
print(-ans if ans < 0 else 0)