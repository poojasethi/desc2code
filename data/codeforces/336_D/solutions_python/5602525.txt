#!/usr/bin/python
import sys

def ext_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    (dp, xp, yp) = ext_gcd(b, a % b)
    return (dp, yp, xp - a//b * yp)

def mod_solve(a, b, n):
    (d, xp, yp) = ext_gcd(a, n)
    if b % d == 0:
        x0 = xp * (b/d) % n
        return x0
    else:
        return None


MOD = 1000000007
(n, m, g) = map(lambda x: int(x), raw_input().split())
if n == 0:
    if (m == 1 and g == 1) or (m > 1 and g == 0):
        result = 1
    else:
        result = 0
    print(result)
    sys.exit(0)

if m == 0:
    if (n % 2 == 0 and g == 1) or (n % 2 == 1 and g == 0):
        result = 1
    else:
        result = 0
    print(result)
    sys.exit(0)

term = 1
result = term
for i in xrange(1, n+1):
    term = (term * (m + i) * mod_solve(i, 1, MOD)) % MOD
    if i % 2 == 0:
        result = (result + term) % MOD
    else:
        result = (result + MOD - term) % MOD
choosenm = term
if n % 2 == 1:
    result = (MOD - result) % MOD
if m == 1:
    if n % 2 == 0:
        result = (result + MOD - 1) % MOD
    else:
        result = (result + 1) % MOD
if g == 1:
    result = (choosenm + MOD - result) % MOD
print(result)




