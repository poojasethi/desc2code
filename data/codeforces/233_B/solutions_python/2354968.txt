#!/usr/bin/env python
import math

def sum (x):
    s = 0
    while (x > 0):
        s += (x % 10)
        x = x / 10
    return s

n = int (raw_input ())
for i in range (1, 90):
    delta = i * i + 4 * n;
    can = int (math.sqrt (delta))
    if (can * can == delta):
        if (can - i) % 2 == 0:
            x = (can - i) / 2
            if i == sum (x):
                print x
                quit ()
print "-1"
