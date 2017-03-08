# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

x, y, z = map(float, raw_input().split())
log = math.log

ans = [
    "x^y^z",
    "x^z^y",
    "(x^y)^z",
    "(x^z)^y",
    "y^x^z",
    "y^z^x",
    "(y^x)^z",
    "(y^z)^x",
    "z^x^y",
    "z^y^x",
    "(z^x)^y",
    "(z^y)^x"
]

a = [-1e9]*12
if x <= 1.0 and y <= 1.0 and z <= 1.0:
    a[0] = y**z*log(x)
    a[1] = z**y*log(x)
    a[2] = z*y*log(x)
    a[4] = x**z*log(y)
    a[5] = z**x*log(y)
    a[6] = x*z*log(y)
    a[8] = x**y*log(z)
    a[9] = y**x*log(z)
    a[10] = x*y*log(z)
else:
    if x > 1.0:
        a[0] = z*log(y) + log(log(x))
        a[1] = y*log(z) + log(log(x))
        a[2] = log(z*y) + log(log(x))
    if y > 1.0:
        a[4] = z*log(x) + log(log(y))
        a[5] = x*log(z) + log(log(y))
        a[6] = log(x*z) + log(log(y))
    if z > 1.0:
        a[8] = y*log(x) + log(log(z))
        a[9] = x*log(y) + log(log(z))
        a[10] = log(x*y) + log(log(z))

a = sorted([[a[i], i] for i in xrange(12)], reverse = True)
mx = a[0][0]
mxi = a[0][1]
for ai, i in a[1:]:
    if abs(mx - ai) < 1e-7:
        mxi = min(mxi, i)

print ans[mxi]
