import math
import sys

def bad_cols(a, b):
  out = set()
  for i in range(len(a)):
    if a[i] > b[i]:
      out.add(i)
    if a[i] < b[i]:
      return out
  return out

def main():
  n, m = map(int, raw_input().split())
  grid = []
  for i in range(n):
    grid.append(list(raw_input()))
  out = 0
  found = True
  while found:
    found = False
    for i in range(n - 1):
      tmp = bad_cols(grid[i], grid[i+1])
      for index in tmp:
        for j in range(n):
          grid[j][index] = 'z'
        found = True
        out += 1
  print out

if __name__ == '__main__':
  main()
