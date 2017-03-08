I=lambda:int(raw_input().split()[0])
n=I()
f=[]
for i in range(n):
    e=I()
    l,r=0,len(f)-1
    while l<=r:
        m = (l+r)/2
        if f[m] <= e: l=m+1
        else: r=m-1   
    if not f or e >= f[-1]: 
        f+=[e]
    else:
        f[l] = e
print n-len(f)