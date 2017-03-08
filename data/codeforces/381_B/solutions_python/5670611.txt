def second():
    freq = [0]*5010
    m = input()
    a = map(int,raw_input().split())
    for i in xrange(m):
        freq[a[i]] += 1
    mx = max(a)
    i = 1
    res = []
    while i < mx:
        if freq[i] != 0:
            res.append(str(i))
            freq[i] -= 1
        i += 1
    while i > 0:
        if freq[i] != 0:
            res.append(str(i))
            freq[i] -= 1
        i -= 1
    #print res
    print len(res)
    print ' '.join(res)
second()
