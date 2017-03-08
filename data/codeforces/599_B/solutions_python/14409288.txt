import sys
n, m = [int(x) for x in raw_input().split()]
f = [int(x) for x in raw_input().split()]
b = [int(x) for x in raw_input().split()]

h = {}
for i in range(n):
    if f[i] in h:
        h[f[i]] = None
    else:
        h[f[i]] = i

l = []
amb = False
for i in range(m):
    if b[i] in h:
        if h[b[i]] is None:
            amb = True
        else:
            l.append(h[b[i]]+1)
    else:
        print "Impossible"
        sys.exit()
if amb:
    print "Ambiguity"
else:
    print "Possible"
    for x in l: print x,

