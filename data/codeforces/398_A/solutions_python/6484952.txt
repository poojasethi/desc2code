from sys import stdout
def main():
    a, b = map(int, raw_input().split())
    if not a or not b:
        stdout.write(str(a * a - b * b) + '\n')
        stdout.write('o' * a + 'x' * b)
        return
    ans = -10 ** 17
    v = 0
    for i in xrange(1, a+1):
        x, y = divmod(b, i + 1)
        t = i - 1 + (a - i + 1) * (a - i + 1) - y * (x + 1) * (x + 1) - (i + 1 - y) * x * x
        if ans < t:
            ans = t
            v = i
    x, y = divmod(b, v + 1)
    c = ['o'] * (v - 1) + ['o' * (a - v + 1)]
    d = ['x' * (x + 1)] * y + ['x' * x] * (a + 1 - y)
    e = []
    for j in xrange(v):
        e.append(d[j])
        e.append(c[j])
    e.append(d[-1])       
    stdout.write(str(ans) + '\n')
    stdout.write(''.join(e))
main()
