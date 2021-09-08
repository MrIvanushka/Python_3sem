n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

for element in sorted(data):
    if element >= 0:
        print(element, end = " ")

for element in sorted(data, reverse=True):
    if element < 0:
        print(element, end = " ")
