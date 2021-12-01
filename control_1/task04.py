line = input()
max_size = 0
size = 0
for i in line:
    if i == '1':
        size += 1
    else:
        max_size = max(size, max_size)
        size = 0
max_size = max(size, max_size)
print(max_size)