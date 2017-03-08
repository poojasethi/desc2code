import math
import sys

def main():
  n, r, avg = map(int, raw_input().split())
  tests = []
  current_average = 0
  for i in range(n):
    a, b = map(int, raw_input().split())
    current_average += a
    tests.append([b, a])
  index = 0
  tests.sort()
  essays = 0
  while current_average < avg * n:
    b, a = tests[index]
    index += 1
    gaining = r - a
    if current_average + gaining >= avg * n:
      need_to_do = avg * n - current_average
      current_average += need_to_do
      essays += need_to_do * b
    else:
      current_average += gaining
      essays += gaining * b
  print essays


if __name__ == '__main__':
  main()
