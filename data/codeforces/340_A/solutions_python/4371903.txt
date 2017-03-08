def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

x, y, a, b = map(int, raw_input().strip().split(' '))
lct = x * y / gcd(x, y)
bottom = (a - 1) / lct
top = b / lct
print top - bottom
