def bsearch(lo, hi, check):
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def main():
    n, k = map(int, raw_input().split())
    arr = map(int, raw_input())
    ps = [int(arr[0] == 0)]
    for x in xrange(1, n):
        ps.append(ps[-1] + (arr[x] == 0))
    lnz = [float('inf')]*n
    rnz = [float('inf')]*n
    for x in xrange(n):
        if arr[x] == 0:
            lnz[x] = x
        else:
            lnz[x] = lnz[x - 1]
    if arr[-1] == 0:
        rnz[-1] = n - 1
    for x in xrange(n - 2, -1, -1):
        if arr[x] == 0:
            rnz[x] = x
        else:
            rnz[x] = rnz[x + 1]
    # print lnz
    # print rnz
    # print ps
    md = float('inf')
    for s in xrange(n):
        if arr[s] != 0:
            continue
        e_t = ps[s] + k
        e = bsearch(0, n, lambda el: ps[el] >= e_t)
        if e == n:
            break
        mid = s + ((e - s + 1) // 2)
        m = lnz[mid]
        md = min(md, max(m - s, e - m))
        m = rnz[mid]
        md = min(md, max(m - s, e - m))
        # for x in xrange(s, e + 1):
        #     if arr[x] == 0:
        #         c2md = min(md, max(x - s, e - x))
        #         m = lnz[mid]
        #         if max(x - s, e - x) < max(m - s, e - m):
        #             print s, e, x, m, c2md, md, 'l'
        #         m = rnz[mid]
        #         if max(x - s, e - x) < max(m - s, e - m):
        #             print s, e, x, m, c2md, md, 'r'
        # m = lnz[mid]
        # if c2md < max(m - s, e - m):
        #     print s, e, e_t, m, md, c2md
        # m = rnz[mid]
        # if c2md < max(m - s, e - m):
        #     print s, e, e_t, m, md, c2md

        # print s, e, e_t, m, md
    print md

main()
