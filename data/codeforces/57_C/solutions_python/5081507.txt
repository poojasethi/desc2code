#!/usr/bin/python
MOD = 1000000007

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

# calculates \choose(2*k-1, k)
def choose(n, nInv):
    result = 1
    for i in range(2*n-1, n-1, -1):
        result = result * i % MOD
    for i in range(n):
        result = result * nInv[i] % MOD
    return result

def solve():
    n = int(raw_input())
    nInv = [mod_solve(i, 1, MOD) for i in range(1, n+1)]
    print (choose(n, nInv) * 2 - n) % MOD

solve()

