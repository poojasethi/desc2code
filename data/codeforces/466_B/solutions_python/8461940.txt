import math

def solve(n, a, b):
  if a * b >= 6 * n:
    print a * b
    print a, b
    return
  swapped = False
  if a > b:
    a, b = b, a
    swapped = True
  i = a
  best = 100000000000000000
  out_a = a
  out_b = b
  while i*i <= 6 *n:
    tmp_b = 6 *n / i;
    if tmp_b * i < 6 *n:
      tmp_b += 1
    if tmp_b < b:
      i += 1
      continue
    if tmp_b * i < best:
      best = tmp_b * i
      out_a = i
      out_b = tmp_b
    i += 1
  if swapped:
    out_a, out_b = out_b, out_a
  print best
  print out_a, out_b

n, a, b = map(int, raw_input().split())
solve(n, a, b)
