import math
import sys

def main():
  m, t, r = map(int, raw_input().split())
  ghosts = map(int, raw_input().split())
  candles = []
  out = 0
  for ghost in ghosts:
    # Clear out candles that aren't going to make it
    while len(candles) > 0 and candles[0] + t <= ghost:
      candles.pop(0)

    need = r - len(candles)
    if need <= 0:
      continue

    if len(candles) == 0:
      last = ghost - t
    else:
      last = candles[-1]

    if last + need > ghost:
      print -1
      return

    for i in range(need - 1, -1, -1):
      candles.append(ghost - i)
    out += need
  print out

if __name__ == '__main__':
  main()
