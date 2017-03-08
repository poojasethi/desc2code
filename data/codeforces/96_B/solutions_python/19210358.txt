from itertools import permutations
n = raw_input()
sz = len(n)
if sz%2:
	sz += 1
	print '4'*(sz/2) + '7'*(sz/2)
	quit()
res = []
for i in range(1,5):
	res.extend([int(''.join(map(str,x))) for x in permutations('4'*i + '7'*i)])
res.append(int('4'*5 + '7'*5))
sorted(res)
for r in res:
	if r >= int(n):
		print r
		quit()