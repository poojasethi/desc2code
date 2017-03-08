for i in range(int(raw_input())):
	for j in range(int(raw_input())):
		i,n,q = map(int,raw_input().split())
		if n % 2 == 0:
			print n/2
		else:
			if i == q:
				print n/2
			else:
				print n/2 + 1
