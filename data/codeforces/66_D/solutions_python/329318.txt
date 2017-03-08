import sys

n = int(raw_input())

if n == 2:
    print -1
    sys.exit(0)
else:
    l = [15, 10, 6]
    if n > 3:
        for i in range(2, n-1):
            l.append(6*i)

for i in l:
    print i
