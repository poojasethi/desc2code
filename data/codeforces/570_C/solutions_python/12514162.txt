n,m = [int(c) for c in raw_input().split()]
s = raw_input()
cnt = [0]*(len(s)+1)
ss=[]
res = 0
curr = 0
for x in range(0,len(s)):
	if s[x]=='.':
		curr+=1
	else:
		if curr>0:
			res+=(curr-1)	
		curr=0
	ss.append(s[x])
else:
	if curr>0:
			res+=(curr-1)	
	curr=0
	
	

while m:
	m-=1
	a,b = [c for c in raw_input().split()]
	a=int(a)-1
	if b =='.':
		if ss[a]!='.':
			if a>0:
				if ss[a-1] =='.':
					res+=1
			if a<n-1:
				if ss[a+1] =='.':
					res+=1
			ss[a]=b
		print(res)					
	else:
		if ss[a]=='.':
			if a>0:
				if ss[a-1] =='.':
					res-=1
			if a<n-1:
				if ss[a+1] =='.':
					res-=1
			ss[a]=b
		print(res)	


