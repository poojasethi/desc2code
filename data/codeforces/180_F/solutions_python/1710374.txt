n = input ();
a = map (int, raw_input().split());
b = map (int, raw_input().split());

p = [0] * n;
for i in xrange (n):
	p[a[i]-1] = b[i];
print ' '.join (map(str,p));
