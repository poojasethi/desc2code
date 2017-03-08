n=int(input())
ar=map(int,raw_input().split())
maxVal=max(ar)+1
hsh=[0]*maxVal
for i in ar:
    hsh[i]+=1
dp=[0]*maxVal
dp[0]=0
dp[1]=hsh[1]
for i in range(2,maxVal):
    dp[i]=max([dp[i-2]+hsh[i]*i,dp[i-1]])
print dp[maxVal-1]
