from sys import stdout
def solve(p, x):
    c = []
    for i in xrange(1, 10):
        s = 0
        b = i
        a = []
        for j in xrange(p):
            a.append(b)
            s, b = divmod(b * x + s, 10)
        if b == i and s == 0:
            a.reverse()
            c.append(''.join(map(str, a)))
    c.sort()
    for r in c:
        if r[0] != '0':
            return r
    return ''
def main():
    p, x = map(int, raw_input().split())
    if x == 5 and p % 42 == 0:
        stdout.write(solve(42, 5) * (p / 42))
        return
    for i in xrange(1, 1000):
        s = solve(i, x)
        if not s: continue
        l = len(s)
        if p % l == 0:
            stdout.write(s * (p / l))
        else:
            stdout.write('Impossible')
        return
main()
