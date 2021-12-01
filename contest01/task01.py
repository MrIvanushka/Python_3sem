n = int(input())
f = [0, 1]
f.extend(f[i-1] + f[i - 2] for i in range(2, n))
print(f[n - 1])