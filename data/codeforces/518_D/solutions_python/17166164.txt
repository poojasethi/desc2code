MAXN = 2005
dp = [[0 for col in range(MAXN)] for row in range(MAXN)]

line = raw_input()
n, q, t = line.split()
n = int(n)
t = int(t)
q = float(q)

if t <= n:
    print(t*q)
else:
    dp[0][0] = 1
    for i in range(t+1):
        for j in range(min(t, n)+1):
            if j == n:
                dp[i+1][j] += dp[i][j]
            else:
                dp[i+1][j] += (1-q) * dp[i][j]
                dp[i+1][j+1] += q * dp[i][j]

    ans = 0
    for i in range(n+1):
        ans += i * dp[t][i]
    print(ans)
 					 					  		 	        	 	