read_func = lambda:map(int, raw_input().split())

n, m = read_func()
groups = read_func()
buses = 0

while groups:
	max_limit = m
	
	while groups and max_limit >= groups[0]:
		max_limit -= groups.pop(0)
		
	buses += 1

print buses
