import math
import bisect

num_piles = int(raw_input())
piles = map(int, raw_input().split())
num_worms = int(raw_input())
labels = map(int, raw_input().split())
accu=0
for i in xrange(num_piles):
  accu+=piles[i]
  piles[i]=accu
for label in labels:
  print bisect.bisect_left(piles, label) + 1
