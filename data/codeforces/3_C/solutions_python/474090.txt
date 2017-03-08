p = ["first", "second"]

a = raw_input()
b = raw_input()
c = raw_input()

nx = (a+b+c).count('X')
no = (a+b+c).count('0')
d = nx - no

opts = [a, b, c, a[0]+b[1]+c[2], a[2]+b[1]+c[0]] + list(map("".join, zip(a, b, c)))
w = ("XXX" in opts) + 2*("000" in opts) - 1

if (d not in [0, 1]) or (w > 1) or d == w:
    print "illegal"
elif w >= 0:
    print "the %s player won" % p[w]
elif nx + no == 9:
    print "draw"
else:
    print p[d]
