n,m = map(int,raw_input().split())
ans = -1
for x in xrange(n):
	ans = max(ans,min(map(int,list(raw_input().split()))))
print ans
