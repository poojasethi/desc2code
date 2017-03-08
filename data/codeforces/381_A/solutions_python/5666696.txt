n = input();
a = map(int, raw_input().split());
ans, ans2 = 0, 0;
f = 1;
lf, rgt = 0, n-1;
while lf <= rgt:
	if a[lf] > a[rgt]:
		if f % 2:
			ans += a[lf];
		else:
			ans2 += a[lf];
		lf += 1;
	else:
		if f % 2:
			ans += a[rgt];
		else:
			ans2 += a[rgt];
		rgt -=1;
	f += 1;
print ans, ans2
