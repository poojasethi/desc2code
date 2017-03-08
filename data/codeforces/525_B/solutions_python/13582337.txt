# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = list(raw_input())
n = len(s)
m = int(raw_input())
a = map(int, raw_input().split())
a.sort()
k = 0
for i in xrange(n / 2):
    while k < m and a[k] - 1 <= i:
        k += 1
    if k % 2:
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
print ''.join(s)
