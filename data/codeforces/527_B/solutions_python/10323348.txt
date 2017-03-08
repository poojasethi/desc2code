
def solve():
	n = input()
	s = raw_input()
	t = raw_input()
	hd = 0
	mydict = {}
	udict = {}
	for i in xrange(n):
		if s[i] != t[i]:
			mydict[s[i]+t[i]] = i+1
			udict[s[i]] = i+1
			hd += 1
	toSubtract = 0
	firstIdx = -1
	secondIdx = -1
	#print udict
	for i in xrange(n):
		if s[i] != t[i]:
			tmp = mydict.get(t[i]+s[i], None)
			if tmp:
				toSubtract = 2
				firstIdx = i+1
				secondIdx = tmp
				break

	if toSubtract == 0:
		for i in xrange(n):
			if s[i] != t[i]:
				tmp = udict.get(t[i], None)
				if tmp:
					toSubtract = 1
					firstIdx = i+1
					secondIdx = tmp
					break
		if toSubtract == 0:
			print hd
			print firstIdx, secondIdx
		else:
			print hd - toSubtract
			print firstIdx, secondIdx

	else:
		print hd - toSubtract
		print firstIdx, secondIdx
solve()
