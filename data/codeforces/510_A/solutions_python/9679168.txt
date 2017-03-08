n,m=map(int,raw_input().split())
k=1
for i in xrange(n):
	if i%2==1:
		if k%2==0:
			print "#"+"."*(m-1)
		else:
			print "."*(m-1)+"#"
		k+=1
	else:
		print "#"*m
