import string

sticks = sorted(map(int,raw_input().split()))
m = max( sticks[0] + sticks[1] - sticks[2], sticks[1] + sticks[2] - sticks[3])
ans = ["IMPOSSIBLE","SEGMENT","TRIANGLE"]
print ( ans[ (m>=0) + (m>0)] )
