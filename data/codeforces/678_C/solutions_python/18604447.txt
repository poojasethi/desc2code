import sys

def gcd(x, y):
    if x < y:
        return gcd(y, x)
    if x % y == 0:
        return y
    return gcd(y, x % y)

f = sys.stdin
n, a, b, p, q = map(int, f.readline().strip().split(' '))
x = n / a
y = n / b
z = n * gcd(a, b) / a / b
print(p * (x - z) + q * (y - z) + z * max(p, q))
