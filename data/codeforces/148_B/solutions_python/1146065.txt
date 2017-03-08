vp = input();
vd = input();
t = input();
f = input();
c = input();
if vp >= vd:
	print 0
	exit()
a = 1.0 * vp * t * vd / (vd - vp);
ret = 0
while a<c:
	ret += 1
	a += vp * (f+a/vd)
	a = a * vd / (vd - vp)
print ret