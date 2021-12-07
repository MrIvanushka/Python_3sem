from numpy import matrix
from numpy.linalg import matrix_power

N = int(input())
start_pos = matrix([[i, ] for i in map(float, input().split(" "))])

arr = []

for i in range(N):
    arr.append([float(i) for i in input().split()])

rot_matrix = matrix(arr)

k = int(input())

ans = (rot_matrix**k) * start_pos
for i in ans:
    print(i.item(0))
