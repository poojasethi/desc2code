n = input()
i, j = 1, n
while i <= j:
	print i,
	i+=1
	if i>j:
		break
	print j,
	j-=1
print