t = int(raw_input())
while t>0:
	t-=1
	string = raw_input()
	c = list(string)
	if c.count('X') == len(c):
		print len(c)-1
	elif c.count('Y') == len(c):
		print len(c)-1
	else:
		ans=0
		i=1
		while i<len(c):
			if c[i]==c[i-1]:
				ans+=1
			i+=1
		print ans