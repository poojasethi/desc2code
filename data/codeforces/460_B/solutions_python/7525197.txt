def S(x):
	res = 0
	while x:
		res += x%10
		x /= 10
	return res
a, b, c = map(int, raw_input().split())
s = [b*x**a+c for x in xrange(1, 82)]
ans = []
for x in s:
	if 0 < x and x < 1e9 and x == b*S(x)**a+c:
		ans += [x]
print len(ans)
print ' '.join(map(str, ans))
