def solve(a,b):
    x,minx,ret=0,0,set()
    for i in xrange(len(a)):
        if x==minx:
            ret.add(i)
        elif x<minx:
            minx=x
            ret=set([i])
        x+=a[i]-b[i]
    return ret
f=lambda :map(int,raw_input().split())
n=input()
a,b=f(),f()
c,d=a[::-1],b[::-1]
d=d[1:]+d[:1]
ret=solve(a,b)|set([n-1-x for x in solve(c,d)])
ret=map(lambda x:x+1 ,ret)
print len(ret)
print " ".join(map(str,sorted(ret)))

