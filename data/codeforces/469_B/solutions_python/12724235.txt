p,q,l,r = [ int(x) for x in raw_input().split(' ') ]
def read_tuples(r):
	return [ ( int(l[0]), int(l[1]) ) for l in [ raw_input().split(' ') for i in range(r) ] ]
Z = read_tuples(p)
X = read_tuples(q) 

times = set()
for a,b in X:
	for c,d in Z:
		for e in range(max(c-b, l), min(d-a, r)+1):
			times.add(e)
print len(times) 

