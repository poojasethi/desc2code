
def main():
    n, a, b = map(int, raw_input().split())
    if n > a * b:
        print -1
        return
    out = [[(y if y <= n else 0) for y in xrange(x * b + 1, (x + 1) * b + 1)] for x in xrange(a)]
    if b % 2 == 0:
        for x in xrange(1, a, 2):
            out[x].reverse()
    print '\n'.join([' '.join(map(str, out[x])) for x in xrange(a)])

main()
