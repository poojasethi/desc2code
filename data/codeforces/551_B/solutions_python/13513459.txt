# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"
a = raw_input()
b = raw_input()
c = raw_input()

cnta = coll.defaultdict(int)
cntb = coll.defaultdict(int)
cntc = coll.defaultdict(int)

for ai in a: cnta[ai] += 1
for bi in b: cntb[bi] += 1
for ci in c: cntc[ci] += 1

s = bn = cn = 0
for bm in xrange(100000):
    ok = True
    for k in alpha:
        if cnta[k] < bm * cntb[k]:
            ok = False
            break
    if not ok: break
    cm = min(max(0, (cnta[k] - bm * cntb[k]) / cntc[k]) for k in alpha if cntc[k] > 0)
    if bm + cm > s:
        bn, cn = bm, cm
        s = bm + cm

ans = b * bn + c * cn
for c in alpha:
    ans += c * (cnta[c] - bn * cntb[c] - cn * cntc[c])
print ans
