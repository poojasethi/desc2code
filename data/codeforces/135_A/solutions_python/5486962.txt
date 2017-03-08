n = input();
a = map(int, raw_input().split());
pos = 0;
for i in xrange(n):
	if a[i] > a[pos]:
		pos = i;
a[pos] = 1 if a[pos] != 1 else 2
a.sort();
for i in xrange(n):
	print a[i],
