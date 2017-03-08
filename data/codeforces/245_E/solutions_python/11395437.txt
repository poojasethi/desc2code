import math
import sys

def main():
  s = raw_input()
  top = 0
  bot = 0
  count = 0
  for i in range(len(s)):
    if s[i] == '+':
      count -= 1
    else:
      count += 1
    top = max(top, count)
    bot = min(bot, count)
  print top - bot

if __name__ == '__main__':
  main()
