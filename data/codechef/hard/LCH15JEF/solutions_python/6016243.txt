import re
def solve(A, m):
	res = 1L
	for i in range(0, len(A), 2):
		res = (res * pow(A[i], A[i+1], m)) % m
	return res

if __name__ == '__main__':
	t = long(raw_input())
	for i in range(t):
		line = raw_input().strip()
		m, s = re.split(r'\s+', line, 1)
		m = long(m)
		A = map(long, re.split(r'\D+', s))
		print(solve(A, m))
