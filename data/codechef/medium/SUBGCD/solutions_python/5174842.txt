"""
http://www.codechef.com/COOK50/problems/SUBGCD
"""
from fractions import gcd

def GCD(L) :
	"""GCD of list L. length of list L is at least 2."""
	ans = L[0]
	for i in xrange(1,len(L)) :
		ans = gcd(ans,L[i])
		if ans == 1 : break
	return ans

T = int(raw_input())
for _ in xrange(T) :
	N = int(raw_input())
	A = map(int,raw_input().split())
	ans = GCD(A)
	if ans > 1 :
		print -1
	else :
		print N

