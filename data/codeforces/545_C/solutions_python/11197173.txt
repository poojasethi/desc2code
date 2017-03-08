import math
import sys
from heapq import *

def main():
  num_trees = int(raw_input())
  trees = []
  MAX = 100005
  xs = [0] * MAX
  hs = [0] * MAX
  for i in range(num_trees):
    x, h = map(int, raw_input().split())
    xs[i] = x
    hs[i] = h
  last = -sys.maxint - 1
  xs[num_trees] = sys.maxint
  out = 0
  for i in range(num_trees):
    if xs[i] - hs[i] > last:
      out += 1
      last = xs[i];
    elif xs[i] + hs[i] < xs[i + 1]:
      out += 1
      last = xs[i] + hs[i]
    else:
      last = xs[i]
  print out


if __name__ == '__main__':
  main()
