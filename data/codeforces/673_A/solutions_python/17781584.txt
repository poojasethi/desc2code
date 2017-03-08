n=input()
arr=list()
arr=(raw_input().split(' '))
for i in range(0,n):
	arr[i]=int(arr[i])
c=0
flag=0
for x in range(0,91):
	if c>15:
		flag=1
		ans=x
		break
	elif x in arr:
		c=0
	c+=1
if flag==1:
	print ans-1
else:
	print 90
