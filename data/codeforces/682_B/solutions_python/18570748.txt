n = int(raw_input())
assert 1 <= n <= 1e5
A = map(int, raw_input().split())
A.sort()
j = 1
for a in A:
	if a >= j:
		j += 1
print j
