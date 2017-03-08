# 
m = int(raw_input())
for t in range(0,m):
	n = int(raw_input())
	# the belo line will split the line and will store in the list
	sol = map(int, raw_input().split())
	rk = range(1, n+1)
	for i in  range(n-1, -1, -1):
		rk.insert(i, rk.pop(i-sol[i]))
	print ' '.join(map(str, rk))
