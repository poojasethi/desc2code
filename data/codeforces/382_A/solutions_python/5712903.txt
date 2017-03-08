a = raw_input()
b = raw_input()
m = (len(a)+len(b))/2
n = a.index('|')
if (len(a)+len(b))%2 and n <= m and n+len(b) >= m:
	print a[:n]+b[:m-n]+a[n:]+b[m-n:]
else:
	print "Impossible"
