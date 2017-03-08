# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
cnt = coll.defaultdict(int)
num = [0] * n
for i in xrange(n - 1, -1, -1):
    num[i] = cnt[a[i] * k]
    cnt[a[i]] += 1

cnt2 = coll.defaultdict(int)
num2 = [0] * n
for i in xrange(n - 1, -1, -1):
    num2[i] = cnt2[a[i] * k]
    cnt2[a[i]] += num[i]
print sum(num2)
