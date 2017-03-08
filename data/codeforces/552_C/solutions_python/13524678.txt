# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

w, m = map(int, raw_input().split())
s = 0
for i in xrange(101):
    s += w ** i
    t = s - m
    if t == 0:
        print "YES"
        exit()
    if t < 0: continue
    for j in xrange(i - 1, -1, -1):
        if t - 2 * w ** j >= 0:
            t -= 2 * w ** j
        elif t - w ** j >= 0:
            t -= w ** j
        if t == 0:
            print "YES"
            exit()
print "NO"
