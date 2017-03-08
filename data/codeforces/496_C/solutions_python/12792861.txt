n,m = [ int(x) for x in raw_input().split(' ') ]
words = [ raw_input() for i in range(n) ]

def is_good(iterable):
	return tuple(iterable) == tuple(sorted(iterable))

from itertools import takewhile, izip, imap

good_cols = [ '' for _ in range(n) ]
count = 0
for col in izip(*words):
	candidate = list(imap(lambda x,y: x+y, good_cols,col))
	if is_good(candidate):
		good_cols = candidate
		count += 1

print m - count
