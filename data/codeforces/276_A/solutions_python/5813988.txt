n,k=map(int,raw_input().split())
p=-10e10
for i in range(n):
    f,t=map(int,raw_input().split())
    p=max(p,f-max(0,t-k));
print p