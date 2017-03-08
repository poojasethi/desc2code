#!/usr/bin/python
import sys
import fractions

(a,b,x,y) = map(int, sys.stdin.next().strip().split (" "))
p = fractions.gcd(x, y);
x /= p
y /= p
q = min([a/x, b/y])
print q*x, q*y
