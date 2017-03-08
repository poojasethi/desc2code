# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())

xy = set()
for i in xrange(n):
    xy.add(tuple(map(int, raw_input().split())))

H, W = 1005, 1005
ans = 0
# / directoin
for sx in xrange(-H, W):
    cnt = 0
    for y in xrange(max(0, -sx), min(H, W - sx)):
        x = sx + y
        if (x, y) in xy:
            cnt += 1
    ans += cnt*(cnt - 1)/2

# \ direction
for sx in xrange(W + H):
    cnt = 0
    for y in xrange(max(0, sx - W), min(H, sx)):
        x = sx - y
        if (x, y) in xy:
            cnt += 1
    ans += cnt*(cnt - 1)/2

print ans
