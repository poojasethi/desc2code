n, v = map(int, raw_input().split())

res = []
for i in range(n):
    item = map(int, raw_input().split())
    minv = min(item[1:])
    if v > minv:
        res.append(i + 1)

print len(res)
res = map(str, res)
print(" ".join(res))
