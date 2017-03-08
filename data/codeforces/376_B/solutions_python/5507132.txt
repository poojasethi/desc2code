n, m = map(int, raw_input().split());
p = [0] * (n + 1);
for i in xrange(m):
	a, b, c = map(int, raw_input().split());
	p[a] -= c; 
	p[b] += c;
ans = 0;
for i in xrange(n+1):
	if p[i] < 0:
		ans -= p[i];
print ans;

