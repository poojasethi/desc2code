t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    x=bin(n)[2:]
    x=len(x)-1
    x2=pow(2,x)
    ans=2*(n-x2)
    if ans==0:
        print x2
    else:
        print ans