[n, k] = map (int, raw_input().split())
a = map (int, raw_input().split());

b = [-x for x in a if x < 0];
nn = len (b)
if k >= nn:
	ans = sum(a) + 2 * sum(b);
	c = [abs(x) for x in a];
	c.sort ();
	if (k-nn) % 2 == 1:
		ans -= 2 * c[0];
else:
	ans = sum (a);
	for i in xrange (k):
		ans += -2 * a[i];
print ans;
		
		
