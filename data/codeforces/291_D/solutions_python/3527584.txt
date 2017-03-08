
t = raw_input()
t = t.split(' ')
n = int(t[0])
k = int(t[1])
A = [2 for i in xrange(n)]
A[n - 1] = 0
if n > 1:A[n - 2] = 1


def get(x):
    l = 0
    r = n
    while l < r:
        mid = (l + r) >> 1
        if A[mid] <= x:
            r = mid
        else :
            l = mid + 1
    return r

import sys
if n == 1:
    print '1'
else:
    for i in xrange(n - 2):
        sys.stdout.write(str(n - 1) + ' ')
    sys.stdout.write(str(n) + ' ' + str(n) + '\n')

for _ in xrange(k - 1):
    C = [0 for i in xrange(n)]
    for i in xrange(n):
        if A[i] < n - (i + 1):
            for j in xrange(get(n - i - 1 - A[i]), n, 1):
                if A[j] + A[i] <= n - (i + 1):
                    C[i] = A[j]
                    sys.stdout.write(str(j + 1) + ' ')
                    break
        else:
            sys.stdout.write(str(n) + ' ')
    for i in xrange(n):
        A[i] += C[i]
    print ''


