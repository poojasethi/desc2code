s = raw_input()
ans,cur = 0,0
for i in range(len(s)):
        if i!=len(s)-1 and s[i+1]=='0': continue
        if cur>i-cur+1 or cur==i-cur+1 and s[:cur]>=s[cur:i+1]: ans += 1
        else: ans = 1
        cur =  i+1
print ans
