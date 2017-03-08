n,m = [int(x) for x in raw_input().split()]
arr = [int(x) for x in raw_input().split()]
total = 0
while m:
	p = [int(x) for x in raw_input().split()]
	if p[0] == 1:
		arr[p[1] - 1] = p[2] - total
	if p[0] == 2:
		total = total+p[1]
	elif p[0] == 3:
		print(total + arr[p[1]-1])
	m-=1			
