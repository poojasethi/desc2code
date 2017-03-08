t=int(raw_input())
maxx,maxy=-10**18,-10**18
minx=10**18
miny=10**18
for z in xrange(t):
    a,b=map(int,raw_input().split())
    maxx=max(maxx,a)
    minx=min(minx,a)
    maxy=max(maxy,b)
    miny=min(miny,b)
print (max(maxx-minx,maxy-miny))**2
