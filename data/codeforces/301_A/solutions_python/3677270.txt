INT_MIN = -1000000007

if __name__ == '__main__':
	n = int(raw_input())
	a = sorted([int(x) for x in raw_input().split()])
	res = INT_MIN
	for i in range(0, 2 * n, 2 - n % 2):
		res = max(res, sum([-x for x in a[:i]] + a[i:]))
	print(res)
