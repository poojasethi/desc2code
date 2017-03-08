n = int(raw_input())
a = map(int, raw_input().split())
k = n
for i in range(0,n-1):
    if a[i] > a[i+1]:
	k = i
	break
    
if k == n:
    print 0
elif a[k+1:]+a[:k+1] == sorted(a):
    print n - 1 - k 
else :
    print -1
    

