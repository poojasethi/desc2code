import math
import sys

def main():
  t, sx, sy, ex, ey = map(int, raw_input().split())
  winds = raw_input()
  time = 0
  for c in winds:
    if sx == ex and sy == ey:
      print time
      return
    time += 1
    if c == 'S':
      if sy > ey:
        sy -= 1
    if c == 'N':
      if sy < ey:
        sy += 1
    if c == 'E':
      if sx < ex:
        sx += 1
    if c == 'W':
      if sx > ex:
        sx -= 1
  if sx == ex and sy == ey:
    print time
    return
  print -1

if __name__ == '__main__':
  main()
