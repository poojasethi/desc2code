n = int(input());
k = map(int, raw_input().split())
ans = 10000000
for i in xrange(n):
	tmp = map(int, raw_input().split())
	count = 0
	for j in xrange(k[i]):
			count += 5 * tmp[j];
			count += 15
	ans = min(ans, count)
print ans 
