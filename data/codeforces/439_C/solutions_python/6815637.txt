n, k, p = map(int, raw_input().split());
a = map(int, raw_input().split());
b, c = [], [];
even, odd = 0, 0;
for i in xrange(n):
  if a[i] % 2 == 0:
  	even += 1
  	b.append(a[i]);
  else:
  	c.append(a[i]);
odd = n - even;
if odd < k-p or (odd-(k-p))/2+even < p or (odd-(k-p))%2:
	print "NO"
else:
	print "YES";
	for i in xrange(k-p-1):
	  print 1, c[i]
	if p == 0:
	  print n-(k-p-1),
	  for i in xrange(k-p-1, odd):
		print c[i],
	  for i in xrange(0, even):
		print b[i],
	else:
	 	if k != p:
	 		print 1, c[k-p-1]
		j = k - p;
		if even >= p and p:
			for i in xrange(p-1):
		  		print 1, b[i]
			left = n - (k-p) - (p-1)
			print left, 
			for i in xrange(k-p, odd):
		  		print c[i],
			for i in xrange(p-1, even):
				print b[i],
		elif even < p and p:
			for i in xrange(even):
				print 1, b[i]
			for i in xrange(p-even-1):
				print 2, c[j], c[j+1]
				j += 2
			left = n - even - j;
			print left, 
			for i in xrange(j, j+left):
				print c[i],





