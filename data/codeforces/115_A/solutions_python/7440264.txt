n = int(raw_input())
a = [0,]
b = [0 for i in range(n+1)]
for i in range(n):
	a.append(int(raw_input()))

maxCur = 0
for i in range(1,n+1):
	t = i
	cur = 1
	while a[t] != -1:
		b[t] = 1
		t = a[t]
		cur += 1
	if cur > maxCur:
		maxCur = cur

print maxCur