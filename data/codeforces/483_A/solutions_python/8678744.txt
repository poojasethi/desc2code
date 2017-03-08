import sys

args = raw_input().split()
l = int(args[0])
r = int(args[1])

if r - l < 2:
  print -1
  sys.exit()

if l % 2 == 0:
  print l, (l + 1), (l + 2)
  sys.exit()

if r - l > 2:
  print (l + 1), (l + 2), (l + 3)
  sys.exit()

print -1
