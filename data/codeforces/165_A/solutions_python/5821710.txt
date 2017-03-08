n=int(raw_input())
a=[map(int,raw_input().split()) for i in range(n)]
k=0
for i in range(n):
    r=l=u=d=0
    x,y=a[i][0],a[i][1]
    for j in range(n):
        x1,y1=a[j][0],a[j][1]
        if x==x1 and y1>y: u+=1
        elif x==x1 and y1<y: d+=1
        elif y==y1 and x1>x: r+=1
        elif y==y1 and x1<x: l+=1
    if r>0 and l>0 and u>0 and d>0: k+=1
print k