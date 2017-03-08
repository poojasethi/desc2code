# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
a = map(int, raw_input().split())

d = [0] * m 
for e in a:
    nd = d[:]
    nd[e % m] = 1
    for i in xrange(m):
        if d[i]:
           nd[(e + i) % m] = 1
    d = nd
    if d[0]:
        print "YES"
        break
else:
    print "NO"
