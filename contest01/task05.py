Arr = [i for i in input().split()]
for i in range(len(sorted(Arr, key = lambda a: str(100000 - Arr.count(a)* 1000)+a[0]))):
    if sorted(Arr, key = lambda a: str(100000 - Arr.count(a)* 1000)+a[0])[i-1] != sorted(Arr, key = lambda a: str(100000 - Arr.count(a)* 1000)+a[0])[i]:
        print(Arr.count(sorted(Arr, key = lambda a: str(100000 - Arr.count(a)* 1000)+a[0])[i]), sorted(Arr, key = lambda a: str(100000 - Arr.count(a)* 1000)+a[0])[i])