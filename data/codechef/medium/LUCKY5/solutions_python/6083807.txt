t=input()
while t:
	t-=1
	n=raw_input().strip()
	print len(n)-n.count('4')-n.count('7')