def solve(strs):
	len = 1
	ss = ['']
	while 1:
		nss = []
		for s in ss:
			for i in range(97, 97+26):
				nss.append(s+chr(i))
		for s in nss:
			isOriginal = True
			for str in strs:
				if s in str:
					isOriginal = False
					break
			if isOriginal:
				return s
		ss = nss

import sys
rl = lambda: sys.stdin.readline()

n = int(rl())
strs = []
for i in range(n):
	strs.append(rl().strip())
print solve(strs)
