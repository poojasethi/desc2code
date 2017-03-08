class pt(object):
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  def __sub__(self, other):
    return pt(self.x-other.x, self.y-other.y)

  def __mod__(self, other):
    return self.x * other.y - self.y * other.x

T = []
ini = 0
fin = 0

def add(x, y):
  p = pt(x, y)
  global T, fin
  while fin - ini >= 2 and\
      (p-T[fin-1]) % (p-T[fin-2]) <= 0:
    fin -= 1
  T[fin] = p
  fin += 1

def remove(x):
  global T, ini
  while fin - ini >= 2 and\
      T[ini].x*x + T[ini].y > T[ini+1].x*x + T[ini+1].y:
        ini += 1

n = int(raw_input())
T = [pt()] * n
A = [int(x) for x in raw_input().split()]
B = [int(x) for x in raw_input().split()]

res_a = 0

for i in xrange(1, n):
  add(B[i-1], res_a)
  remove(A[i])
  res = T[ini].x*A[i] + T[ini].y
  res_a = res

print(res)
