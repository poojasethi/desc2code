n = int(raw_input())
if   n <= 2:
    print 1
    print 1
elif n == 3:
    print 2
    print 1,3
elif n == 4:
    print 4
    print 3,1,4,2,
else:
    print n
    for i in xrange(0,n,2):
        print i+1,
    for i in xrange(1,n,2):
        print i+1,
    print
