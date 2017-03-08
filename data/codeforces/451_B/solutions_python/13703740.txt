# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())
b = sorted(a)
l, r = n, 0
for i in xrange(n):
    if a[i] != b[i]:
        l, r = min(l, i), max(r, i)

if l > r: l = r = 0
a = a[:l] + a[l:r + 1][::-1] + a[r + 1:]
if a == b:
    print "yes"
    print l + 1, r + 1
else:
    print "no"
