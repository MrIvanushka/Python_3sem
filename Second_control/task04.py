import numpy as np

time_stamp = int(input())

dict = { }

for i in range(time_stamp):
    data = input().split()
    if data[1] in dict:
        dict[data[1]] = np.append(dict[data[1]], float(data[5]))
    else:
        dict[data[1]] = np.array(float(data[5]))

fluctuations = []

for key in dict.keys():
    if(dict[key].size > 1):
        fluctuations.append((key,dict[key].max() - dict[key].min()))

fluctuations.sort(key = lambda a: a[1] * 1000000 + int(a[0]))

if len(fluctuations) == 0:
    print(-1)
elif len(fluctuations) < 3:
    for element in fluctuations:
        print(element[0], end=" ")
else:
    for i in range(3):
        element = fluctuations[i]
        print(element[0], end=" ")