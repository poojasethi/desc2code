#raw_input split

n = int(raw_input())

_ = map(int, raw_input().split())

A = []
for ind, val in enumerate(_):
    A.append((val, ind+1))

from StringIO import StringIO
s = StringIO()
A.sort()

flag = 0
for i in xrange(n-1):
    if A[i][0] == A[i+1][0]:
        flag += 1
        for x in A[:i]:
            print >>s, x[1],
        print >>s, A[i+1][1], A[i][1],
        for x in A[i+2:]:
            print >>s, x[1],
        print >>s

        if flag == 1:
            for x in A[:i]:
                print >>s, x[1],
            print >>s, A[i][1], A[i+1][1],
            for x in A[i+2:]:
                print >>s, x[1],
            print >>s
        elif flag == 2:
            break

if flag == 2:
    print 'YES'
    print s.getvalue()
else:
    print 'NO'
