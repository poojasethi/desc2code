
n = int(raw_input())

A = [ int(_) for _ in raw_input().split() ]

if n < 3:
  print n
  exit()

b = [0] * n

b[1] = b[0] = 1

for i in range(2, n):
  if A[i] == A[i-1] + A[i-2]:
    b[i] = 1

cnt = 0

ba= 0
ob = 0
for i in xrange(2, n):
  ba += b[i]
  if ba == ob:
    ba = 0
    ob = 0
  if ba > cnt:
    cnt = ba
  ob = ba

print cnt + 2
