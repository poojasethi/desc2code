import math
import sys

def main():
  n = int(raw_input())
  a = map(int, raw_input().split())
  out = 1
  last = a[0]
  current_size = 1
  for i in range(1, len(a)):
    if a[i] <= last:
      out = max(out, current_size)
      current_size = 0
    last = a[i]
    current_size += 1
  print max(out, current_size)


if __name__ == '__main__':
  main()
