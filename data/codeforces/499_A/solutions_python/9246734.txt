

n, x = map(int, raw_input().split())

ans = 0

now = 1

for i in xrange(n):
  l, r = map(int, raw_input().split())
  ans += r - (l-((l-now)%x))+1
  now = r+1

print ans
