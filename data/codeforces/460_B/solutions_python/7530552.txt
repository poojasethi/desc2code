def digitsum(x):
	return sum(map(int,str(x)))



a,b,c=map(int,raw_input().split(" "))
k=0
lst=[]
for i in range(1,82):
	tmp=b*(i**a)+c
	if tmp<0:
		continue
	if(digitsum(tmp)==i):
		if (tmp<1000000000) and (tmp>0):
			k+=1
			lst.append(tmp)
sorted(lst)
print len(lst)
for i in lst:
	print i,
