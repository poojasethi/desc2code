N = int(raw_input())
arr = map(int,raw_input().strip().split(' '))
c = []
for i in range(2):
	m = max(arr)
	c.append(m)
	arr.remove(m)
print ' '.join(str(t) for t in c)