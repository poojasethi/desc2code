# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
xa = [map(int, raw_input().split()) for i in xrange(n)]
xa.sort()
i = 0
while i < n and xa[i][0] < 0: i += 1
l, r = i, n - i
a = [ai for xi, ai in xa]
print max(sum(a[i - min(r, l):i + min(r, l + 1)]),
          sum(a[i - min(l, r + 1):i + min(r, l)]))
