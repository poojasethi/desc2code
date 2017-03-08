n=input()
d=raw_input()
p=map(int,raw_input().split())
mini=float('inf')

for i in range(len(p)-1):
    j=i+1
    if d[i]=='R' and d[j]=='L':
        if p[j]-p[i]<mini:
            mini=p[j]-p[i]
print mini//2 if mini !=float('inf') else "-1"