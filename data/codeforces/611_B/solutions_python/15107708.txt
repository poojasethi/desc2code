import sys

f = sys.stdin

def generate(x):
    ans = sum([2 ** it for it in xrange(x + 1)])
    ret = []
    for it in xrange(x - 1, -1, -1):
        ret.append(ans - 2 ** it)
    return ret

repo = []
for jt in xrange(1, 62):
    repo += generate(jt)
a, b = map(int, f.readline().split(' '))
ans = 0
for num in repo:
    if num < a:
        continue
    if num > b:
        break
    ans += 1
print ans
