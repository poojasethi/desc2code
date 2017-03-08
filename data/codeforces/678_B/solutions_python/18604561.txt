import sys

def isLeap(p):
    if p % 100 == 0:
        return p % 400 == 0
    return p % 4 == 0

f = sys.stdin
n = int(f.readline())
x = n
s = 0
while True:
    if isLeap(x):
        s += 2
    else:
        s += 1
    x += 1
    if s % 7 == 0 and isLeap(n) == isLeap(x):
        break
print(x)
