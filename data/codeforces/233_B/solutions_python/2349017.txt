import math

n = input ();

def f (x):
	cnt = 0;
	while x != 0:
		cnt += x % 10;
		x /= 10;
	return cnt

mi = -1;
for sx in xrange (1, 100):
	t = int (math.sqrt (4 * n + sx * sx));
	if t * t == 4 * n + sx * sx:
		tmpAns = (t - sx) / 2;
		if f(tmpAns) == sx and (mi == -1 or tmpAns < mi):
			mi = tmpAns;
print mi
		
