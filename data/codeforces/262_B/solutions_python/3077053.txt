from sys import stdin

(n, k) = [int(x) for x in stdin.readline().strip().split()]

a = [int(x) for x in stdin.readline().strip().split()]

p = 0

for i in range(0, k):
    if i < n and a[i] <= 0:
        a[i] = -a[i]
        p += 1

k -= p

a.sort()

if k % 2 == 1:
    a[0] = -a[0]

print(sum(a))
