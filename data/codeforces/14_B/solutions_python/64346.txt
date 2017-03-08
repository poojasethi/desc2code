#!/usr/bin/python
import sys
g = {}

def getRange (a, b):
    if (b > a):
        return range(a, b+1)
    else:
        return range(b, a+1)

"""
main function starts from here
This problem solved using Bi partite graph.
"""
(n, x0) = map (int, sys.stdin.next().strip().split(" "))
for i in xrange(1001):
    g[i] = []

for ii in xrange(n):
    (a, b) = map(int, sys.stdin.next().strip().split (" "))
    l = getRange(a,b);
    for i in l:
        g[i].append(ii)

x = 0
for i in xrange(1001):
    if len(g[i]) > x:
        x = len(g[i])

if (x < n):
    print -1
    sys.exit (0)

md = 1000
for i in xrange(1001):
    if (len(g[i]) == x) and (md > abs(x0 - i)):
        md = abs(x0 - i)

print md



