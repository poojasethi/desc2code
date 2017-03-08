import math

n = input()
classes = []
for i in range(n):
  classes.append(map(int,raw_input().split()))
classes.sort()
t = 0
for a, b in classes:
  t = a if t > b else b
print t
