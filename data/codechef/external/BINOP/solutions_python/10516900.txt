__author__ = 'kh1911'


t = input()
while t:
    t -= 1
    a = raw_input().strip()
    b = raw_input().strip()
    total = 0
    if a != b:
        if a.count('0') == 0:
            print 'Unlucky Chef'
            continue
        if a.count('1') == 0:
            print 'Unlucky Chef'
            continue
        i = 0
        onesCount = 0
        zerosCount = 0
        while i < len(a):
            if a[i] != b[i]:
                if a[i] == '1':
                    onesCount += 1
                else:
                    zerosCount += 1
            i += 1
        minCount = min(onesCount,zerosCount)
        total += minCount
        onesCount -= minCount
        zerosCount -= minCount
        total += onesCount
        total += zerosCount
    print 'Lucky Chef'
    print total
