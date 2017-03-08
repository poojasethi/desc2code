import sys
t=int(sys.stdin.readline())
while t!=0:
    n=int(sys.stdin.readline())
    a=map(int,sys.stdin.readline().split())
    s=sum(a)
    f=0
    for i in range(0,n):
        if a[i]!=0:
            f+=1
    if s<100:
        sys.stdout.write('NO\n')
    else:
        if s==100:
            sys.stdout.write('YES\n')
        else:
            if s-100<f:
                sys.stdout.write('YES\n')
            else:
                sys.stdout.write('NO\n')
    t-=1
