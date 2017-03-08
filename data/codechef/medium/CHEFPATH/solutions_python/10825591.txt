val=raw_input()
t=int(val)
for i in range(t):
	lens=list()
	stri=raw_input()
	lens=stri.split()
	n=int(lens[0])
	m=int(lens[1])
	if n%2==0 and m%2==1 and m!=1:
		print 'Yes'
	elif m%2==0 and n%2==1 and n!=1:
		print 'Yes'
	elif n%2==0 and m%2==0:
		print 'Yes'
	elif n%2==1 and m%2==1 and n!=1 and m!=1: 
		print 'No'
	elif (n==1 and m==2) or (m==1 and n==2): 
		print 'Yes'
	else:
		print 'No'