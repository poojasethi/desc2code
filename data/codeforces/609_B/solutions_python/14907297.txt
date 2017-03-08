from collections import Counter
n,m=map(int,raw_input().split())
a=Counter(map(int,raw_input().split()))
ans=0
for x in a:
    n-=a[x]
    ans+=a[x]*n
print ans
