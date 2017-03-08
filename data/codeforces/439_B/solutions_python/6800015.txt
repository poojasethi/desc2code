n, x = map(int, raw_input().split());
c = map(int, raw_input().split());
c.sort();
ans = 0;
for i in xrange(n):
	ans += c[i]*x
	if x > 1:
		x -= 1;
print ans
