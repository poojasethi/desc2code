n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
b = [0] * n
c = [0] * n
p = 1005
for i in xrange(n):
	b[i] = a[i];
	cnt = 0
	for j in xrange(i+1, n):
		b[j] = b[j-1] + k
	for j in xrange(i-1, -1, -1):
		b[j] = b[j+1] - k;
	for j in xrange(n):
		if a[j] != b[j]:
			cnt += 1;
		if b[j] <= 0:
			cnt += 1006
	if cnt < p:
		p = cnt
		c = b[:]
print p
for i in xrange(n):
	if a[i] < c[i]:
		print '+', i+1, c[i]-a[i]
	elif a[i] > c[i]:
		print '-', i+1, a[i]-c[i]
