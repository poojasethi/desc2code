def cur_pos(a, d):

	if 0 <= d <= a:
		return d, 0.0
	elif a < d <= a + a:
		return a, d - a 
	elif a + a < d <= a * 3:
		return 3 * a - d, a
	else:
		return 0.0, 4 * a - d

a, d = map(float, raw_input().split())
n = int(input())
d = d * 1.0 / (4 * a) - int(d * 1.0 / (4 * a))
d *= (4 * a)

for i in xrange(1, n+1):
	dd = i * d + 0.0;
	dd = dd / (4 * a) - int(dd / (4 * a))
	dd *= (4 * a)
	x, y = cur_pos(a, dd);
	print ("%.10f %.10f")%(x, y)