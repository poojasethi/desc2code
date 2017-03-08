#!/usr/bin/python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def visit(a, b, lcm):
    return lcm/a-1 if a < b else lcm/a

a, b = map(lambda x: int(x), raw_input().split())
lcm = a * b / gcd(a, b)
dasha = visit(a, b, lcm)
masha = visit(b, a, lcm)
if dasha > masha:
    print "Dasha"
elif dasha < masha:
    print "Masha"
else:
    print "Equal"
