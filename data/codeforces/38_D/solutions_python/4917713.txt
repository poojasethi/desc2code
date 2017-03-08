#!/usr/bin/python
import sys
from fractions import Fraction

class Area:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def __mul__(self, other):
        x1 = max(self.x1, other.x1)
        y1 = max(self.y1, other.y1)
        x2 = min(self.x2, other.x2)
        y2 = min(self.y2, other.y2)
        return Area(x1, y1, x2, y2)

class BoxStack:
    def __init__(self, a, x0, y0):
        # always start from a single box
        self.wx = Fraction(2*x0 + a, 2)
        self.wy = Fraction(2*y0 + a, 2)
        self.weight = a**3
    def addBox(self, a, x0, y0):
        weight = a**3
        self.wx = (self.wx * self.weight +
                   Fraction(2*x0 + a, 2) * weight) / (self.weight + weight)
        self.wy = (self.wy * self.weight +
                   Fraction(2*y0 + a, 2) * weight) / (self.weight + weight)
        self.weight += weight
    def isSupported(self, area):
        return (area.x1 <= self.wx and self.wx <= area.x2 and
                area.y1 <= self.wy and self.wy <= area.y2)

def solve():
    n = int(raw_input())
    boxStacks = [None for i in range(n)]
    supports  = [None for i in range(n)]
    prevTop = Area(-100, -100, 100, 100)
    for i in range(n):
        (x1, y1, x2, y2) = map(lambda x: int(x), raw_input().split())
        if x1 > x2:
            (x1, x2) = (x2, x1)
        if y1 > y2:
            (y1, y2) = (y2, y1)
        a = x2 - x1
        boxStacks[i] = BoxStack(a, x1, y1)
        bottom = Area(x1, y1, x2, y2)
        supports[i] = prevTop * bottom
        prevTop = bottom
        for j in range(i-1, -1, -1):
            boxStacks[j].addBox(a, x1, y1)
        for j in range(i, -1, -1):
            if not boxStacks[j].isSupported(supports[j]):
                print i
                sys.exit(0)
    print n

solve()
