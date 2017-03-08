import math
import sys

def main():
  n = int(raw_input())
  first = map(lambda x: [int(x), 0], raw_input().split())
  m = int(raw_input())
  second = map(lambda x: [int(x), 1], raw_input().split())
  total = first + second
  total.sort()
  sum0 = 3 * n
  sum1 = 3 * m
  best = sum0 - sum1
  best_ratio = '{0}:{1}'.format(sum0, sum1)
  for p in total:
    if p[1] == 0:
      sum0 -= 1
    else:
      sum1 -= 1
    if sum0 - sum1 > best:
      best = sum0 - sum1
      best_ratio = '{0}:{1}'.format(sum0, sum1)
  print best_ratio

if __name__ == '__main__':
  main()
