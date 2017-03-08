dp = []
for x in range(2001):
	dp.append(-1)

ans = 0
n = input()
for i in range(n):
	line = raw_input().split()
	c, x = line[0], int(line[1])
	if c == 'win':
		dp[x] = ans
	elif dp[x] != -1:
		ans = max(ans, dp[x] + pow(2, x))

print ans
