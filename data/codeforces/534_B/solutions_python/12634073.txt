#http://codeforces.com/contest/534/problem/B
#problem solved by Benegripe
#/usr/bin/py

import math

v1,v2 = [int(x) for x in raw_input().split()]
t,d = [int(x) for x in raw_input().split()]
dist = 0
for i in range(t):
	dist += min(v1 + d*i,v2 + d*(t-i-1))
print dist
