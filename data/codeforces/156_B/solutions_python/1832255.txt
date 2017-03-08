from math import *
n,m=map(int,raw_input().split())
r=range(0,n)
s=map(int,(raw_input() for _ in r))
p=len(filter(lambda i: i<0,s))
a,b=[0]*n,[0]*n
for i in r:
    if s[i]>0: a[s[i]-1]+=1
    else: b[-s[i]-1]+=1
d=map(lambda i: a[i]+p-b[i],r)
k=len(filter(lambda i: i==m, d))
for i in r: print ['Truth','Lie','Not defined'][(d[abs(s[i])-1]==m)!=(s[i]>0) if k==1 else (2 if d[abs(s[i])-1]==m else s[i]>0)]
