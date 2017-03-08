import math
import sys

def main():
  k, b, n, t = map(int, raw_input().split())
  cur = 1
  out = 0
  while cur < t:
    cur = k * cur + b
    out += 1
  if cur == t:
    print max(0, n - out)
  else:
    print max(0, n - out + 1)

if __name__ == '__main__':
  main()
