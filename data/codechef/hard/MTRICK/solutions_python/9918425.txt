from collections import deque
def solve(n, l, a, B, c, string):
	b = deque(l)
	add = 0
	mult = 1
	for i,s in enumerate(string):
		if s == "R":
			for j in xrange(len(b)/2):
				b[j], b[len(b)-j-1] = b[len(b)-j-1], b[j]

		elif s == "A":
			add += a
		else:
			mult *= B
			add *= B
		# for j in xrange(len(b)):
		# 	b[j] %= c
		try:
			print (b.popleft()*mult + add)%c,
		except:break
	print
		
for _ in xrange(input()):
	n= input()
	l = map(int, raw_input().split())
	a, b, c = map(int, raw_input().split())
	s = raw_input()
	solve(n, l, a, b, c, s)