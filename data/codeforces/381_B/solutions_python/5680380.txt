N = input()
a = map(int, raw_input().split())
b = [0]*5001
for x in a:
	b[x] += 1
ans = [i for i in xrange(1, len(b)) if b[i] > 0]
ans += [i for i in xrange(1, len(b)) if b[i] > 1 and i < ans[len(ans)-1]][::-1]
print len(ans)
print ' '.join(map(str, ans))
