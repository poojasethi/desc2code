n=input()
c = {}
while n:
	s=raw_input()
	try:
		c[s]+=1
	except:
		c[s]=1
	n-=1
res = 0	
for x in c:
	if c[x]>res:
		res=c[x]
print(res)		
