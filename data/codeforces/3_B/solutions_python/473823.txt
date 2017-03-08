n, v = map(int, raw_input().split())

a = [[], []]
for i in xrange(n):
    t, p = map(int, raw_input().split())
    a[t-1].append( (p, str(i+1)) )

k, kn = zip(*sorted(a[0], reverse=True)) if a[0] else ((), ())
c, cn = zip(*sorted(a[1], reverse=True)) if a[1] else ((), ())

k = [0] + list(k)
c = [0] + list(c)

for i in xrange(1, len(k)):
    k[i] += k[i-1]
for i in xrange(1, len(c)):
    c[i] += c[i-1]

s, q, w = 0, 0, 0
for i in xrange(len(c)):
    j = min(v - 2*i, len(k)-1)
    if j < 0: break
    x = c[i] + k[j]
    if x <= s: break
    s, q, w = x, i, j

print s
print " ".join(cn[:q] + kn[:w])
