# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

dxy = zip([1, 0, -1 ,0], [0, 1, 0, -1])
n = int(raw_input()) 
a = [raw_input() for i in xrange(n)]
ans = True
for y in xrange(n):
    for x in xrange(n):
        cnt = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                cnt += a[ny][nx] == "o"
        ans &= cnt % 2 == 0
print "YES" if ans else "NO"
