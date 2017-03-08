import math
a,b,c = map(int, raw_input().split())
delta = b**2 - 4*a*c
delta = math.sqrt(delta)
if (a < 0): a,b,c = -a,-b,-c
print (delta - b)/(a*2)
print (-delta - b)/(a*2)