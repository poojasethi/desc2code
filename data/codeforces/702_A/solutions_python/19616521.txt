n=int(raw_input())
integers=raw_input()
integers=map(int,integers.split(" "))
incrLen=1
incrList=[incrLen]
for i in xrange(1,n):
	if integers[i-1]<integers[i]:
		incrLen+=1
		incrList.append(incrLen)
	else:
		incrLen=1;

def max(x,y):
	if x>y:
		return x
	else:
		return y
answer=reduce(max,incrList)
print answer
