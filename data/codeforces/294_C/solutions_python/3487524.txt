
def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret

MOD = 1000000007

def C(n, k): #n choose k
	ans = 1
	for i in range(k):
		ans = ans * (n - i)
		ans /= (i+1)
	return ans


def main():
	n, m = read_array(int)
	a = sorted(read_array(int))

	pow2 = [1]
	for i in range(1024):
		pow2.append((pow2[-1] * 2) % MOD)

	ans = 1
	l = 0
	for i in range(0, m):
		l2 = 0
		way = 1
		if i == 0:
			way = 1
			l2 = a[i] - 1
		else:
			l2 = a[i] - a[i-1] - 1
			if l2:
				way = pow2[l2 - 1]
			else:
				way = 1

		ans *= way * C(l2+l, l)
		ans %= MOD
		l += l2
		# print 'ans', ans, 'l', l, 'i', i, a[i]
		# print 'way', way, 'l2', l2

	if a[-1] != n:
		l2 = n - a[-1]
		way = 1

		ans *= way * C(l2 + l, l)
		ans %= MOD
		l += l2

	l += m
	# print l
	assert l == n

	print int(ans)


main()
