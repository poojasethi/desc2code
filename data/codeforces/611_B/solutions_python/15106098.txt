# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

a, b = map(int, raw_input().split())

ans = 0
for i in xrange(1, 61):
    for j in xrange(i):
        x = "".join(map(str, [1 if k != j else 0 for k in xrange(i)]))
        if x[0] == "0": continue
        x = int(x, 2)
        if a <= x <= b:
            ans += 1
print ans
