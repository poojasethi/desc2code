for i in range(input()):
	a = raw_input()
	print [a, a[0]+str(len(a)-2)+a[-1]][(len(a)>10)]