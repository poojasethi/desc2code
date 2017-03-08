import sys

(n, m, k) = [int(buf) for buf in sys.stdin.readline().split()]

x = sorted([int(buf) for buf in sys.stdin.readline().split()], reverse=True)

ans = 0
m -= k

for c in x:
    if m > 0:
        ans += 1
        m -= c - 1

print(-1 if m > 0 else ans)
