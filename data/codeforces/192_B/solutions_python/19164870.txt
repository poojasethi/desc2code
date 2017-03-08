n = input()
a = [int(i) for i in raw_input().split()]
m = 1001
for i in range(len(a)-1):
	minVal = max(a[i], a[i+1])
	if minVal < m:
		m = minVal
print min(a[0], m, a[-1])
