def solution(num_problems, num_similars):
	if num_similars == 0:
		return num_problems-1
	biggest_div_2 = None
	smallest_div_1 = None
	faulty = False
	for _ in xrange(num_similars):
		line = raw_input().split()
		big = max(int(line[0]), int(line[1]))
		small = min(int(line[1]), int(line[0]))
		if biggest_div_2 is None:
			biggest_div_2 = small
			smallest_div_1 = big
			continue
		if big <= biggest_div_2 or small >= smallest_div_1: 
			faulty = True
			break
		if big <= smallest_div_1:
			smallest_div_1 = big
		if small >= biggest_div_2:
			biggest_div_2 = small
	if faulty: return 0
	return smallest_div_1 - biggest_div_2

line = raw_input().strip().split()

num_problems = int(line[0])
num_similars = int(line[1])

print solution(num_problems, num_similars)
