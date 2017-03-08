def main():
    n, p, q = map(int, raw_input().split())
    s = raw_input()
    l = len(s)

    for i in xrange(l + 1):
        for j in xrange(l + 1):
            if p * i + q * j == l:
                print i + j
                x = 0
                for _ in xrange(i):
                    print s[x:x+p]
                    x += p
                for _ in xrange(j):
                    print s[x:x+q]
                    x += q
                return

    print -1

main()
