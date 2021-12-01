data = [i for i in input().split("#")]
max = ""
for el in data:
    if len(el) > len(max):
        max = el

print(max)