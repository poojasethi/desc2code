N = input()
a = int(-2e9)
b = int(2e9)
for i in xrange(N):
	s = raw_input().split()
	s[1] = int(s[1])
	# print s
	if s[0] == '>':
		if s[2] == 'Y':
			a = max(a, s[1]+1)
		else:
			b = min(b, s[1])
	elif s[0] == '<':
		if s[2] == 'Y':
			b = min(b, s[1]-1)
		else:
			a = max(a, s[1])
	elif s[0] == '>=':
		if s[2] == 'Y':
			a = max(a, s[1])
		else:
			b = min(b, s[1]-1)
	else:
		if s[2] == 'Y':
			b = min(b, s[1])
		else:
			a = max(a, s[1]+1)
	# print a, b
if a <= b:
	print a
else:
	print 'Impossible'
