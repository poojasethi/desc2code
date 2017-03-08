# your code goes here
from math import ceil, log
from sys import stdin, stdout
st = []
def getMid(s, e):
	return s + (e-s) / 2

def construct(st, arr, ss, se, si, type):
	if se == ss:
		if se%2 == type:
			st[si] = arr[ss]
		else:
			st[si] = 0
		return st[si]
	m = getMid(ss, se)
	st[si] = max(construct(st, arr, ss, m, si*2+1, type), construct(st, arr, m+1, se, si*2 + 2, type))
	return st[si]
		
def createSegTree(arr, type):
	st = [0] * (2 * (pow(2, int(ceil(log(len(arr))/log(2)))) - 1))
	construct(st, arr, 0, len(arr)-1, 0, type)
	return st
	
def getMaxUtil(st, ss, se, qs, qe, si):
	if qs <= ss and qe >= se:
		return st[si];
	if se < qs or ss > qe:
		return 0
	mid = getMid(ss, se)
	return max(getMaxUtil(st, ss, mid, qs, qe, 2 * si + 1),
    getMaxUtil(st, mid + 1, se, qs, qe, 2 * si + 2))

def getMax(st, n, qs, qe):
	if qs < 0 or qe > n-1 or qs > qe:
		return -1
	return getMaxUtil(st, 0, n-1, qs, qe, 0)
	
def updateUtil(st, ss, se, pos, val, si, type):
	if pos < ss or pos > se:
		return
	if ss == se:
		if pos%2 == type:
			st[si] = val
		return
	mid = getMid(ss, se)
	updateUtil(st, ss, mid, pos, val, 2*si+1, type)
	updateUtil(st, mid+1, se, pos, val, 2*si+2, type)
	st[si] = max(st[2*si+1], st[2*si+2])
	
def update(st, n, pos, val, type):
	updateUtil(st, 0, n-1, pos, val, 0, type)
	
n, q = map(int, stdin.readline().strip().split(' '))
arr = map(int, stdin.readline().strip().split(' '))
odd = createSegTree(arr, 1)
even = createSegTree(arr, 0)
while q:
	q -= 1
	c, l, r = map(int, stdin.readline().strip().split(' '))
	if c == 1:
		update(odd, n, l-1, r, 1)
		update(even, n, l-1, r, 0)
	else:
		stdout.write(str(getMax(odd, n, l-1, r-1) + getMax(even, n, l-1, r-1)) + "\n")