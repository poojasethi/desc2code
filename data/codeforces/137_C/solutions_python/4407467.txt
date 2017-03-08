import sys

inputs = sys.stdin.readline().split()
n = int(inputs[0])
l = [0] * n
for i in xrange(n):
    inputs = sys.stdin.readline().split()
    a = int(inputs[0])
    b = int(inputs[1])
    l[i] = (a,b)

l1 = sorted(l, key=lambda e : e[0])
prev_max = l1[0][1]
counter = 0

for i in xrange(1, n):
    cur = l1[i]
    if (prev_max > cur[1]):
        counter += 1
    else:
        prev_max = cur[1]
print counter 


