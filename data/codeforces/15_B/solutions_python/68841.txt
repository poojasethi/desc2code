#!/usr/bin/python
import sys

t = int(sys.stdin.next())
for ii in xrange(t):
    (n, m, x1, y1, x2, y2) = map(int, sys.stdin.next().strip().split (" "))
    ur = 0
    x = n - abs(x1 - x2)
    y = m - abs(y1 - y2)
    ur = n*m  + max([(2*x - n),0])*max([(2*y - m),0]) - 2*x*y
    print "%d" % (ur)





































