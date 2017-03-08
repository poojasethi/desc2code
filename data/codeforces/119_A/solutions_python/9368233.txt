from fractions import gcd

a, b, n = map(int, raw_input().split())

i = 0
while n > 0:
    n -= gcd([a, b][i % 2], n)
    i += 1
print (i + 1) % 2

