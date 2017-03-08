N=int(input())
D=[0]*N
for i in range(N-1):
    a,b=map(int,raw_input().split())
    a-=1;b-=1;
    D[a]+=1
    D[b]+=1
ans=N*(N-1)*(N-2)
ans/=6
ans-=(N-1)*(N-2)
for i in D:
    if i>=2:
        ans+=(i*(i-1))/2
print ans
