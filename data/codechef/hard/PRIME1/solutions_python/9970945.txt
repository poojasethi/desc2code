from math import sqrt

def sieve():
	l[0] = False
	l[1] = False
	for i in xrange(2, limit + 1):
		if l[i]:
			prime.append(i)
			for j in xrange(i * i, limit + 1, i):
				l[j] = False

limit = int(sqrt(1000000000))
l = [True for x in xrange(limit + 1)]
prime = []
sieve()
#print len(prime)
#print prime

t = int(raw_input())
for i in xrange(t):
	m, n = map(int, raw_input().split())
	a = [True for x in xrange(m, n + 1)]
	for p in prime:
		#print p
		if p * p > n:
			break
		lo = (m / p) * p
		if lo < m:
			lo += p
		if lo == p:
			lo += p
		#print lo, m
		for j in xrange(lo, n + 1, p):
			a[j - m] = False
		#print a
	for j in xrange(m, n + 1):
		if a[j - m] and j != 1:
			print j
	print
