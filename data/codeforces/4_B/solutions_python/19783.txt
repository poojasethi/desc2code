d, sumTime = map(int, raw_input().split())
space = 0
m, M = [], []
for i in range(d):
    mind, Mind = map(int, raw_input().split())
    sumTime -= mind
    space += Mind - mind
    m.append(mind)
    M.append(Mind)

if 0 <= sumTime <= space:
    print 'YES'
    ans = []
    for i in range(d):
        s = min(sumTime, M[i] - m[i])
        ans.append(m[i] + s)
        sumTime -= s
    print ' '.join(`x` for x in ans)
else:
    print 'NO'
