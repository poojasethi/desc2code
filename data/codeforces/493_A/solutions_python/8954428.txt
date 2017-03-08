import math
import sys

def main():
  home = raw_input()
  away = raw_input()
  n = int(raw_input())
  cards = {}
  seen = {}
  for i in range(n):
    params = raw_input().split()
    t = int(params[0])
    place = params[1]
    number = int(params[2])
    kind = params[3]
    key = place + str(number)
    if kind == 'r' and key not in seen:
      seen[key] = True
      if place == 'h':
        print home, number, t
      else:
        print away, number, t
    else:
      if key in cards and key not in seen:
        seen[key] = True
        if place == 'h':
          print home, number, t
        else:
          print away, number, t
      else:
        cards[key] = True



if __name__ == '__main__':
  main()
