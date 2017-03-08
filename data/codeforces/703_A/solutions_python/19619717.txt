
tt = int(raw_input())
M = 0
C = 0
for i in xrange(tt):
	m, c = map(int, raw_input().split())
	if m > c:
		M += 1

	elif m < c:
		C += 1

if M > C:
	print('Mishka')

elif M < C:
	print('Chris')		

else:
	print('Friendship is magic!^^')	