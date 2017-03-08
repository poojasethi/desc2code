def py_1():
	a = raw_input()
	b = list(a)
	blen = len(b)
	mini = -1
	c = int(b[-1])
	for i in xrange(blen):
		tmp = int(b[i])
		if tmp%2 == 0 and tmp < c:
			mini = i
			break
	if mini == -1:
		i = blen - 1
		while i >= 0:
			tmp = int(b[i])
			if tmp%2 == 0:
				mini = i
				break
			i -= 1
	if mini == -1:
		print mini
	else:
		tmp = b[-1]
		b[-1] = b[mini]
		b[mini] = tmp
		print ''.join(b)
py_1()
