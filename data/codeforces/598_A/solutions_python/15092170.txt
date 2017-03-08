t = input()
for x in xrange(t):
	n = input()
	ans = 0
	ans = (n*(n+1))/2
	tmp = 1
	while tmp <= n:
		ans = ans - 2*tmp
		tmp = tmp*2
	print ans