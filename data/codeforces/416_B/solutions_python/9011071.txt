mn = [int(x) for x in raw_input().split()]
m = mn[0]
n = mn[1]
resp = [0 for x in range(m)]
matrix = [[0 for x in range(n)] for y in range(m)]

for i in range(m):
	ent = [int(x) for x in raw_input().split()]
	for j in range(n):
		matrix[i][j]=ent[j]

for i in range(n):
	free = 0
	for j in range(m):
		begin = max(free,resp[j])
		resp[j] = begin+matrix[j][i]
		free=resp[j]

print ' '.join([str(x) for x in resp])
