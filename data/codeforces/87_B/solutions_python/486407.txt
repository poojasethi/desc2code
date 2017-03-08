#!/usr/bin/env python2

n = int(raw_input())
inf = -10000
M = {"void": 0, "errtype": inf}
for i in xrange(n):
	line = raw_input().split()
	s1 = line[0]
	s2 = line[1]
	if len(line) > 2: s3 = line[2]
	d = s2.count("*") - s2.count("&")
	s2 = s2.strip('*&')
	d += M.get(s2, inf)
	if d < 0: d = inf
	if s1 == "typedef":
		M[s3] = d
	else:
		if d < 0:
			print("errtype")
		else:
			print("void" + ('*' * d))
