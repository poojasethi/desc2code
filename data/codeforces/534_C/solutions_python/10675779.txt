n, A = map(int, raw_input().split())
d = map(int, raw_input().split())
s = sum(d)

ans = [0]*n
for i in xrange(n):
    if d[i]+n-1 > A:
        ans[i] += d[i]+n-1-A
    if s-d[i]+1 < A:
        ans[i] += A-(s-d[i]+1)

print " ".join(map(str, ans))
