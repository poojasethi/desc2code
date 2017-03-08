n = int(input())
if n%2 == 1:
	print 0
else:
	n=n/2
	print (n-1-int(not n%2))/2

