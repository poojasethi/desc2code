import math
import sys

def main():
  n, m = map(int, raw_input().split())
  a = map(int, raw_input().split())
  b = map(int, raw_input().split())
  merged = []
  for x in a:
    merged.append([x, True])
  for x in b:
    merged.append([x, False])
  merged.sort()
  lefts = []
  rights = []
  tower = -1000000000000
  for i in range(len(merged)):
    if merged[i][1]: # City
      lefts.append(abs(merged[i][0] - tower))
    else: # Tower
      tower = merged[i][0]
  tower = 10000000000000
  for i in range(len(merged) - 1, -1, -1):
    if merged[i][1]: # City
      rights.append(abs(merged[i][0] - tower))
    else: # Tower
      tower = merged[i][0]
  rights.reverse()
  mins = []
  for i in range(n):
    mins.append(min(lefts[i], rights[i]))
  print max(mins)

if __name__ == '__main__':
  main()
