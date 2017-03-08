# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

hack = ans = 0
while 1:
    for i in xrange(n):
        if 0 <= a[i] <= hack:
            hack += 1
            a[i] = -1
    if hack == n: break
    ans += 1
    for i in xrange(n - 1, -1, -1):
        if 0 <= a[i] <= hack:
            hack += 1
            a[i] = -1
            flag = True
    if hack == n: break
    ans += 1
print ans
