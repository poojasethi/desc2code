n = int(raw_input())
arr = map(int, raw_input().split())
idx = [-1]*(n+5)
for i in xrange(n):
    idx[arr[i]] = i

m = int(raw_input())
q = map(int,raw_input().split())
res1,res2=0,0
for num in q:
    res1 += idx[num]+1
    res2 += n-idx[num]
    
print res1, res2