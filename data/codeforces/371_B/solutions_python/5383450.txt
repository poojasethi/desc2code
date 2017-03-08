a, b = [int(_) for _ in raw_input().split()]


 
A = [0] * 3
B = [0] * 3


aa = 1
bb = 1

for i,x in enumerate ( [2,3,5] ):
  t = a
  while t % x == 0:
    aa *= x
    A[i] += 1
    t /= x

  t = b
  while t % x == 0:
    bb *= x
    B[i] += 1
    t /= x

if 1.0 * a / aa != 1.0 * b / bb:
  print -1
  exit()

cnt = 0
cnt += max(A[0], B[0]) - min(A[0], B[0])
cnt += max(A[1], B[1]) - min(A[1], B[1])
cnt += max(A[2], B[2]) - min(A[2], B[2])

print cnt
