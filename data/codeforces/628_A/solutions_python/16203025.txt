def largest_pow_under(k):
    a = 1
    while a * 2 <= k:
        a *= 2
    return a

def solve(n, b):
    ans = 0
    while n > 1:
        players = largest_pow_under(n)
        ans += players * b
        ans += players / 2
        n = players / 2 + n - players

    return ans

n, b, p = map(int, raw_input().split())
print solve(n, b), n * p
