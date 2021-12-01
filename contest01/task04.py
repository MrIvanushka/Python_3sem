Arr = list(map(int, input().split()))
Max = max([el for el in Arr if Arr.count(el) == 1])
print(Max)