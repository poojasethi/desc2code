
n = input()
a = map(int, raw_input().strip().split())


if len(a) <= 2:
    print len(a)
else:
    mx = 2
    cr = 2
    for i in range(2, n):
        if a[i] == a[i-1]+a[i-2]:
            cr += 1
        else:
            mx = max(mx, cr)
            cr = 2
    mx = max(mx, cr)
    print mx





