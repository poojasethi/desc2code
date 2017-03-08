n=int(raw_input())
a=map(int,raw_input().split())
powers=[2**i for i in xrange(1,32)]
c=0
dic={}
for value in a:
	for pow2 in powers:
		if pow2>value:
			if pow2-value in dic:
				c+=dic[pow2-value]
	if value in dic:
		dic[value]+=1
	else:
		dic[value]=1
print c			