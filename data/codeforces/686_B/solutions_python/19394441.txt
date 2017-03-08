n=int(raw_input())
a=map(int,raw_input().split())
i=0
flag=1
while flag>0:
	flag=0
	l=102
	r=-102
	while(i<n-1):
		if a[i]>a[i+1]:
			l=min(l,i)
			r=max(r,i+1)
			a[i],a[i+1]=a[i+1],a[i]
			i+=2
			flag+=1
		else:
			if l!=102 and r!=-102:
				print l+1,r+1
				l=102
				r=-102
			i+=1
	i=0
	if l!=102 and r!=-102: print l+1,r+1


