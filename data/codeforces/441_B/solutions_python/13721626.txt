# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, v = map(int, raw_input().split())
fruit = [0] * 3010
for i in xrange(n):
    a, b = map(int, raw_input().split())
    fruit[a] += b

ans = 0
for i in xrange(1,3005):
    w = v
    get = min(w, fruit[i - 1])
    ans += get
    w -= get
    get = min(w, fruit[i])
    ans += get
    fruit[i] -= get
print ans
