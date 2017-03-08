import itertools

n = int(raw_input())
m = int(raw_input())
ls = range(1, n + 1)
op = list(itertools.combinations(ls, m))
for t in op:
	for x in t:
		print x,
	print