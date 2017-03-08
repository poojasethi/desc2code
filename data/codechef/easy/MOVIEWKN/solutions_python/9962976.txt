def noe(a,n):
	k = 0
	for i in a:
		if i == n:
			k += 1
	if k == 1:
		return True
	else: 
		return False
t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	l = map(int,raw_input().split())
	r = map(int,raw_input().split())
	lr = []
	for j in xrange(n):
		lr.append(l[j]*r[j])
	a = max(lr)
	if noe(lr,a):
		print lr.index(a)+1
	else:
		a = max(r)
		print r.index(a)+1			