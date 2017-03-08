import sys
t=int(sys.stdin.readline())
while t!=0:
    n=int(sys.stdin.readline())
    f=1
    for i in range (1,n+1):
        f=f*i
    f=str(f)
    c=0
    l=len(f)-1
    while l>=0:
        if f[l]=='0':
            c+=1
            l-=1
        else:
            break
    print c
    t-=1
