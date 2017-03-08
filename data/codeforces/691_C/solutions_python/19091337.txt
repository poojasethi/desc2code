import sys
ns = raw_input()

if not '.' in ns:
	ns = ns + '.'

i = 0
j = len(ns)-1

if set(ns) == set(['0']) or set(ns) == set(['.','0']) or set(ns) == set(['.']):
	print 0
	sys.exit(0)

while ns[i] == '0':
	i += 1
while ns[j] == '0':
	j -= 1

# print "ns:",ns
ns = ns[i:j+1]
# print "ns:",ns

if set(ns) == set(['0']) or set(ns) == set(['.','0']) or set(ns) == set(['.']):
	print 0
	sys.exit(0)

if ns[-1] == '.':
	base = ns[0]
	fract = ns[1:len(ns)-1]
	if fract:
		expo = len(fract)
		j = len(fract) -1
		while j >= 0 and fract[j] == '0':
			j -= 1
		fract = fract[:j+1]
		if fract:
			if expo == 0:
				print "%s.%s"%(base, fract)
			else:
				print "%s.%sE%d"%(base, fract, expo)
		else:
			if expo == 0:
				print base
			else:
				print "%sE%d"%(base, expo)
	else:
		print base

	sys.exit(0)

if ns[0] == '.':
	j = 0
	while ns[j] > '9' or ns[j] < '1':
		j += 1
	e = j
	if j == len(ns)-1:
		print "%sE%d"%(ns[j], -e)
	else:
		fract = ns[j+1:]
		k = len(fract) -1
		while k >= 0 and fract[k] == '0':
			k -= 1
		fract = fract[:k+1]
		print "%s.%sE%d"%(ns[j], fract, -e)
	sys.exit(0)
# print "ns:",ns
j = ns.index('.')
expo = j-1
base = ns[0]
fract = ns[1:j]+ns[j+1:]
if expo == 0:
	print "%s.%s"%(base, fract)
else:
	print "%s.%sE%d"%(base, fract, expo)