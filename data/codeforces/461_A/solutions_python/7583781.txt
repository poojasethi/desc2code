N = input()
a = map(int, raw_input().split())
a.sort()
s = sum(a)
ans = s
for i in xrange(N-1):
	ans += a[i]
	s -= a[i]
	ans += s
print ans
