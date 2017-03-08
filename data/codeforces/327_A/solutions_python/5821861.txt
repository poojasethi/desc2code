n=input()
s=map(int,raw_input().split())
k=0
for i in range(n):
    for j in range(i+1,n+1):
        k=max(k,(s[:i]+s[j:]).count(1)+s[i:j].count(0))
print k