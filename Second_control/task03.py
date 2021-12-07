import math

array = sorted((list(map(int, input().split()))))

number = math.ceil((float(input()) / 100) * len(array)) - 1

print(array[number])