n = input()
a = map(int, raw_input().split())
ans = sum(a)
for i in xrange(3, n):
    if n % i: continue
    s = n / i
    for j in xrange(s):
        ans = max(ans, sum(a[x] for x in xrange(j, n, s)))
print ans