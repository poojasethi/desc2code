n = input ();

if n % 2 == 0:
	for i in xrange (n / 2):
		print 2 * (i+1), 2 *i + 1,
else:
	print -1
		
