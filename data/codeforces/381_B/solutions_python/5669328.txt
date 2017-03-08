m = input();
a = [0] * 5005;
b = map(int, raw_input().split())
b = sorted(b);
c = []
for i in b:
	if a[i] < 2:
		a[i] += 1;
		c.append(i);
if a[c[-1]] == 2:
	a[c[-1]] -= 1;
	c = c[:-1];
print len(c);
#print c
#print a
d = []
for i in xrange(len(c)):
	if i != 0 and c[i] == c[i-1]:
		continue;
	d.append(c[i])
	a[c[i]] -= 1;
for i in xrange(len(c)-1, -1, -1):
	if a[c[i]] > 0:
		a[c[i]] -= 1;
		d.append(c[i]);
print ' '.join(map(str, d))
