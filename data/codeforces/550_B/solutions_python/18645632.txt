I = lambda f: map(f, raw_input().split())
n, l, r, x = I(int)
C = I(int)
count = 0
for bits in xrange(1, 1 << n):
	V = [C[i] for i in xrange(n) if (bits & (1 << i)) != 0]
	if l <= sum(V) <= r and max(V) - min(V) >= x:
		count += 1
print count