import sys

f = sys.stdin
n = int(f.readline())
color = [int(x) for x in f.readline().split(' ')]
m = min(color)
ans = m * n
color = [x - m for x in color]
color = color + color
color = color[:-1]
s = 0
x = 0
big = 0
while x < n:
    start = x
    while(color[start] > 0):
        s += 1
        start += 1
    if s > big:
        big = s
    if x == start:
        x += 1
    else:
        x = start
    s = 0
print ans + big

