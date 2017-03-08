n  = int(raw_input())

A = [ None ] * n

for i in xrange(n):
  A[i] = [ int(_) for _ in raw_input().split() ]


for i in xrange(n):
  ans = "YES"
  for j in xrange(n):
    if i != j:
      flag = 0
      for x in A[j][1:]:
        if x not in A[i][1:]:
          flag = 1
          break
      if not flag:
        ans = "NO"
        break
  print ans
