n = input()
a = [int(x) for x in raw_input().split()]
hashi = [0]*100001
prev = [0]*100001
visit1 = [False]*100001
visit2 = [False]*100001
valid = [1]*100001
res = 0
for x in range(0,n):
	if not visit1[a[x]] and not visit2[a[x]]:
		hashi[a[x]] = 0
		visit1[a[x]] = True
		prev[a[x]] = x
	elif not visit2[a[x]]:
		hashi[a[x]] = x - prev[a[x]]
		visit2[a[x]] = True
		prev[a[x]] = x
	else:
		if not hashi[a[x]] == x - prev[a[x]]:
			valid[a[x]] = 0
			prev[a[x]] = x	
		else:
			prev[a[x]] = x	
visit1 = [False]*100001					
for x in range(0,n):
	if valid[a[x]] and not visit1[a[x]]:
		res+=1
		visit1[a[x]] = True
print(res)	
visit1 = [False]*100001		
a.sort()
for x in range(0,n):
	if valid[a[x]] and not visit1[a[x]]:
		print(a[x]),
		print(hashi[a[x]])
		visit1[a[x]] = True
	
						  		
			  		
			  		
			  		
