# coding = utf-8
n = int(input())
a = map(int,raw_input().split())
i = 0
ans = 0
while i<n:
	if a[i]==1:
		while i<n and a[i]==1:
			i += 1
			ans += 1
		ans += 1
	else:
		i += 1
print [ans-1,0][ans-1<=0]