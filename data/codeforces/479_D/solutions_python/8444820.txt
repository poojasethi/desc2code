import math
from bisect import bisect_left

n, l, x, y = map(int, raw_input().split())
marks = map(int, raw_input().split())

markx = set()
marky = set()

def in_range(x):
  return x >= 0 and x <= l

for mark in marks:
  if in_range(mark + x):
    markx.add(mark + x)
  if in_range(mark - x):
    markx.add(mark - x)
  if in_range(mark + y):
    marky.add(mark + y)
  if in_range(mark - y):
    marky.add(mark - y)

found_x = False
found_y = False
for mark in marks:
  if mark in markx:
    found_x = True
  if mark in marky:
    found_y = True
if found_x and found_y:
  print 0
  exit()
if found_x:
  print 1
  print y
  exit()
if found_y:
  print 1
  print x
  exit()
intersect = markx.intersection(marky)
if len(intersect) == 0:
  print 2
  print x, y
else:
  print 1
  print intersect.pop()
