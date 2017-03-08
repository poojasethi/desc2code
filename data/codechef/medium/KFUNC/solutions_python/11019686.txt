def f(x):
	return (x-1)%9 + 1

t = int(raw_input())
for i in range(t):
	a,d,l,r = map(int, raw_input().split())
	l = l - 1
	r = r -1
	s = 0
	for x in range(1,10):
		s += f(a + d*x)
	ans = 0
	while (r-l+1)%9 != 0:
		ans += f(a+d*r)
		r -= 1
	ans += s * (r-l+1)/9
	print str(ans)
