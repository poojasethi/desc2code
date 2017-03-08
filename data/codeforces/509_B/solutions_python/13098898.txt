'''
Created on Sep 19, 2015

@author: sshadmin
'''
n,k = map(int,raw_input().strip().split())
a = map(int,raw_input().strip().split())
import sys
i=0
nc=True
sm=sum(a)
r=[]
for i in range(n):
    r.append([])

i=0
while sm!=0:
    if i == n :
        i = 0
    if i==0:
        if nc==True:
            if k==0:
                print "NO"
                sys.exit()
            k-=1
            nc=False
    if a[i]==0:
        nc=True
    else:
        a[i]-=1
        r[i].append(k+1)
        sm-=1
    i+=1
print "YES"
for i in range(n):
    print " ".join(map(str,r[i]))
    
    
    
    
