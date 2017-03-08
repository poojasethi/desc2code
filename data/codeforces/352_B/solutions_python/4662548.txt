n = int(raw_input().strip())
ais = map(int, raw_input().strip().split(' '))

collector = {}
BAD = -1

for i, ai in enumerate(ais):
    if ai in collector:
        prevs = collector[ai]
        if prevs == BAD:
            continue
        elif isinstance(prevs, tuple):
            if i - prevs[1] == prevs[1] - prevs[0]:
                collector[ai] = (prevs[1], i)
            else:
                collector[ai] = BAD
        else:
            collector[ai] = (prevs, i)
    else:
        collector[ai] = i

print len([1 for k, v in collector.iteritems() if v != BAD])

for k in sorted(collector.keys()):
    v = collector[k]
    if v != BAD:
        if isinstance(v, tuple):
            print k, v[1] - v[0]
        else:
            print k, 0
