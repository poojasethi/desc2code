import math
import itertools
import sys

def dist_squared(p1, p2):
  return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def is_rectangle(p1, p2, p3, p4):
  cx = (p1[0] + p2[0] + p3[0] + p4[0]) / 4.0
  cy = (p1[1] + p2[1] + p3[1] + p4[1]) / 4.0

  dd1 = (cx - p1[0]) ** 2 + (cy - p1[1]) ** 2
  dd2 = (cx - p2[0]) ** 2 + (cy - p2[1]) ** 2
  dd3 = (cx - p3[0]) ** 2 + (cy - p3[1]) ** 2
  dd4 = (cx - p4[0]) ** 2 + (cy - p4[1]) ** 2

  return abs(dd1 - dd2) <= .001 and abs(dd1 - dd3) <= .001 and abs(dd1 - dd4) <= .001

def is_square(p1, p2, p3, p4):
  x = set()
  x.add(dist_squared(p1, p2))
  x.add(dist_squared(p1, p3))
  x.add(dist_squared(p1, p4))
  x.add(dist_squared(p2, p3))
  x.add(dist_squared(p2, p4))
  x.add(dist_squared(p3, p4))
  return len(x) == 2

def main():
  vertices = []
  for i in range(8):
    x, y = map(int, raw_input().split())
    vertices.append((x, y))
  for square in itertools.combinations(vertices, 4):
    rect = []
    for point in vertices:
      if point not in square:
        rect.append(point)
    if is_square(square[0], square[1], square[2], square[3]) and is_rectangle(rect[0], rect[1], rect[2], rect[3]):
      print 'YES'
      for point in square:
        print vertices.index(point) + 1,
      print
      for point in rect:
        print vertices.index(point) + 1,
      return
  print 'NO'

if __name__ == '__main__':
  main()
