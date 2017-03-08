n = int(raw_input())

if n >= 4:
	print n
	print ' '.join(map(str, range(2, n+1, 2)+range(1, n+1, 2)))
elif n == 3:
	print 2
	print 1, 3
else:
	print 1
	print 1

