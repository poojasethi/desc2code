n = int(input());
a = [];
b = [];
for i in xrange(n):
	c, d = map(int, raw_input().split());
	a.append(c);
	b.append(d);
#print a;
#print b;
ans1 = ans2 = "1" * (n/2);
for i in xrange(n/2, n):
		if a[i] < b[n-i-1]:
			ans1 += "1";
		else:
			ans1 += "0";
		if b[i] < a[n-i-1]:
			ans2 += "1";
		else:
			ans2 += "0";
print ans1
print ans2;

