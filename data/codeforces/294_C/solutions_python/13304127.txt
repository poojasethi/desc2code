MOD = 1000000007
c = [[1]*i for i in xrange(1,1002)]
for i in xrange(2, 1001):
    for j in xrange(1, i):
        c[i][j] = (c[i-1][j-1] + c[i-1][j]) % MOD
n,m =map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
k=n-m
ans =1
s=a[0]
p=a[0]
for i in xrange(1,m):
    q = a[i]
    d = q-p-1
    if d:
        ans = ans*pow(2,d-1,MOD)*c[k][d]%MOD
        k-=d
    p = q
ans = ans*c[k][s-1]%MOD
ans = ans*c[k-s+1][n-p]%MOD
print ans