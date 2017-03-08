n, d = map(int, raw_input().split())
a = map(int, raw_input().split())
if sum(a) + (n-1)*10 > d:
	print -1
else: 
	print (d - sum(a)) / 5
