n = int(raw_input())
A = map(int, raw_input().split())

S = [0]
for i in xrange(n):
	S += [S[-1]+1-A[i]]

ans = 0
for i in xrange(n):
	if A[i] == 1:
		ans += S[n]-S[i+1]
print ans
