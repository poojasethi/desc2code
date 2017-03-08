#!/usr/bin/python

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#  a*x + b*y = c1
# -b*x + a*y = c2
# is it solvable?
def is_solvable(a, b, c1, c2):
    if a == 0 and b == 0:
        return c1 == 0 and c2 == 0
    if (c1*b + c2*a) % (a*a + b*b) != 0:
        return False
    y = (c1*b + c2*a) / (a*a + b*b)
    if a != 0:
        return (c1 - b*y) % a == 0
    else:
        return (c2 - a*y) % b == 0

# can we solve for (m, n) in the following equations?
# x0 + m*cx + n*cy = x1
# y0 - n*cx + m*cy = y1
def can_solve(x0, y0, x1, y1, cx, cy):
    dx = x1 - x0
    dy = y1 - y0
    if cx == 0 and cy == 0:
        return dx == 0 and dy == 0
    if cx == 0:
        return dx % cy == 0 and dy % cy == 0
    if cy == 0:
        return dx % cx == 0 and dy % cx == 0
    d = gcd(abs(cx), abs(cy))
    if (dx % d != 0) or (dy % d != 0):
        return False
    return is_solvable(cx/d, cy/d, dx/d, -dy/d)

x1, y1 = map(lambda(x): int(x), raw_input().split())
x2, y2 = map(lambda(x): int(x), raw_input().split())
cx, cy = map(lambda(x): int(x), raw_input().split())

possible = (can_solve(x1, y1, x2, y2, cx, cy) or
            can_solve(-y1, x1, x2, y2, cx, cy) or
            can_solve(-x1, -y1, x2, y2, cx, cy) or
            can_solve(y1, -x1, x2, y2, cx, cy))
print "YES" if possible else "NO"
        


