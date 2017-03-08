stick = map(int, raw_input().split())
stick.sort()
if sum(stick[:2]) > stick[2] or sum(stick[1:3]) > stick[3]:
    print 'TRIANGLE'
elif sum(stick[:2]) == stick[2] or sum(stick[1:3]) == stick[3]:
    print 'SEGMENT'
else:
    print 'IMPOSSIBLE'
