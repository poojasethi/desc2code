n = input ()
su, sd = 0, 0
eo, oe = False, False
for i in xrange (n):
	[a, b] = map (int, raw_input().split())
	su += a
	sd += b
	if a % 2 == 0 and b % 2 == 1:
		eo = True
	if a % 2 == 1 and b % 2 == 0:
		oe = True


if su % 2 == 0 and sd % 2 == 0:
	print 0
elif su % 2 == 1 and sd % 2 == 1:
	if eo or oe:
		print 1
	else:
		print -1
else:
	print -1
	
	
	
