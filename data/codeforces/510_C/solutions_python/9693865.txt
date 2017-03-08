import math
import string
import sys
from collections import deque

def main():
  n = int(raw_input())
  names = []
  for i in range(n):
    names.append(raw_input())
  edges = {}
  for c in string.lowercase:
    edges[c] = set()
  for i in range(n - 1):
    name_1 = names[i]
    name_2 = names[i + 1]
    found = False
    for c1, c2 in zip(name_1, name_2):
      if c1 != c2:
        if c2 not in edges[c1]:
          edges[c1].add(c2)
        if c1 in edges[c2]:
          print "Impossible"
          exit()
        found = True
        break;
    if not found and len(name_1) > len(name_2):
      print "Impossible"
      exit()

  visited = set()
  indicies = {}
  out = deque()

  def topsort(v):
    visited.add(v)
    for c in edges[v]:
      if c not in visited:
        topsort(c)
    out.appendleft(v)
    indicies[v] = len(edges) - len(out)

  for c in string.lowercase:
    if c not in visited:
      topsort(c)

  for c in edges:
    for u in edges[c]:
      if indicies[c] > indicies[u]:
        print "Impossible"
        exit();

  print "".join(out)


if __name__ == '__main__':
  main()
