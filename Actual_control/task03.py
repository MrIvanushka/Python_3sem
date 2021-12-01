path = input()
exp_count = int(input())
try:
    data = [i.split() for i in open(path, 'r').read().split('\n')]
    data.sort(reverse = True, key = lambda a: float(a[1]))
    for i in range(exp_count):
        print(data[i][0])

except BaseException:
    print("Can not read data")