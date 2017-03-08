import fileinput, math

###          ###
# utility func #
###          ###

dbug = True

def pd(s, label=''):
	global dbug
	if dbug:
		header = 'debug:'
		if label != '':
			header += ' (%s)\t' % label
		print header, s

def stoi(s):
	return([ int(x) for x in s.split() ])

def perm(n, k, wheels=True):
	if wheels:
		assert(n > 0)
		assert(k > 0)
	return math.factorial(n) / math.factorial(k)

def comb(n, k, wheels=True):
	if wheels:
		assert(n > 0)
		assert(k > 0)
		assert(n - k > 0)
	return perm(n, k, False) / math.factorial(n - k)

def tol(actual, expected, tolerance=10 ** -9):
	if type(actual) != type([]):
		(actual, expected) = ([ actual ], [ expected ])
	r = [ expected[i] - tolerance <= actual[i] <= expected[i] + tolerance for i in xrange(len(actual)) ]
	return sum(r) == len(r)

def btod(b):
	return b * 2 - 1

def _sigma(f):
	return f * (f + 1) / 2

# sum(x from i to f)
def sigma(i, f, wheels=True):
	if wheels:
		assert(i >= 0)
		assert(f >= 0)
	return _sigma(f) - _sigma(i - 1)

def ps(l, wheels=True):
	if wheels:
		assert(len(l) > 0)
	r = [ l[0] ] * len(l)
	for i in xrange(1, len(l)):
		r[i] = l[i] + r[i - 1]
	return r

def test_utilities():
	assert(stoi('1 2 3\n') == [ 1, 2, 3 ])
	assert(stoi('') == stoi('\n') == [])
	assert(perm(10, 5) == 30240)
	assert(comb(10, 5) == 252)
	assert(tol(0.0, 0.0) == tol(0.0, 0.1, tolerance=0.1) == tol(0.0, 10, tolerance=10) == True)
	assert(tol(0.0, 0.1) == tol(0.0, 0.1, tolerance=0.1 - 10 ** -9) == False)
	assert(_sigma(1) == 1)
	assert(_sigma(10) == 55)
	assert(sigma(1, 10) == 55)
	assert(sigma(3, 10) == 52)
	assert(sigma(10, 10) == 10)
	assert(sigma(10, 11) == 21)
	assert(ps([ 1 ]) == [ 1 ])
	assert(ps([ 1, 2, 3, 4, 5 ]) == [ 1, 3, 6, 10, 15 ])
	assert(btod(0) == -1)
	assert(btod(1) == 1)

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	n = int(args[0])
	e = []
	c = []
	for l in args[1:n]:
		e.append(stoi(l))
	q = int(args[n])
	for l in args[n + 1:]:
		c.append(stoi(l))
	return(n, e, c)

from collections import defaultdict
adj_list = defaultdict(list)
CACHE = defaultdict(int)

# recursive DFS doesn't work so well in Python with recursion > 500
#	cf. http://codeforces.com/contest/500/submission/9334488
def dfs():
	is_visited = defaultdict(int)
	# build my own stack
	from collections import deque
	# calc subtree size, given root node and parent
	global adj_list, CACHE

	# build the order in which we will inspect the nodes
	o = []

	# scratch queue
	s = deque([ 1 ])
	while len(s):
		n = s.popleft()
		o.append(n)
		is_visited[n] = 1
		for c in adj_list[n]:
			if is_visited[c]:
				continue
			s.append(c)

	# and reverse order -- look at the leaves first
	o.reverse()
	for n in o:
		CACHE[n] = 1
		for c in adj_list[n]:
			# if c == p: CACHE[c] isn't computed yet, and thus adds nothing
			CACHE[n] += CACHE[c]

	return CACHE[1]

# credit to http://codeforces.com/contest/500/submission/9326111 and
#	http://codeforces.com/blog/entry/15488
def solve(args, verbose=False):
	global adj_list, CACHE
	adj_list = defaultdict(list)
	CACHE = defaultdict(int)
	(n, edges, changes) = proc_input(args)
	FAC = 3.0 / n / (n - 1)
	for (a, b, w) in edges:
		adj_list[a].append(b)
		adj_list[b].append(a)
	dfs()
	S = 0.0
	for (a, b, w) in edges:
		# find subtree
		n_A = min(CACHE[a], CACHE[b])
		# find nodes in the remaining tree
		n_B = n - n_A
		S += 2 * w * n_A * n_B
	results = []
	for (r, wp) in changes:
		(a, b, w) = edges[r - 1]
		edges[r - 1] = (a, b, wp)
		n_A = min(CACHE[a], CACHE[b])
		n_B = n - n_A
		S -= 2 * (w - wp) * n_A * n_B
		results.append(FAC * S)
	if verbose:
		for r in results:
			print r
	return results

def test():
	assert(solve([ '3', '2 3 5', '1 3 3', '5', '1 4', '2 2', '1 2', '2 1', '1 1' ], verbose=True) == [ 14, 12, 8, 6, 4 ])
	assert(tol(solve([ '6', '1 5 3', '5 3 2', '6 1 7', '1 4 4', '5 2 3', '5', '1 2', '2 1', '3 5', '4 1', '5 2' ], verbose=True), [ 19.6, 18.6, 16.6, 13.6, 12.6 ]))

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test_utilities()
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
