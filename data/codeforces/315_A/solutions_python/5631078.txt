N = input()
a, b = zip(*[map(int, raw_input().split()) for i in xrange(N)])
print len([i for i in xrange(N) if a[i] not in b[:i]+b[i+1:]])
