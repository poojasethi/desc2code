# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, a, b = map(int, raw_input().split())
n *= 6
if n <= a * b:
    print a * b
    print a, b
else:
    m = int(n ** 0.5) + 1
    s = (a + m) * (b + m)
    for i in xrange(a, m):
        bb = max(int(math.ceil(1. * n / i)), b)
        if i * bb < s:
            s = i * bb
            p = i
            q = bb
    for i in xrange(b, m):
        aa = max(int(math.ceil(1. * n / i)), a)
        if i * aa < s:
            s = i * aa
            p = aa
            q = i
    print p * q
    print p, q
