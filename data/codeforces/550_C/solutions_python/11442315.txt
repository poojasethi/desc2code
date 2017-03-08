import math
import sys

def main():
  n = raw_input()
  for i in range(1000):
    if i % 8 == 0:
      s = str(i)
      index = 0
      for j in range(len(n)):
        if n[j] == s[index]:
          index += 1
        if index == len(s):
          break
      if index == len(s):
        print 'YES'
        print i
        return
  print 'NO'

if __name__ == '__main__':
  main()
