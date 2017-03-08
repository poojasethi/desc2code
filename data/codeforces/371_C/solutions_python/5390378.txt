s = raw_input()

n1, n2 , n3 = [ int(_) for _ in raw_input().split() ]
r1, r2 , r3 = [ int(_) for _ in raw_input().split() ]
r = int(raw_input())

a = s.count('B')
b = s.count('S')
c = s.count('C')

def cal(x):
  rr1 = (x * a - n1) * r1
  rr2 = (x * b - n2) * r2
  rr3 = (x * c - n3) * r3

  rr1 = max(rr1, 0)
  rr2 = max(rr2, 0)
  rr3 = max(rr3, 0)

  if rr1 + rr2 + rr3 <= r:
    return 1
  else:
    return 0


low = 0
hig = 10 ** 13

flag = 0

while  low < hig:
  if flag:break
  mid = (low + hig) >> 1
  if mid == low:
    flag = 1

  ret = cal(mid)
  if ret:
    low = mid
  else:
    hig = mid - 1

if cal(low+1):
  low += 1
print low
