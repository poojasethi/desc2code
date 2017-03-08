n, k, d = map(int, raw_input().split())
l = []
for i in xrange(n):
    l += map(int, raw_input().split())
for i in l:
    if (i - l[0]) % d:
        print -1
        exit(0)
l.sort()
m = l[len(l) / 2]
k = 0
for i in l:
    k += abs(m - i) / d
print k