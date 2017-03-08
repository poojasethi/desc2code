n,m = map(int,raw_input().split())
a = map(int,raw_input().split())
ones, minus = [0,0]
for i in a:
	if i == 1:
		ones += 1
	else:
		minus += 1

for i in xrange(m):
	l, r = map(int,raw_input().split())
	print 1 if((r-l+1)%2 == 0 and ones>=(r-l+1)/2 and minus >= (r-l+1)/2) else 0
