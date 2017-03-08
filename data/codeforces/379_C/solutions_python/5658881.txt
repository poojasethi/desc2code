N = input()
a = sorted((y, x) for x, y in enumerate(map(int, raw_input().split())))
c = 0; b = [0]*N
for x, y in a:
	b[y] = c = max(c+1, x)
print ' '.join(map(str, b))
