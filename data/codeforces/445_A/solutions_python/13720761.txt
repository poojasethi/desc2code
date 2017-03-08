# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
a = [list(raw_input()) for i in xrange(n)]

for y in xrange(n):
    for x in xrange(m):
        if a[y][x] != "-":
            a[y][x] = "B" if (x + y) % 2 == 0 else "W"
for line in a:
    print "".join(line)
