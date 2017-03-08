N = input()
a = map(int, raw_input().split())
p = -1; c = 0
for i in xrange(N-1):
	if a[i] > a[i+1]:
		p = i+1
		c += 1
if c == 0:
	print 0
elif c == 1 and a[N-1] <= a[0]:
	print N-p
else:
	print -1
