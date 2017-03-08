import sys

n, m = map(int, sys.stdin.readline().split())

ok = 2*(m-1)

for i in xrange(n):
    s, f, t = map(int, sys.stdin.readline().split())

    if s == f:
        print t
    elif s < f:
        if t < s:
            print s-1+f-s
        else:
            tot = s-1
            while tot < t:
                tot += ok
            tot += f-s
            print tot
    else:
        if t < s:
            print s-1+2*(m-s)+s-f
        else:
            tot = s-1+2*(m-s)

            while tot < t:
                tot += ok
            tot += s-f
            print tot


