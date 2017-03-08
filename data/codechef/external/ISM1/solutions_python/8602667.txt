t=input()
while t>0:
	b=[]
	a=raw_input().split()
	for i in range(len(a)):
		str=a[i]
		rev=str[::-1]
		b.append(rev)
	for i in range(len(b)):
		print b[i],
	print "\n"
	t=t-1