n,k = map(int,raw_input().split())
l = [0]*n
opentw = 0
for i in xrange(k):
	c = str(raw_input()).split()
	if c[0] == "CLICK":
		x = int(c[1])-1
		if l[x] == 0:
			l[x] = 1
			opentw += 1
		else:
			l[x] = 0
			opentw -= 1
	elif c[0] == "CLOSEALL":
		l = [0]*n
		opentw = 0
	print opentw