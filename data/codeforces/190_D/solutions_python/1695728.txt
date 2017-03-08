import os
import sys

debug="DEBUG" in os.environ

n,k= map( int, sys.stdin.readline().split()[:2] )
vals = map( int, sys.stdin.readline().strip('\n\r ').split()[:n] )
if k==1:
  count = (n*(n+1))/2 
else:
  count = 0
  d = {}
  leftmost = -1
  for i,val in enumerate(vals):
    if val in d:
      d[val] += [i]
      dval = d[val]
      if len(dval) < k: pass
      else:
        dvalk = dval[-k]
        if dvalk > leftmost: leftmost = dvalk
    else:
      d[val] = [i]

    count += leftmost + 1

print( count )
