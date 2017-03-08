n = int (raw_input ())
count = 0
k = pow (n, 2)
for j in range (k / 2) :
	print j + 1,
	print k - j,
	count += 2
	if count == n :
		count = 0
		print
