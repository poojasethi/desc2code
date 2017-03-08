n = map(int, raw_input().split())[0]
l = map(int, raw_input().split())

s = sum(l)

if len(l) == 1 and s == 1:
    print 'YES'
elif s == len(l)-1 and len(l) != 1:
    print 'YES'
else:
    print 'NO'
