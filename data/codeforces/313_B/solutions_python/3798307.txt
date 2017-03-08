s = raw_input()
l = len(s)
num = [0]

for x in range(0,l-1):
	if(s[x] == s[x+1]):
		num.append(num[x] + 1)
	else:
		num.append(num[x]+0)
m = input()
for x in range(0,m):
	l,r = [int(x) for x in raw_input().split()]
	
	print(num[r-1] - num[l-1]) 		
	
