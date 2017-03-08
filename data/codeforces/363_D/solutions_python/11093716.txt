import math
import sys

def check(boys, bikes, k, a):
  if k > len(boys):
    return False
  for i in range(k):
    if boys[k - i - 1] >= bikes[i]:
      continue
    if boys[k - i - 1] + a < bikes[i]:
      return False
    a -= bikes[i] - boys[k - i - 1]
  return True

def get_total(boys, bikes, k, a):
  out = 0
  for i in range(k):
    if boys[k - i - 1] >= bikes[i]:
      out += bikes[i]
      continue
    if boys[k - i - 1] + a < bikes[i]:
      return False
    out += boys[k - i - 1]
    a -= bikes[i] - boys[k - i - 1]
  return max(out - a, 0)

def main():
  n, m, a = map(int, raw_input().split())
  boys = map(int, raw_input().split())
  boys.sort(reverse = True)
  bikes = map(int, raw_input().split())
  bikes.sort()
  low = 0
  high = len(bikes)
  best = 0
  while low <= high:
    mid = low + (high - low) / 2
    if check(boys, bikes, mid, a):
      if mid > best:
        best = mid
      low = mid + 1
    else:
      high = mid - 1
  print best, get_total(boys, bikes, best, a)


if __name__ == '__main__':
  main()
