n=int(raw_input())
a=map(int,raw_input().split())
a.sort()
ans=1
for i in a: 
	if ans<=i:
		ans+=1
print ans
