N = input()
print (N**2+1)/2
for i in xrange(N):
	print ''.join(['C' if not (i+j)%2 else '.' for j in xrange(N)])
