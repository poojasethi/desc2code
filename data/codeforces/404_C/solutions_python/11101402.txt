import math
import sys
from collections import deque

def main():
  n, k = map(int, raw_input().split())
  a = list(enumerate(map(int, raw_input().split()), 1))
  a.sort(key = lambda x: x[1])
  if a[0][1]:
    print -1
    return
  e = []
  q = deque([[1, k, a[0][0]]])
  for i, x in a[1:]:
    while q and q[0][0] < x:
      q.popleft()
    if not q or q[0][0] != x:
      print -1
      return
    if k > 1:
      q.append([x + 1, k - 1, i])
    e.append((q[0][2], i))
    q[0][1] -= 1
    if not q[0][1]:
      q.popleft()
  print len(e)
  print '\n'.join(' '.join(map(str, x)) for x in e)

if __name__ == '__main__':
  main()
