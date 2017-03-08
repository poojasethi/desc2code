def solve():
    n, m, X = map(int, raw_input().split())

    sh = []
    cc = []
    for j in xrange(n):
        for i, c in enumerate(raw_input().strip()):
            if c == 'S':
                sh += [(j, i)]
            else:
                cc += [(c, j, i)]

    l, u = set(), set()
    for c, j, i in cc:
        l.add(c)
        if sh and min([(i-si)**2 + (j-sj)**2 for sj, si in sh]) <= X*X:
            u.add(c.upper())

    q = int(raw_input())
    r = 0
    for c in raw_input().strip():
        if (c.lower() not in l) or (c.isupper() and not u):
            return -1
        if c.isupper() and (c not in u):
            r += 1
    return r

print solve()
