arr = [list(map(int, input().split()))]
N = int(input())
arr.sort()
for i in range(len(arr) - N, len(arr)):
    print(arr[i])