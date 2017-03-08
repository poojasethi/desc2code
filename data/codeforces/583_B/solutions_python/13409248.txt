n = input()
l = list(map(int, raw_input().split()))
N = 0; plus = 1;  t = 0
mp = {}
while(N<n):
    if t%2==0:
        for i in range(0,n):
            if (l[i]<=N) and (not mp.has_key(i)):
                N+=1
                mp[i]=True    
    else:
        for i in range(n-1,-1,-1):
            if (l[i]<=N) and (not mp.has_key(i)):
                N+=1
                mp[i]= True
    t+=1
     
print(t-1)