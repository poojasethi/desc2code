n = input()
a = [int(x) for x in raw_input().split()]
l = len(a)
res = 0
t1 = True
p = 0
for x in range(0,l):
	if a[x] == x:
		res+=1
		p+=1
	elif t1 == True and a[a[x]] == x:
		t1 = False
		res+=2  	
if res == p and res < l:
	res+=1
	
print(res)						
				
