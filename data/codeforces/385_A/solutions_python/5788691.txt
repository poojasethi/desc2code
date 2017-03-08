N, C = map(int, raw_input().split())
a = map(int, raw_input().split())
b = [a[i]-a[i+1] for i in xrange(N-1)]
c = max(b)
print c-C if c > C else 0
