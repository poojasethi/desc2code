import sys

inputs = sys.stdin.readline().split()
n = int(inputs[0])
totalArea = 0
min_x1 = 31400
min_y1 = 31400
max_x2 = 0
max_y2 = 0

for i in xrange(n):
    line = sys.stdin.readline().split()
    x1 = int(line[0])
    y1 = int(line[1])
    x2 = int(line[2])
    y2 = int(line[3])
    totalArea += (x2-x1) * (y2-y1)
    if (x1 < min_x1):
        min_x1 = x1
    if (y1 < min_y1):
        min_y1 = y1
    if (x2 > max_x2):
        max_x2 = x2
    if (y2 > max_y2):
        max_y2 = y2
squareSide = max(max_y2 - min_y1, max_x2 - min_x1)
squareArea = squareSide * squareSide
if (squareArea == totalArea):
    print "YES"
else:
    print "NO"
