n, m = map (int, raw_input().split());
if n == 0 and m > 0:
	print ('Impossible');
else:
	mi = n + max (m - n, 0);
	mx = n + max (m - 1, 0);
	print mi, mx;
