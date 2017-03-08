from math import pow

t = int(raw_input())
for i in range(t):
    x = int(raw_input())
    if x % 2 == 0:
        print x
    else:
        print x - 1
