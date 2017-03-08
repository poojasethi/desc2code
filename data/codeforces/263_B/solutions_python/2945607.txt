n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
a.sort()
if k > n:
    print "-1"
else:
    k = n - k
    print a[k], a[k]
