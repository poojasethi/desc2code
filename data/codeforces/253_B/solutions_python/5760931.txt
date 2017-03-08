import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

n = int(raw_input())
c = map(int, raw_input().split())
c.sort()
ans = n
i, j = 0, 0
while i < len(c):
	while j < len(c) and c[j] <= 2 * c[i]: j += 1
	ans = min(ans, n - (j - i))
	i += 1
print ans