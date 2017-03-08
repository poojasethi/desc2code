n=input()
m=map(int,raw_input().split())
avg=1.*sum(m)/len(m)
l,r=0,0
for x in m:
    d=x-avg
    if d<0:
        l+=int(-d)
    else:
        r+=int(d)
print max(r,l)
