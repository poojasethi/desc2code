a,b=(raw_input().split(' '))
a=int(a)
b=int(b)
arr=list()
arr=raw_input().split(' ')
count=list()
count.append(0)
for i in range(1,a):
	count.append(count[i-1]+i)
i=0
while i<a and count[i]<b:
	i+=1
i-=1

#print i
print arr[b-count[i]-1]