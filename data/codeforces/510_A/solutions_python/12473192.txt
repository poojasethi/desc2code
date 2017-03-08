#!/usr/bin/py
n,m = [ int(x) for x in raw_input().split() ]
for x in xrange(n):
	if x%2==0:
		print '#'*m
	elif 1 == x % 4:
		print '.'*(m-1) + '#'
	elif 3 == x % 4:
		print '#'+'.'*(m-1)
