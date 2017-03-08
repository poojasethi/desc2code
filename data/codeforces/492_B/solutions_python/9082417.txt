n,l = map(int,raw_input().split())
a = sorted(map(int,raw_input().split()))
k = max(l - a[-1],a[0])
for i in xrange(0,n-1):
    if(a[i+1] - a[i] > 2 * k):
        k = (a[i+1] - a[i]) / 2.0
print(k)
