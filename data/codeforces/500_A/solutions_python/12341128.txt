#!/usr/bin/python
a=raw_input()
b=a.split()
b=map(int, b)
c=raw_input()
d=c.split()
d=map(int, d)
i=0
while i < b[1]-1:
	i+=d[i]
if i==(b[1]-1):
	print "YES"
else:
	print "NO"
