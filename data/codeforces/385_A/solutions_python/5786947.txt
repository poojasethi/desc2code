n,c = [int(x) for x in raw_input().split()]
a = [int(x) for x in raw_input().split()]

maxi = 0
for i in range(0,n-1):
	maxi = max(maxi,a[i]-a[i+1]-c)
print maxi