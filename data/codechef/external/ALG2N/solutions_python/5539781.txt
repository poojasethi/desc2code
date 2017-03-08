t=int(raw_input())
while t!=0:
    n=int(raw_input())
    n=str(2**n)
    s=0;
    for i in range(0,len(n)):
        s+=int(n[i])
    print s
    t-=1
