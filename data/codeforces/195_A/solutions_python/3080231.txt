import math, sys

(a, b, c) = [int(x) for x in sys.stdin.readline().strip().split()]

w = 0

while (w+c) * b < a * c:
    w += 1

print(w)
