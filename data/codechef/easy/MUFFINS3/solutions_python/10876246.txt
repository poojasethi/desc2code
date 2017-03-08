t = int(raw_input())
for ii in range(t):
	i = int(raw_input())
	if i == 1  :
		print 1
	elif i == 2 :
		print 2
	elif i%2 == 0 :
		print (i/2 +1)
	else :
		print ( (i+1)/2)