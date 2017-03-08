N = int(raw_input())

ans = 0

for tc in xrange(N):
    a, b, c, d = map(int, raw_input().split())
    ans += (c - a + 1) * (d - b + 1)

print ans
