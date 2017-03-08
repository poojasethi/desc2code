l, s = map(int, raw_input().split())
minn, maxn = [1] + [0] * (l - 1), [1] + [0] * (l - 1)

def get(num, s, r):
    for i in (xrange(0, len(num)) if not r else xrange(len(num) - 1, -1, -1)):
        for n in xrange(num[i], 10):
            num[i] = n
            if sum(num) == s:
                return ''.join(map(str, num))
    return '-1'

print '0 0' if l == 1 and s == 0 else ' '.join((get(minn, s, True), get(maxn, s, False)))
