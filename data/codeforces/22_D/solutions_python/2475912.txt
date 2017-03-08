n = input ();

v = [(0, 0)] * n;
ans = [0] * n;
for i in xrange (n):
	[a, b] = map (int, raw_input (). split());
	if a > b:
		a, b = b, a;
	v[i] = (a, b);

v.sort ();

cx = v[0][0]; cy = v[0][1];


cnt = 0;
for i in xrange (1, n):
	wx, wy = v[i][0], v[i][1];
	if wx > cy:
		ans[cnt] = cy;
		cnt += 1
		cx, cy = wx, wy;
		
	else:
		cx, cy = wx, min (cy, wy);

ans[cnt] = cy;
cnt += 1;
print cnt;
print ' '.join (map (str, ans[:cnt]));
		
	


