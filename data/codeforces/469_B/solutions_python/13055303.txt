'''
Created on Sep 16, 2015

@author: sshadmin
'''
p,q,l,r=map(int,raw_input().strip().split())
x,z=[],[]
for i in range(p):
    x.append(map(int,raw_input().strip().split()))
for i in range(q):
    z.append(map(int,raw_input().strip().split()))

c=0
for i in range(l,r+1):
    found=False
    for sz,ez in z:
        if found:
            break
        for sx,ex in x:
            if (sx >=sz+i and sx<=ez+i) or (sz+i >=sx and sz+i <=ex):
                c+=1
                found=True
                break
print c
        
    
    