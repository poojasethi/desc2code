n = input()
l = [int(k) for k in raw_input().strip().split()]
l.sort()
if l[0] == l[-1]:
	print 0,(n*(n-1))/2
else:
	print l[-1]-l[0],(l.count(l[0])*l.count(l[-1]))