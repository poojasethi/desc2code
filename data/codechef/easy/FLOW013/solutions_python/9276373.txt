T = int(raw_input())

for i in range(T):
    a = map(int, raw_input().split())
    if (a[0]+a[1]+a[2]) == 180 and 0 not in a:
        print 'YES'
    else:
        print 'NO'
