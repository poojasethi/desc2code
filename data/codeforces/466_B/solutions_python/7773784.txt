
n, a, b  = map(int ,raw_input().split())

aa = a
bb = b

a, b = max(a, b), min(a, b)
n*=6
if aa*bb>=n:
    print aa*bb
    print aa,bb
    exit(0)


import math
x = int(math.sqrt(n))+2

ans=n
xx=-1
for i in xrange(b, x):
    t = max((n+i-1)/i, a)*i - n
    if t < ans:
        ans = t
        xx = i
        if t==0:
            break

if aa>bb:
    print max(aa, (n+xx-1)/xx) * max(xx, bb)
    print max(aa, (n+xx-1)/xx) , max(xx, bb)
else:
    print max(aa, xx)*max(bb, ((n+xx-1)/xx))
    print max(aa, xx),max(bb, ((n+xx-1)/xx))
