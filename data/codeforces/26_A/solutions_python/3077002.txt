from sys import stdin

n = int(stdin.readline().strip())

a = [0]*(n+1)

p = []

for i in range(2, n+1):
    if a[i] == 0:
        for x in p:
            a[i * p] = 1
        for j in range(i, n+1, i):
            a[j] += 1

for i in range(2, n+1):
    a[i] = 1 if a[i] == 2 else 0
    a[i] += a[i-1]

print(a[n])
