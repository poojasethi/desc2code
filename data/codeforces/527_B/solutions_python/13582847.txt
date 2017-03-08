# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
S = raw_input()
T = raw_input()

D, A, B = {}, {}, {}
diff = 0
for i in xrange(n):
    if S[i] != T[i]:
        D[S[i] + T[i]] = A[S[i]] = B[T[i]] = i + 1
        diff += 1

for c in D:
    if c[::-1] in D:
        print diff - 2
        print D[c], D[c[::-1]]
        exit()

for c in A:
    if c in B:
        print diff - 1
        print A[c], B[c]
        exit()

print diff
print -1, -1
