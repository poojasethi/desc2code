s = raw_input()
t = raw_input()
n = len(s)
d = sum(s[i] != t[i] for i in xrange(n))
if d % 2 == 1:
    print "impossible"
    exit()

d /= 2
p = ""
for i in xrange(n):
    if s[i] == t[i]:
        p += s[i]
    else:
        if d > 0:
            p += s[i]
            d -= 1
        else:
            p += t[i]
print p
