from sys import stdin
n, k = map(int, stdin.readline().split(" "))
ans = 0
for i in range(k):
	s = map(int, stdin.readline().split(" "))
	if s[0] == 1:
		continue
	if s[1] > 1:
		ans += s[0] - 1
	else: 
		j = 0
		while j < s[0]:
			if s[j + 1] != s[1] + j:
				break
			j += 1
		ans += s[0] - j

ans *= 2
ans += k - 1

print(ans)


