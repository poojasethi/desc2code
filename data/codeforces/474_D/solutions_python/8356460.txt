par = map(int, raw_input().split(" "))
t, k = par[0], par[1]
MOD = 1000000007
MAXN = 100010


dp = [1]
for i in range(1, MAXN):
    dp.append(dp[i-1] + (dp[i-k] if i>=k else 0) % MOD)
    
dp[0] = 0
#print dp[:10]
for i in range(1, MAXN):
    dp[i] = (dp[i] + dp[i-1]) % MOD

#print dp[:10]
for i in range(t):
    par = map(int, raw_input().split(" "))            
    print (dp[par[1]] - dp[par[0]-1] + MOD) % MOD