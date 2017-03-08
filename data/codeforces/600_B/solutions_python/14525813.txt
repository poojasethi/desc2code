import bisect
n,m = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
a.sort()
c = ["%s"%bisect.bisect(a, x) for x in b]
print ' '.join(c)
