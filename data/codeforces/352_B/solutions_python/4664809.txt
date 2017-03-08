import sys
import math

inputs = sys.stdin.readline().split()
n = int(inputs[0])

digits = sys.stdin.readline().split()

d = dict()

for i in xrange(n):
    num = int(digits[i])
    if num not in d:
        d[num] = [i]
    else:
        d[num].append(i)

l = []
for num in d:
    v = d[num]
    if len(v) == 1:
        l.append((num, 0))
    elif len(v) == 2:
        l.append((num,v[1] - v[0]))
    else:
        diff = v[1] - v[0]
        for j in xrange(1, len(v)):
            if v[j] - v[j-1] != diff:
                break
        else:
            l.append((num, diff)) 


l.sort()
print len(l)
for p in l:
    print p[0], p[1]
