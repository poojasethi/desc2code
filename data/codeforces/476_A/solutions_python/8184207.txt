# raw_input, split

n, m = map(int, raw_input().split())

for i in xrange((n+1)/2, n+1):
  if i % m == 0:
    print i
    exit(0)

print -1
