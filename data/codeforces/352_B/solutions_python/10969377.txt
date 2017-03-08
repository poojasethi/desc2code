import collections

n = input()
xs = map(int, raw_input().split())

d = collections.defaultdict(list)
for i in range(n):
    d[xs[i]] += [i]

result = []
for k, v in d.items():
    if len(v) == 1:
        result += [(k, 0)]
    else:
        diff = v[1] - v[0]
        add = True
        for i in range(2, len(v)):
            if v[i] - v[i - 1] != diff:
                add = False
                break
        if add:
            result += [(k, diff)]
        

print len(result)
print '\n'.join('%d %d' % x for x in sorted(result))