n = int(input());
a = map(int, raw_input().split());
ans = "";

s = sum(a);
f = 1;
while s > 0:
	if f % 2:
		for i in xrange(1, n):
			ans += 'R'
			if a[i] > 0:
				a[i] -= 1;
				ans += 'P';
	else:
		for i in xrange(n-2, -1, -1):
			ans += 'L';
			if a[i] > 0:
				a[i] -= 1;
				ans += 'P'
	f += 1;
	s = sum(a);
print ans;
