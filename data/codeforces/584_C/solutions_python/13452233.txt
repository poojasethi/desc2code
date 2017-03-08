# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

alpha = "abcdefghijklmnopqrstuvwxyz"
def another(a1, a2):
    for a in alpha:
        if a != a1 and a != a2:
            return a

n, t = map(int, raw_input().split())
s1 = raw_input()
s2 = raw_input()

ans = [another(a1, a2) for a1, a2 in zip(s1, s2)]
t1, t2 = n, n
for i in xrange(n):
    if t1 == t2 == t: break
    if s1[i] == s2[i]:
        ans[i] = s1[i]
        t1 -= 1
        t2 -= 1

i = 0
while i < n:
    if t1 == t: break
    if ans[i] != s1[i]:
        ans[i] = s1[i]
        t1 -= 1
    i += 1

while i < n:
    if t2 == t: break
    if ans[i] != s2[i]:
        ans[i] = s2[i]
        t2 -= 1
    i += 1

if t1 == t2 == t:
    print "".join(ans)
else:
    print -1
