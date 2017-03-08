for i in range(int(raw_input())):
	n=int(raw_input())-1
	p,d=1,1
	for k in range(2,n+1):
		p, d = p * (n + k), d * k
                if  p % d == 0:
           	 p, d = p / d, 1
        p, d = p / d, 1
	print int(p)%10000