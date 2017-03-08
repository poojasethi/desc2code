# 2012
# Maciej Szeptuch
# II UWr
import sys

data = sys.stdin.read().split("\n")
markers, caps = map(int, data[0].split())
data = data[1:]
result = 0
beautiful = 0
marker = [list() for i in range(1024)]
cap = [list() for i in range(1024)]
for m in range(markers):
	color, diameter = map(int, data[m].split())
	marker[diameter].append(color)

data = data[markers:]
for c in range(caps):
	color, diameter = map(int, data[c].split())
	cap[diameter].append(color)

for diameter in range(1024):
	m = 0; c = 0
	eM = len(marker[diameter]); eC = len(cap[diameter])
	result += min(eM, eC)
	marker[diameter].sort()
	cap[diameter].sort()
	while m < eM  and c < eC:
		if marker[diameter][m] < cap[diameter][c]:
			m += 1

		elif marker[diameter][m] > cap[diameter][c]:
			c += 1

		else:
			beautiful += 1
			c += 1
			m += 1

print result, beautiful
