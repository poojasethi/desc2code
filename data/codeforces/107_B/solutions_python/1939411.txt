import sys
n,m,h = map(int, raw_input().split())
s = map(int, raw_input().split())

p = 1.0
h -= 1
s[h] -= 1
n -= 1
total = sum(s)
if total < n:
    print -1.0
else:
    for i in range(n):
        p *= (total - s[h] - i)/(1.0*(total - i))
    print 1.0 - p


