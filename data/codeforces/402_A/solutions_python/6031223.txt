k,a,b,v = [int(x) for x in raw_input().split()]
res = 0
while a>0:
	res+=1
	if b>=k:
		a = a- k*v
		b=b-(k-1)
	elif b>0:
		a = a - (b+1)*v
		b = 0;
	else:
		a = a-v
print(res)			
