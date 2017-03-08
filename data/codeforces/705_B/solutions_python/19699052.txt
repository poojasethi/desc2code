# input data
t = int(raw_input())
vertices = map(int, raw_input().split())

def solve(a):
	c = sum(a) - len(a)
	if c % 2 == 0:
		return 2
	else:
		return 1

c = 0
for v in vertices:
	c += v - 1
	if c % 2 == 0:
		print 2
	else:
		print 1
	
