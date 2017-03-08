from collections import defaultdict
a = {}
b = {}
a = defaultdict(lambda:0,a)
b = defaultdict(lambda:0,b)

n = int(raw_input())
for i in xrange(n):
	x, y = map(int, raw_input().split())
	a[x+y] += 1
	b[x-y] += 1

items = a.values() + b.values()

def nc2(x):
	return x*(x-1)/2

total = 0

for i in items:
	total += nc2(i)

print total