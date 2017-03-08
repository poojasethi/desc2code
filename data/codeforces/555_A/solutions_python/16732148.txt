n,k=map(int,raw_input().split())
counter = 0
result =0
for i in range(k):
	line = map(int,raw_input().split())
	line=line[1:]
	result+=len(line)
	if line[0]==1:
		i = 1
		c = 0
		while(i < len(line) and line[i]-line[i-1]==1):
			c+=1
			i+=1
		result-=c
		counter +=len(line)-1-c
	else:
		counter+=len(line)-1
counter+=result-1
print counter
