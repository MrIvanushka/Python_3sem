path = input()
key = input().lower()
key_count = 0
try:
    data = [i for i in open(path, 'r').read().split()]
    for word in data:
        if word.lower() == key:
            key_count += 1
except BaseException:
    pass
print(key_count)