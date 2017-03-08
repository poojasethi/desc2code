import sys
import collections

n, k = map(int, sys.stdin.readline().split())
num = map(int, sys.stdin.readline().split())

num.sort()

L = len(num)
for i in xrange(L):
    x = num[i]
    if k <= 0:
        break
    if x < 0:
        num[i] = - x
        k -= 1

if k % 2 == 1:
    num.sort()
    num[0] = - num[0]

print sum(num)
