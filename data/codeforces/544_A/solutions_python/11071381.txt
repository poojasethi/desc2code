import sys

k = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
d = dict()
for x in xrange(len(s)):
    if s[x] in d:
        pass
    else:
        d[s[x]] = x
        if len(d) == k:
            break
if len(d) == k:
    print 'YES'
    ke = sorted(d.values())
    for i in xrange(len(ke)-1):
        print s[ke[i]:ke[i+1]]
    print s[ke[-1]:]
else:
    print 'NO'
