n = input();
num = [raw_input() for i in xrange(n)];
ans = 0;
l = len(num[0]);
for i in xrange(l):
	f = 1;
	for j in xrange(1, n):
		if num[j][i] != num[0][i]:
			f = 0;
			break;
	if not f:
		break;
	ans = i + 1;
print ans 
