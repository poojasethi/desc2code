
n = input()

mis = 0
ch = 0

for i in xrange(n):
	x, y = map(int, raw_input().split())
	if x > y:
		mis += 1
	elif x < y:
		ch += 1

if mis > ch:
	print "Mishka"
elif mis < ch:
	print "Chris"
else:
	print "Friendship is magic!^^"