n = input()
v = [(map(int, raw_input().split())) for _ in range(n)]
v = sorted(v, key=lambda x: x[0], reverse=True)
v = sorted(v, key=lambda x: x[1], reverse=True)
counter = 1
points = 0
i = 0
while (i < n and counter > 0):
	counter += v[i][1] - 1
	points += v[i][0]
	i += 1
print points