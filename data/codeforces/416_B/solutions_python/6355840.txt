m, n = map(int, raw_input().split())
s = []
for i in xrange(m):
	a = map(int, raw_input().split())
	tmp = [0] * n;
	if i == 0:
		for j in xrange(n):
			tmp[j] = (0 if j == 0 else tmp[j-1]) + a[j];
		s.append(tmp);
		continue; 
	for j in xrange(n):
		if j == 0:
			tmp[j] = s[i-1][0] + a[0];
			continue;
		tmp[j] = a[j] + max(s[i-1][j], tmp[j-1]);
	s.append(tmp);

for i in xrange(m):
	print s[i][n-1],

