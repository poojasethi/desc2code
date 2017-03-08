n, l = map(int, raw_input().split())
d, lec = dict(raw_input().split() for _ in xrange(0, l)), raw_input().split()
t = lambda w: w if len(w) <= len(d[w]) else d[w]
print ' '.join(map(t, lec))
