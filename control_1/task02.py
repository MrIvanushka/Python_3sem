arr = [i for i in input().split()]
sum = 0
for element in arr:
    try:
        sum += int(element)
    except ValueError:
        pass
print(sum)