import sys

n,t = [int(x) for x in raw_input().split()]

a = [int(x) for x in raw_input().split()]

s = set()
b = []
for i in range(n-1,-1,-1):
	s.add(a[i])
	b.append(len(s))
b.reverse()
for i in range(t):
	print b[input()-1]
