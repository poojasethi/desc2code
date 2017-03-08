s = map(int, raw_input().split())
s.sort()
x = s[0] + s[1] - s[2]
y = s[1] + s[2] - s[3]
if x > 0 or y > 0:
    print 'TRIANGLE'
elif x < 0 and y < 0:
    print 'IMPOSSIBLE'
else:
    print 'SEGMENT'
