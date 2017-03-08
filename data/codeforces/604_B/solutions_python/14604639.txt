# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, k = map(int, raw_input().split())
s = map(int, raw_input().split())

m = k
while m > 0 and 2*(m - 1) + k - m + 1 >= n: m -= 1
ans = 0
for i in xrange(min(m, n)):
    ans = max(ans, s[i] + s[min(2*m, n) - i - 1])
for i in xrange(2*m, n):
    ans = max(ans, s[i])
print ans
