import math
import sys

def main():
  n = int(raw_input())
  if n <= 3:
    print 'NO'
    return
  if n % 2 == 0:
    print 'YES'
    while n != 4:
      print '{0} - {1} = 1'.format(n, n - 1)
      print '4 * 1 = 4'
      n -= 2
    print '4 * 3 = 12'
    print '12 * 2 = 24'
    print '24 * 1 = 24'
  else:
    print 'YES'
    while n != 5:
      print '{0} - {1} = 1'.format(n, n - 1)
      print '4 * 1 = 4'
      n -= 2
    print '3 - 1 = 2'
    print '5 - 2 = 3'
    print '4 * 3 = 12'
    print '12 * 2 = 24'


if __name__ == '__main__':
  main()
