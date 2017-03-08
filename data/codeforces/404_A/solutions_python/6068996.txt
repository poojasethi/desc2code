n = int(input())
string = []
cnt, cnt2 = 0, 0
for _ in xrange(n):
	tmp = raw_input();
	string.append(tmp)
a, b= string[0][0], string[0][1]
f = 1
for i in xrange(n):
	if a == b:
		f = 0
		break
	if string[i][i] != a or string[i][n-i-1] != a:
		f = 0
		break
	for j in xrange(n):
		if i == j or j == n - i - 1:
			continue
		if string[i][j] != b:
			f = 0;
			break;
	if f == 0:
		break
print "YES" if f else "NO"

