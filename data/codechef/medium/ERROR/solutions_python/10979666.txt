# your code goes here
t=int(raw_input())
while t>0:
	
	s=str(raw_input())
	
	
	f1=s.find('010')
	
	f2=s.find('101')
	
	
	if f1>-1 and f2>-1:
		print "Good"
	elif (f1 > -1 and f2== -1) or (f1==-1 and f2 > -1):
		print "Good"
	else: 
		print "Bad"	
		
	t=t-1