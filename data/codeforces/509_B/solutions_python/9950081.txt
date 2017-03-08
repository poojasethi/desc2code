n,k = map(int,raw_input().split())
a = map(int,raw_input().split())
p = [sorted([i%k+1 for i in xrange(ai)]) for ai in a]
c = [[p[i].count(j+1) for j in xrange(k)] for i in xrange(n)]
for i in xrange(n):
    for j in xrange(i+1,n):
        if max(abs(c[i][x]-c[j][x]) for x in xrange(k)) > 1:
            print "NO"
            exit()
print "YES"
for pi in p: print " ".join(map(str,pi))
