line = raw_input().strip().split()

num_ingrid = int(line[0])
magic_powder = int(line[1])

required = [int(x) for x in raw_input().split()]
has = [int(x) for x in raw_input().split()]

factor = has[0]/required[0]

for i in xrange(1, len(required)):
	if has[i]/required[i] < factor: factor = has[i]/required[i]

at_least = factor
state = [has[i]-required[i]*(factor+1) for i in xrange(len(has))]	
_sum = reduce(lambda x,y: x+y, [i for i in state if i < 0])

if _sum + magic_powder >= 0: 
	at_least += 1
	magic_powder += _sum
	state = map(lambda x: x if x > 0 else 0, state)
	while True:
		state = [state[i] - required[i] for i in xrange(len(has))]
		_sum = reduce(lambda x,y: x+y, [i for i in state if i < 0])
		if _sum + magic_powder >= 0: 
			at_least += 1
			magic_powder += _sum
			state = map(lambda x: x if x > 0 else 0, state)
		else: break
	print at_least
else:
	print at_least
