t = int(raw_input())
while t>0:
	m,a = raw_input().split()
	m = int(m)
	a = a.split('*')
	a = filter(None,a)
	pre = 1
	cur = 0
	l = len(a)
	ans = 1
	# b = []
	for x in xrange(0,l,2):
		cur = pow(int(a[x]),int(a[x+1]),m)
		ans = (cur*pre)%m
		pre = ans
	print ans
	t -= 1