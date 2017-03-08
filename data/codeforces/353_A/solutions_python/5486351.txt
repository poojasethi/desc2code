n = input();

f = s1 = s2 = 0;
for i in range(n):
	x, y = map(int, raw_input().split());
	s1 += x;
	s2 += y;
	if (x + y) % 2:
		f = 1;
if s1 % 2 == 0 and s2 % 2 == 0:
	print 0;
elif (s1 + s2) % 2 == 1:
	print -1;
else:
	print 1 if f else -1;

