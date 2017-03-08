def main():
    dic = {}
    lados = {}
    for i in xrange(4):
        x1, y1, x2, y2 = map(int, raw_input().split())

        if (x1 != x2 and y1 != y2) or (x1 == x2 and y1 == y2):
            print "NO"
            exit(0)

        if x1 > x2 or (x1 == x2 and y1 > y2):
            x1, y1, x2, y2 = x2, y2, x1, y1

        try:
            lados[(x1, y1, x2, y2)] += 1
        except KeyError:
            lados[(x1, y1, x2, y2)] = 1

        try:
            dic[(x1, y1)] += 1
        except KeyError:
            dic[(x1, y1)] = 1

        try:
            dic[(x2, y2)] += 1
        except KeyError:
            dic[(x2, y2)] = 1

    cx = cy = 0

    if len(lados) < 4:
        print "NO"
    else:
        for p in dic:
            if dic[p] != 2:
                cx = cy = 4
                break
            if p[0] == x2:
                cx += 1
            if p[1] == y2:
                cy += 1

        if cx == 4 or cy == 4:
            print "NO"
        else:
            print "YES"

if __name__ == '__main__':
    main()