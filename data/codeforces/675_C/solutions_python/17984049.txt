n = int(raw_input())
a = map(int, raw_input().split())
d = {}
sumi = 0
for i in a:
    sumi += i
    if sumi not in d:
        d[sumi] = 0
    d[sumi] += 1

print n - max(d.values())
