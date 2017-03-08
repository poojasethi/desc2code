N,a,ans=input(),map(lambda x:abs(int(x)),raw_input().split()),0
for i in xrange(0,N):
    x,y=0,0;
    for j in xrange(0,N):
        if a[j]<a[i]:
            if j<i:x+=1
            else:y+=1
    ans+=min(x,y)
print(ans)