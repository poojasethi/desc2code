n,m=map(int,raw_input().split())
a=[0]*(n+2)
#print a
for i in range(m):
	left,right=map(int,raw_input().split())
	a[left]+=1
	a[right+1]-=1
for j in range(1,n+1):
	a[j]+=a[j-1]
a=a[:n+1]
a.sort()
#print a
print a[(n/2)+1]
