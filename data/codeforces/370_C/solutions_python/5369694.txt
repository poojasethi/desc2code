n, m = [ int(_) for _ in raw_input().split() ]

A = [ int(_) for _ in raw_input().split() ]
A.sort()

mm = 1
cn = 1
for i in xrange(1, m+1, 1):
  t = A.count(i)
  if t > cn:
    mm = i
    cn = t

print n - max(0,   cn - (n - cn) )

for i in xrange(n):
  print A[(i+cn) % n], A[i]
