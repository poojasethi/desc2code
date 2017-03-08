s = raw_input()
def check(s, i, l):
    a = list(s)
    a.insert(i,l)
    if a==a[::-1]:
        print ''.join(a)
        exit()
n = len(s)
for i in xrange(n):
    check(s, i, 'y')
    check(s, i, s[n-1-i])
    check(s, n-i, s[i])
print 'NA'
