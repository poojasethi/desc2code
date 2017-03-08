n, m = map(int, raw_input().split())
b = map(int, raw_input().split())
a = [0] * (n + 1)
for i in xrange(m):
	for j in xrange(b[i], n+1):
		if a[j] == 0:
			a[j] = b[i];
for i in xrange(1, n):
	print a[i], 
print a[n]
