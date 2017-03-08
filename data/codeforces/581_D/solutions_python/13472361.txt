# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

xa, ya, xb, yb, xc, yc = map(int, raw_input().split())

ans = []
for a, b, c in it.product([0, 1], repeat = 3):
    if a == 0: x1, y1 = xa, ya
    else: x1, y1 = ya, xa
    if b == 0: x2, y2 = xb, yb
    else: x2, y2 = yb, xb
    if c == 0: x3, y3 = xc, yc
    else: x3, y3 = yc, xc
    if x1 == x2 == x3 and x1 == y1 + y2 + y3:
        for i in xrange(y1): ans.append("A" * x1)
        for i in xrange(y2): ans.append("B" * x2)
        for i in xrange(y3): ans.append("C" * x3)
        break
    elif x1 == x2 + x3 and y2 == y3 and x1 == y1 + y2:
        for i in xrange(y1): ans.append("A" * x1)
        for i in xrange(y2): ans.append("B" * x2 + "C" * x3)
        break
    elif x2 == x1 + x3 and y1 == y3 and x2 == y2 + y1:
        for i in xrange(y2): ans.append("B" * x2)
        for i in xrange(y1): ans.append("A" * x1 + "C" * x3)
        break
    elif x3 == x1 + x2 and y1 == y2 and x3 == y3 + y1:
        for i in xrange(y3): ans.append("C" * x3)
        for i in xrange(y1): ans.append("A" * x1 + "B" * x2)
        break
else:
    print -1
    exit()

print len(ans)
for line in ans:
    print line 
