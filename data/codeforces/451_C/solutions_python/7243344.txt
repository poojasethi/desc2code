t = int(input());
while t > 0:
	t -= 1;
	n, k, d1, d2 = map(long, raw_input().split());
	n -= k;
	flag = 0;
	if n-d2-2*d1 >= 0 and (n-d2-2*d1) % 3 == 0 and 2*d2+d1<=k and (k-2*d2-d1)%3==0:
		flag = 1;
	elif d2>=d1 and n-d1-d2 >= 0 and (n-d1-d2) % 3 == 0 and 2*d2-d1<=k and (k-2*d2+d1) % 3== 0:
		flag = 1;
	elif d1 >= d2 and n+d2-2*d1>=0 and (n+d2-2*d1)%3==0 and (k-d1-d2)%3==0 and d1+d2<=k:
		flag = 1;
	elif d1>=d2 and n-d2-d1>=0 and (n-d2-d1)%3==0 and d1*2-d2<=k and (k-d1*2+d2) %3==0:
		flag = 1;
	elif d2>=d1 and d2+d1<=k and n+d1-2*d2>=0 and (n+d1-2*d2)%3==0 and(k-d1-d2)%3==0:
		flag = 1;
	elif d1+2*d2<=n and (n-d1-2*d2)%3==0 and 2*d1+d2<=k and (k-2*d1-d2)%3==0:
		flag = 1
	print 'yes' if flag else 'no'
