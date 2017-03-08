# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

mod = 10**9 + 7

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

ans = 1
for i in xrange(n/k):
    l, r = b[i]*10**(k-1) - 1, (b[i] + 1)*10**(k-1) - 1
    cnt = (10**k - 1)/a[i] - (r/a[i] - l/a[i]) + 1
    ans = (ans * cnt) % mod
print ans
