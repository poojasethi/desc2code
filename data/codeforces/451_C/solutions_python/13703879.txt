# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

t = int(raw_input())
for loop in xrange(t):
    n, k, d1, d2 = map(int, raw_input().split())
    ok = False
    for i in xrange(4):
        x = 1 if i % 2 else -1
        y = 1 if i / 2 else -1

        z = k + x*d1 + y*d2
        b = z/3
        a = b - x*d1
        c = b - y*d2
        ok |= z%3 == 0 and 0 <= a <= n/3 and -0 <= b <= n/3 and 0 <= c <= n/3
    if (n%3 == 0 and ok):
        print "yes"
    else:
        print "no"
