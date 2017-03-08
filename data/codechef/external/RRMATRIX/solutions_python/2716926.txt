from fractions import gcd
def new_rrmatrix():
    for t in xrange(input()):
        n,m = map(int,raw_input().split())
        print 1+ gcd(n-1,m-1)
new_rrmatrix()
