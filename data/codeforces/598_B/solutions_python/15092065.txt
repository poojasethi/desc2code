a = raw_input()

t = int(raw_input())


def rotate(target,k):
	k = k % len(target)							# abcdef = f + abcde
	return target[-k:] + target[:-k]


for x in xrange(0,t):
	l, r, k = map(int,raw_input().split())
	a = a[:l-1] + rotate(a[l-1:r],k) + a[r:]

print a