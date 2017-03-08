from collections import defaultdict
n = int(raw_input())

l = defaultdict(int)
r = defaultdict(int)
for _ in xrange(n):
    a, b = map(int, raw_input().split())
    # \ is b - a
    l[b - a] += 1
    # / is b + a
    r[a + b] += 1

ans = 0

for k, v in l.iteritems():
    ans += v * (v - 1) / 2

for k, v in r.iteritems():
    ans += v * (v - 1) / 2

print ans
