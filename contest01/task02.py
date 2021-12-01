n = int(input())
f = [0] * 8 + [1]
for i in range(9, n):
    f[i % 9] = sum(f) - f[i % 9]
print(f[n % 9 - 1])