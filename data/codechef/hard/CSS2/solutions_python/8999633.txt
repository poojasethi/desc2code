n,m = map(int,raw_input().split())
table = {}
for i in xrange(n):
	a,b,c,d = map(int,raw_input().split())
	try:
		if(table[(a,b)][1]<=d): table[(a,b)] = [c,d]
	except:
		table[(a,b)] = [c,d]
for i in xrange(m):
	a,b = map(int,raw_input().split())
	print table[(a,b)][0]