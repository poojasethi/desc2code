n, k = map(int, raw_input().split())
if n / 2 > k or (n == 1 and k != 0):
	print -1
elif n / 2 == k:
	for i in xrange(n):
		print i + 1,
else:
	tmp = k - n / 2 + 1
	print tmp, tmp << 1,
	tmp *= 2; 
	for i in xrange(n-2):
		print tmp + i + 1,
	