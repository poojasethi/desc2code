t = int(raw_input())
for i in xrange(1,t+1):
	s = str(raw_input())
	holes = 0
	for j in s:
		if j == 'A' or j == 'D' or j == 'O' or j == 'P' or j == 'Q' or j == 'R':
			holes += 1
		if j == 'B':
			holes += 2
	print holes