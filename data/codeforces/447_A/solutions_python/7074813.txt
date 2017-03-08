p, n = map(int, raw_input().split())

s = set()
ret = -1
for i in range(n):
    x = int(raw_input())
    h = x % p
    if h in s:
        ret = i+1
        break
    s.add(h)

print ret
