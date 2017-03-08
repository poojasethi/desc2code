n=int(raw_input())
a=map(int,raw_input().split())
l=1
m=1
if n==1:
	print 1
	exit()
for i in xrange(n-1):
	if a[i]<a[i+1]:
		l+=1
		m=max(m,l)
	else:
		l=1
print m	
