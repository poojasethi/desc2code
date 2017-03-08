t=raw_input()
t=int(t)
while t:
    t-=1
    n=raw_input()
    n=int(n)
    for i in xrange(1,n):
        j=i
        sum=i
        while j:
            sum+=j%10
            j/=10
        if sum==n:
            j=-1
            break
    if j!=-1:
        print "NONE"
    else:
        print i