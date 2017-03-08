t = int(raw_input())
for i in xrange(t):
	n = int(raw_input())
	s = str(raw_input())
	r = 0
	g = 0
	b = 0
	for j in s:
		if j == 'R':
			r += 1
		elif j == 'G':
			g += 1
		else:
			b += 1
	x = max(r,g,b)
	print n-x