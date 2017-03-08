# coding = utf-8
I = lambda:map(int,raw_input().split())
n,k = I()
a = I()
if k>n:
	print '-1'
else:
	a.sort()
	print str(a[n-k]),str(0)