import bisect
sqs=bytearray(raw_input())

l=0
i=0
cost=0
s=[]
while i < len(sqs):
    if sqs[i]==ord('('):
        l+=1
    elif sqs[i]==ord(')'):
        l-=1
    else:
        a,b=[int(j)for j in raw_input().split()]
        l-=1
        cost+=b
        sqs[i]=')'
        bisect.insort(s,(b-a,i))
    if l < 0:
        if len(s)==0:break
        v,ii=s.pop()
        cost-=v
        sqs[ii]='('
        l+=2
    i+=1

if l==0:
    print(cost)
    print(str(sqs))
else:
    print(-1)
    