a = map(int, raw_input().split())
a.sort()
print a[0] + a[1] if (a[0] + a[1]) * 2 <= a[2] else sum(a) / 3
