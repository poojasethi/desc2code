for _ in xrange(input()):
	a=raw_input()
	print a[0]+str(len(a)-2)+a[-1] if len(a)>10 else a