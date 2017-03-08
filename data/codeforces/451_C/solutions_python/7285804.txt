T = int(raw_input())
for _ in range(T):
    n, k, d1, d2 = map(int, raw_input().split())
    if n % 3 != 0:
	flag = False
    else :
	m = n / 3
	flag = False
	def test(x):
	    return x >= 0 and x <= m
	if (k-d1-d2) % 3 == 0:
	    t = (k-d1-d2) / 3
	    if test(t) and test(t+d1) and test(t+d2):
		flag = True
        if (k-d1+d2) % 3 == 0:
	    t = (k-d1+d2) / 3
	    if test(t) and test(t+d1) and test(t-d2):
		flag = True
	if (k+d1-d2) % 3 == 0:
	    t = (k+d1-d2) / 3
	    if test(t) and test(t-d1) and test(t+d2):
		flag = True
        if (k+d1+d2) % 3 == 0:
	    t = (k+d1+d2) / 3
	    if test(t) and test(t-d1) and test(t-d2):
		flag = True
    if flag:
	print 'yes'
    else:
	print 'no'

		

		
	    
	    
	
	    

	    
	    
