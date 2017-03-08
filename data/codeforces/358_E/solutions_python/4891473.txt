import sys
sys.setrecursionlimit(10**6)
def main():
    n, m = map(int, raw_input().split())
    a = [raw_input().split() for _ in xrange(n)]
    dd = [(1,0), (0,1)]
    od = 0
    D = [[[] for _ in xrange(m)] for _ in xrange(n)]
    done = [[False] * m for _ in xrange(n)]
    par = range(n * m)
    rank = [0] * (n * m)
    def find(x):
        if x == par[x]:
            return x
        else:
            par[x] = find(par[x])
            return par[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x == y: return
        if rank[x] < rank[y]:
            par[y] = x
        else:
            par[x] = y
            if rank[x] == rank[y]:
                rank[x] += 1
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] == '0': continue
            deg = 0
            for d in dd:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < n and 0 <= nj < m and a[ni][nj] == '1':
                    deg += 1
                    D[i][j].append(d)
                    union(i * m + j, ni * m + nj)
                ni, nj = i - d[0], j - d[1]
                if 0 <= ni < n and 0 <= nj < m and a[ni][nj] == '1':
                    deg += 1
            if deg % 2:
                od += 1 
    if od > 2:
        print -1
        return
    deg = 0
    S = set()
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] == '0': continue
            deg += 1
            S.add(find(i * m + j))
    if deg == 1 or len(S) != 1:
        print -1
        return
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x%y)
    p = 0
    for i in xrange(n):
        for j in xrange(m):
            if a[i][j] == '0' or done[i][j]: continue
            for d in D[i][j]:
                t = 1
                while 1:
                    ni, nj = i + t * d[0], j + t * d[1]
                    if 0 <= ni < n and 0 <= nj < m and a[ni][nj] == '1' and [d] == D[ni][nj]:
                        pass
                    else:
                        break
                    done[ni][nj] = 1
                    t += 1
                p = gcd(t, p)
    if p == 1:
        print -1
        return
    for i in xrange(2, p+1):
        if p % i == 0:
            print i,
main()
