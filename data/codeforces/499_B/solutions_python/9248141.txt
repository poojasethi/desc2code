n, m = map(int, raw_input().split())

d = {}
for i in xrange(m):
  a, b = raw_input().split()
  if len(b) < len(a):
    d[a] = b
  else:
    d[a] = a


s = raw_input().split()

for w in s:
  print d[w],
