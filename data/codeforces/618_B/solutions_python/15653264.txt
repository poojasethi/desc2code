# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = [map(int, raw_input().split()) for i in xrange(n)]

ans = [-1]*n
for i in xrange(n - 1, 0, -1):
    for y in xrange(n):
        for x in xrange(n):
            if a[y][x] == i:
                if ans[y] == -1:
                    ans[y] = i
                else:
                    ans[x] = i
                break
        if ans[y] != -1: break

for i in xrange(n):
    if ans[i] == -1:
        ans[i] = n

#print
#for i in xrange(n):
#    print " ".join(map(str, [min(ans[i], ans[j]) if i != j else 0 for j in xrange(n)]))
#print

print " ".join(map(str, ans))
