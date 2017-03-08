# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

ans1 = n/a
ans2 = 0
if n >= b:
    ans2 = (n - c)/(b - c)
    rem = n - ans2*(b - c)
    ans2 += rem/a
print max(ans1, ans2)
