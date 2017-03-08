# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S, B = coll.defaultdict(int), coll.defaultdict(int)
n, s = map(int, raw_input().split())
for loop in xrange(n):
    d, p, q = raw_input().split()
    p, q = int(p), int(q)
    if d == "S":
        S[p] += q
    else:
        B[p] += q

ans = []
for p, q in S.items():
    ans.append(("S", p, q))
ans = sorted(ans, key = lambda x: x[1], reverse = True)
for d, p, q in ans[-s:]:
    print d, p, q

ans = []
for p, q in B.items():
    ans.append(("B", p, q))
ans = sorted(ans, key = lambda x: x[1], reverse = True)
for d, p, q in ans[:s]:
    print d, p, q
