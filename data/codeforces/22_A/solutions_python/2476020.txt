n = input ();
v = map (int, raw_input().split());
v.sort ();
if v[n - 1] == v[0]:
	print 'NO'
else:
	i = 1;
	while v[i] == v[i-1]:
		i += 1;
	print v[i];
