import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	return(str_to_int(args[0]))

def is_possible(n, count_x, count_y, x, y):
	(n_fac_x, n_fac_y, n_fac_b) = (n / x, n / y, n / (x * y))
	n_free = n - n_fac_x - n_fac_y + n_fac_b
	(n_reserved_x, n_reserved_y) = (n_fac_y - n_fac_b, n_fac_x - n_fac_b)
	(n_remaining_x, n_remaining_y) = (max(0, count_x - n_reserved_x), max(0, count_y - n_reserved_y))
	return(n_remaining_x + n_remaining_y - n_free <= 0)

def solve(args, verbose=False):
	(count_x, count_y, x, y) = proc_input(args)
	(l, r) = (0, 10 ** 18)
	while(r - l > 1):
		m = (l + r) / 2
		if(is_possible(m, count_x, count_y, x, y)):
			# skimp off larger numbers
			r = m
		else:
			l = m
	if verbose:
		print r
	return r

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '3 1 2 3' ]) == 5)
	assert(solve([ '1 3 2 3' ]) == 4)

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
