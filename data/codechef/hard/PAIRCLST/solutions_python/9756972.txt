INFINITY = 10**9+7
from heapq import *
def dijkstra(s):
	global mini
	q, seen = [(0, s)], set()
	while q:
		cost, v1 = heappop(q)
		if v1 not in seen:
			seen.add(v1)
			if cost > mini:
				break
			if specials[v1] == 1:
				if v1 != s:
					mini = cost
					break
			for c, v2 in g[v1]:
				if v2 not in seen:
					heappush(q, (cost+c, v2))

N, M, K = map(int, raw_input().split())
A = map(int, raw_input().split())
specials = [-1 for _ in xrange(N+1)]
for a in A:
	specials[a] = 1
g = [[] for _ in xrange(N+1)]
for m in xrange(M):
	X, Y, Z = map(int, raw_input().split())
	g[X].append((Z, Y))
	g[Y].append((Z, X))
ds = []
mini = INFINITY
for i in xrange(1, K+1):
	dijkstra(A[i-1])
print mini