a = int(raw_input())
b = int(raw_input())
n = a+b+1
if a == 0:
    print " ".join(map(str,range(n,0,-1)))
else:
    print " ".join(map(str,[1]+range(n-a+1,n+1)+range(n-a,1,-1)))
