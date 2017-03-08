x, k = map(int, raw_input().split())
vis = []
flag = [0] * x;
for _ in xrange(k):
	a = map(int, raw_input().split())
	if a[0] == 1:
		vis.append(a[1])
		vis.append(a[2])
		flag[a[1]] = flag[a[2]] = 1
	else:
		vis.append(a[1])
		flag[a[1]] = 1
maximum = x - 1 - len(vis)
minimum = 0
for i in xrange(1, x):
	if flag[i] == 0:
		minimum += 1
		if i < x-1 and flag[i+1] == 0:
			flag[i+1] = 1
print minimum, maximum