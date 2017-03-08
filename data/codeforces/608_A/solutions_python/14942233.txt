# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, s = map(int, raw_input().split())
ft = [map(int, raw_input().split()) for i in xrange(n)]
ft = sorted(ft, key = lambda x:x[1], reverse = True)

ans = 0
for f, t in ft:
    ans += s - f
    s = f
    if ans < t:
        ans = t
ans += s
print ans
