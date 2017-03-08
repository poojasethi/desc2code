n, m, k = map(int, raw_input().split())
a = map(int, raw_input().split())
print 0 if n%2==0 else min([min(a[0::2]), k*(2*m/(n+1))])
