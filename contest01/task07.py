files = [i for i in input().split(" ")]
words = []
for path in files:
    try:
        words.extend([i for i in open(path, 'r').read().split()])
    except Exception:
        pass
print(*sorted(set(words)))