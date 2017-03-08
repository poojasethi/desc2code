n = input()
for i in xrange(n):
	s = raw_input()
	a = s[-5:] == "lala."
	b = s[:5] == "miao."
	if (a==1 and b==0):
		print "Freda's"
	elif (b==1 and a==0):
		print "Rainbow's"
	else:
		print "OMG>.< I don't know!"