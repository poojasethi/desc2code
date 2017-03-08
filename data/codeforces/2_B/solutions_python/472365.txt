def solve(a, n, k):
    def count(x):
        r = 0
        while x > 0 and x % k == 0:
            x = x / k
            r += 1
        return r

    b = [map(count, r) for r in a]

    for i in xrange(1, n):
        b[0][i] += b[0][i-1]

    for j in xrange(1, n):
        b[j][0] += b[j-1][0]
        for i in xrange(1, n):
            b[j][i] += min(b[j][i-1], b[j-1][i])

    p, j, i = [], n-1, n-1
    while j > 0 and i > 0:
        if b[j-1][i] < b[j][i-1]:
            p += ['D']
            j -= 1
        else:    
            p += ['R']
            i -= 1
    p += ['D'*j, 'R'*i]
    return b[n-1][n-1], reversed(p)

n = int(raw_input())
a = [map(int, raw_input().split()) for i in xrange(n)]

rz = [any([x==0 for x in r]) for r in a]

v, p = min(solve(a, n, 2), solve(a, n, 5))
if v > 1 and any(rz):
    path = ['D']*n
    path[rz.index(True)] = 'R'*(n-1)
    v, p = 1, path

print v
print ''.join(p)
