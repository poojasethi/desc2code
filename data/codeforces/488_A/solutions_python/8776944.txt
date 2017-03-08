import math

n = int(raw_input())

count = 1
n += 1
while "8" not in str(n):
  n += 1
  count += 1
print count
