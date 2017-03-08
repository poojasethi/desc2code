n = int(raw_input())
a = map(int, raw_input().split(' '))

res = []
for i in range(1, 10):
    if i in a:
        res.append(i)
        break

for i in range(10, 100, 10):
    if i in a:
        res.append(i)
        break

if len(res) == 0:
    for i in a:
        if not i in (0, 100):
            res.append(i)
            break

if 0 in a:
    res.append(0)
if 100 in a:
    res.append(100)

print len(res)
for i in range(len(res)):
    print res[i],
