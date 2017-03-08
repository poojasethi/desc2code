n, x0 = map(int, raw_input().split())

total = 0
amax = 0
bmax = 1000
sa = sb = False
for i in xrange(n):
    a, b = map(int, raw_input().split())

    if b < a:
        a, b = b, a

    if b < bmax:
        bmax = b
        #if b < x0:
        #    sb = True
    if a > amax:
        amax = a
        #if a
        #sa = True

if amax > bmax:# or sa and sb:
    print "-1"
elif x0 < amax:
    print amax - x0
elif x0 > bmax:
    print x0 - bmax
else:
    print "0"
    

        
