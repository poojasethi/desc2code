k,b,n,t=map(int,raw_input().split())
m=n
z=1
x = 1
while z<=t and m>=0:
    z+=(b-1)*x
    x*=k
    z+=x
    m-=1
print m+1