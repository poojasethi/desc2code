import sys
t=int(sys.stdin.readline())
while t!=0:
    n=int(sys.stdin.readline())
    f=1
    for i in range (1,n+1):
        f=f*i
    print f
    t-=1
