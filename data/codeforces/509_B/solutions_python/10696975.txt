n, k = map(int, raw_input().split())

pebbles = [int(x) for x in raw_input().split()]


def check(pebbles):
	if max(pebbles) - min(pebbles) > k:
		return False
	return True


flag = check(pebbles)


def process(pebbles, flag):
	if not flag:
		print "NO"
	else:
		op = {x : [] for x in xrange(len(pebbles))}
		curr_color = 0
		done = False
		while not done:
			one = False
			for i in range(len(pebbles)):
				if pebbles[i] > 0:
					one = True
					op[i].append(str((curr_color % k) + 1))
					
					pebbles[i] -= 1
			curr_color += 1
			if not one:
				done = True
		print "YES"
		for i in range(len(pebbles)):
			print " ".join(op[i])

process(pebbles, flag)



