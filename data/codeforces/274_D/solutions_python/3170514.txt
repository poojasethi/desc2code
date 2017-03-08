n, m = map(int, raw_input().split())
b = [map(int, raw_input().split()) for _ in range(n)]
c = [n - x.count(-1) for x in zip(*b)]
d = []
for r in b:
	t = {}
	for i, x in enumerate(r):
		if x != -1:
			if x not in t:
				t[x] = set()
			t[x].add(i)
	d.append([x for i, x in sorted(t.items())][ : : -1])
p = [i for i, x in enumerate(c) if not x]
for v in d:
	if v:
		for x in v[-1]:
			c[x] -= 1
			if not c[x]:
				p.append(x)
r = []
while p:
	x = p.pop()
	r.append(x + 1)
	for i, v in enumerate(d):
		if v:
			v[-1].discard(x)
			if not v[-1]:
				d[i].pop()
				if d[i]:
					for y in d[i][-1]:
						c[y] -= 1
						if not c[y]:
							p.append(y)
print [-1, ' '.join(map(str, r))][len(r) == m]