n = int(raw_input())
orig = [ int(raw_input()) for x in xrange(n) ]

f = filter(lambda a : a > 0, orig)
s = map(lambda b : -1*b, filter(lambda a : a < 0, orig))

total = reduce(lambda x, y: x + y, orig)

if total > 0:
    print "first"
elif total < 0:
    print "second"
else:
    if f > s:
        print "first"
    elif s > f:
        print "second"
    else:
        print ("first" if orig[-1] > 0 else "second")

