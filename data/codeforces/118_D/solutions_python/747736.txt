import sys

n1, n2, k1, k2 = map(int, sys.stdin.readline().split())

mod = 100000000
dp = {}

def calc(al, bl, ac, bc):
    global k1
    global k2
#    print al, bl, ac, bc

    if ac > k1 or bc > k2:
        return 0
    if al < 0 or bl < 0:
        return 0
    if al == 0 and bl == 0:
        return 1

    k = (al, bl, ac, bc)
    if dp.has_key(k):
        return dp[k]

    dp[k] = calc(al-1, bl, ac+1, 0) + calc(al, bl-1, 0, bc+1)
    return dp[k]

print calc(n1, n2, 0, 0)%mod
