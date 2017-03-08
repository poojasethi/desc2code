n=int(raw_input())
integers=map(int,raw_input().split(" "))
intdic={}

for i in xrange(0,n):
	intdic[i+1]=integers[i]

li=sorted(intdic.iteritems(),key=lambda d:d[1])

for j in xrange(0,n/2):
	print li[j][0],
	print li[n-1-j][0]