d, n = input().split()
d = float(d)
n = int(n)

value_pool = map(float, input().split())

rep = 0
lr = 0
event_count = 0
for value in value_pool:
    value = abs(value)
    if value > d:
        if lr >= n:
            event_count += 1
            lr = 0
            rep = 0
        else:
            rep += lr
            lr = 0
        rep += 1
    elif rep >= n:
        lr += 1
if rep > 0:
    event_count += 1

print(event_count)