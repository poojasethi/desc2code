t = int(raw_input())
for i in xrange(t):
	n,k = map(int,raw_input().split())
	e = sorted(map(float,raw_input().split()))
	sum = 0
	for j in e[k:len(e)-k]:
		sum += j
	print sum/(n-2*k)