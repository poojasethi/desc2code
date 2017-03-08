# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

less = set(range(1, n + 1)) - set(a)
cnt = [0] * 100005
for ai in a: cnt[ai] += 1
ans = a[:]
for i in xrange(n):
    if cnt[a[i]] > 1 or a[i] > n:
        ans[i] = less.pop()
        cnt[a[i]] -= 1
print  " ".join(map(str, ans))
