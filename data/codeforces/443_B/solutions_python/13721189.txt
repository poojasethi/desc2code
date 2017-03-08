# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
k = int(raw_input())
ans = 1
for sp in xrange(len(s)):
    for n in xrange(1, (len(s) + k - sp) / 2 + 1):
        flag = True
        for i in xrange(n):
            if sp + i + n > len(s) - 1:
                break
            if s[sp + i] != s[sp + i + n]:
                flag = False
                break
        if flag:
            ans = max(ans, 2 * n)
print ans
