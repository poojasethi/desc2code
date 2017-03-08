ms = [int(x) for x in raw_input().split()]
m = ms[0]
s = ms[1]

temps = s

maior = [0 for x in range(m)]
menor = [0 for x in range(m)]

if (s==0 and m>1) or s>m*9:
	print "-1 -1"
else:
	for i in range(m):
		if temps>9:
			maior[i]=9
			temps-=9
		else:
			maior[i]=temps
			break
	temps = s
	
	for i in range(m-1,-1,-1):
		if temps>9:
			menor[i]=9
			temps-=9
		else:
			if i!=0:
				menor[0]=1
				if temps!=1:
					menor[i]=temps-1
				break
			else:
				menor[i]=temps
			
	print ''.join([str(x) for x in menor]),''.join([str(x) for x in maior])
