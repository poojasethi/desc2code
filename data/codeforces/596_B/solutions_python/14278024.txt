n = input()
a = map(int, raw_input().split())
last = 0
ans = 0
for i in range(n):
	ans+=abs(last-a[i])
	last=a[i]
print ans