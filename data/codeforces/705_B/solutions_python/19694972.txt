n = int(raw_input())

a = map(int, raw_input().split())

moves = 0
for i in xrange(len(a)):
	moves += a[i]-1
	if moves%2:
		print 1
	else:
		print 2