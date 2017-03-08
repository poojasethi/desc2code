import sys
import re

def mask(x):
    return re.sub(r'[01235689]', '', str(x))

(a, b) = [int(x) for x in sys.stdin.readline().strip().split()]

a = a + 1
b = str(b)

while mask(a) != b:
    a += 1

print(a)
