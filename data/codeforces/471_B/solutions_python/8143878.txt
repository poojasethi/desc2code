import collections
import math
import operator

n = int(raw_input())
difficulties = map(int, raw_input().split())
pairs = sorted([(difficulties[i], i) for i in range(len(difficulties))])
counts = [difficulties.count(x) for x in set(difficulties)]
if reduce(operator.mul, counts, 1) < 3:
  print "NO"
  exit()
def display():
  print ' '.join([str(x[1] + 1) for x in pairs])
print "YES"
display()
mask = []
for i in range(len(pairs) - 1):
  if pairs[i][0] == pairs[i + 1][0]:
    mask.append(i)
x = mask[0]
pairs[x], pairs[x + 1] = pairs[x + 1], pairs[x]
display()
x = mask[1]
pairs[x], pairs[x + 1] = pairs[x + 1], pairs[x]
display()
