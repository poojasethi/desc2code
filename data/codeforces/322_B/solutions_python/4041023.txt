import sys
def solve():    
    inputs = sys.stdin.readline().split()
    r = int(inputs[0])
    g = int(inputs[1])
    b = int(inputs[2])

    total = r/3 + g/3 + b/3
    l = [r%3, g%3, b%3]
    total += min(l)
    if (l.count(2) == 2 and r!=0 and g!=0 and b!=0):
        total = total - 1 + 2
    print total 

solve()

