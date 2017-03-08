import math
import sys

def main():
  n, m, s, f = map(int, raw_input().split())
  t = 1
  xenias = []
  for i in range(m):
    next_t, l, r = map(int, raw_input().split())
    xenias.append((next_t, l, r))
  index = 0
  current_spy = s
  if f > s:
    d = 'R'
    next_spy = s + 1
  else:
    d = 'L'
    next_spy = s - 1
  out = ''
  while current_spy != f:
    if index < len(xenias):
      next_t, l, r = xenias[index]
    else:
      next_t = -1
    if next_t == t:
      if current_spy >= l and current_spy <= r or next_spy >= l and next_spy <= r:
        out += 'X'
      else:
        out += d
        if d == 'R':
          current_spy, next_spy = next_spy, next_spy + 1
        else:
          current_spy, next_spy = next_spy, next_spy - 1
      index += 1
    else:
      out += d
      if d == 'R':
        current_spy, next_spy = next_spy, next_spy + 1
      else:
        current_spy, next_spy = next_spy, next_spy - 1
    t += 1
  print out


if __name__ == '__main__':
  main()
