m = int(raw_input())
q = map(int, raw_input().split())
n = int(raw_input())
a = map(int, raw_input().split())
mi = min(q)
a.sort()
a.reverse()
ans = sum(a)
for i in xrange(n):
    if (i % (mi+2) >= mi):
        ans -= a[i]
print ans

