n = input()

if n <= 3:
	print "NO"

elif n % 2 == 0:
	print "YES"	
	print "4 * 3 = 12"
	print "12 * 1 = 12"
	print "12 * 2 = 24"
	for i in range(5,n,2):
		print "%d - %d = 1" % (i+1, i)
		print "24 * 1 = 24"
	
else:
	print "YES"
	print "2 - 1 = 1"
	print "1 + 3 = 4"
	print "4 * 5 = 20"
	print "20 + 4 = 24"
	for i in range(6,n,2):
		print "%d - %d = 1" % (i+1, i)
		print "24 * 1 = 24"
