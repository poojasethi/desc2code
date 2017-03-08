n, a = input(), map(int, raw_input().split())
a = [sum(a[i::3]) for i in xrange(3)]
print ["chest", "biceps", "back"][a.index(max(a))]