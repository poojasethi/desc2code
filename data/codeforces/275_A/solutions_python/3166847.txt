s = [[0] * 5 for _ in range(5)]
for i in range(3):
	for j, x in enumerate(map(int, raw_input().split())):
		s[i][j + 1] += x
		s[i + 1][j] += x
		s[i + 1][j + 1] += x
		s[i + 1][j + 2] += x
		s[i + 2][j + 1] += x
for i in range(3):
	print ''.join(map(str, [1 - x & 1 for x in s[i + 1][1 : 4]]))