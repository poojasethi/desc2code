import fileinput

def str_to_int(s):
	return([ int(x) for x in s.split() ])

# args = [ 'line 1', 'line 2', ... ]
def proc_input(args):
	(n, x, y) = str_to_int(args[0])
	inputs = []
	for l in args[1:]:
		inputs.append(int(l))
	return(n, x, y, inputs)

LOOKUP = []
def pre_proc(x, y):
	x = float(x)
	y = float(y)
	global LOOKUP
	x_counts = y_counts = 0
	while x_counts < x and y_counts < y:
		if((x_counts + 1) / x) > ((y_counts + 1) / y):
			LOOKUP.append('Vova')
			y_counts += 1
		elif((x_counts + 1) / x) < ((y_counts + 1) / y):
			LOOKUP.append('Vanya')
			x_counts += 1
		else:
			LOOKUP.append('Both')
			LOOKUP.append('Both')
			x_counts += 1
			y_counts += 1
	assert(len(LOOKUP) == x + y)

def solve(args, verbose=False):
	(n, x, y, inputs) = proc_input(args)
	pre_proc(x, y)
	global LOOKUP
	outputs = []
	for i in inputs:
		r = LOOKUP[(i - 1) % (x + y)]
		outputs.append(r)
		if verbose:
			print r
	return outputs

def test():
	assert(str_to_int('1 2 3') == [ 1, 2, 3 ])
	assert(solve([ '4 3 2', '1', '2', '3', '4' ], 1) == [ 'Vanya', 'Vova', 'Vanya', 'Both' ])

if __name__ == '__main__':
	from sys import argv
	if argv.pop() == 'test':
		test()
	else:
		solve(list(fileinput.input()), verbose=True)
