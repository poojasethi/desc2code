import fileinput

###          ###
# utility func #
###          ###

dbug = True

def stoi(s):
	return([ int(x) for x in s.split() ])

def pd(s):
	global dbug
	if dbug:
		print 'dbug: ', s

###          ###
# code follows #
###          ###

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(_, l, x, y) = stoi(args[0])
	a = stoi(args[1])
	return(a, l, x, y)

def solve(args, verbose=False):
	(a, l, x, y) = proc_input(args)
	# a now in ascending order
	a.sort()
	s = set(a)
	x_found = y_found = False
	candidates = []
	for term in s:
		if term + x in s or term - x in s:
			x_found = True
		if term + y in s or term - y in s:
			y_found = True

	if not x_found:
		candidates.append(x)
	if not y_found:
		candidates.append(y)

	if not x_found and not y_found:
		for term in s:
			if term + x + y in s and term + x < l:
				candidates = [ term + x ]
			elif term + x - y in s and term + x < l:
				candidates = [ term + x ]
			elif term - x + y in s and term - x > 0:
				candidates = [ term - x ]
			elif term - x - y in s and term - x > 0:
				candidates = [ term - x ]
	if verbose:
		print len(candidates)
		print ' '.join([ str(x) for x in candidates ])
	return candidates

def test():
	assert(solve([ '3 250 185 230', '0 185 250' ]) == [ 230 ])
	assert(solve([ '4 250 185 230', '0 20 185 250' ]) == [])
	assert(solve([ '2 300 185 230', '0 300' ]) == [ 185, 230 ])
	assert(solve([ '4 300 4 5', '0 6 7 300' ]) == [ 11 ])
	assert(solve([ '4 300 4 5', '0 298 299 300' ]) == [ 295 ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		dbug = False
		solve(list(fileinput.input()), verbose=True)
