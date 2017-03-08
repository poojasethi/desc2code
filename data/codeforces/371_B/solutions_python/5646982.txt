import sys

seent = {}

def vect(x, k):
  if (x in seent):
    return

  seent[x] = k
  if (x % 2 == 0):
    vect(x / 2, k + 1)
  if (x % 3 == 0):
    vect(x / 3, k + 1)
  if (x % 5 == 0):
    vect(x / 5, k + 1)

def orr(x, k):
  if (x in seent):
    if (seent[x] == -1):
      return -1
    else:
      return k + seent[x]

  seent[x] = -1

  mn = float("inf")
  if (x % 2 == 0):
    ret = orr(x / 2, k + 1)
    if (ret != -1):
      mn = min(ret, mn)

  if (x % 3 == 0):
    ret = orr(x / 3, k + 1)
    if (ret != -1):
      mn = min(ret, mn)

  if (x % 5 == 0):
    ret = orr(x / 5, k + 1)
    if (ret != -1):
      mn = min(ret, mn)
  
  if (mn == float("inf")):
    return -1
  return mn


a, b = [ int(x) for x in sys.stdin.readline().strip().split() ]
vect(a, 0)
print orr(b, 0)
