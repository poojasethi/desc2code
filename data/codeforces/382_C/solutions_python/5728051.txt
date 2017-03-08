N = input()
a = map(int, raw_input().split())
a.sort()
if N == 1:
	print -1
elif N == 2:
	d = a[1]-a[0]
	if not d:
		print 1
		print a[0]
	elif (a[0]+a[1])%2:
		print 2
		print a[0]-d, a[1]+d
	else:
		print 3
		print a[0]-d, a[0]+d/2, a[1]+d
else:
	c = [a[i+1]-a[i] for i in xrange(len(a)-1)]
	b = sorted(set(c))
	if len(b) == 1 and b[0] == 0:
		print 1
		print a[0]
	elif len(b) == 1:
		print 2
		print a[0]-b[0], a[len(a)-1]+b[0]
	elif len(b) == 2 and b[0] == 0:
		print 0
	elif len(b) == 2 and c.count(b[1]) == 1 and b[0]*2 == b[1]:
		print 1
		print a[[i for i in xrange(len(a)-1) if a[i+1]-a[i] == b[1]][0]]+b[0]
	else:
		print 0
