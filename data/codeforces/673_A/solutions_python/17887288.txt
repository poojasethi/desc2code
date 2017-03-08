num_intervals = int(raw_input())
times = [int(x) for x in raw_input().split()]
times.insert(0, 0)
val = 0
for i in xrange(1, len(times)):
	val = times[i]
	if times[i] - times[i-1] > 15:
		val = times[i-1]
		break

if val + 15 > 90: print 90
else:
	print val + 15