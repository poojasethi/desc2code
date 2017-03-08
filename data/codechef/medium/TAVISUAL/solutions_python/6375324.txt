t = int (raw_input())
for  i in range (t) : 
	n , c , q = raw_input().split () 
	n = int (n)
	c= int (c)
	q = int (q)
	for j in range (q):
		l , r = raw_input ().split () 
		l = int (l)
		r = int (r)
		if (c < l or r<c):
			continue 
		c = (l+r -c)
	print c
	 