n, k = map(int, raw_input().split())

s = raw_input()

d = [0] * 26

for i in xrange(26):
  d[i] = s.count(chr(ord('A')+i))

d.sort()

ans = 0
cnt = 0

for i in d[::-1]:
  if i + cnt >= k:
    ans += (k-cnt) * (k-cnt)
    print ans
    exit(0)
  else:
    ans += i*i
    cnt += i
