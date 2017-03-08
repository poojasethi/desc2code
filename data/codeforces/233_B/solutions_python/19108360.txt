import math
n = input()
root = math.sqrt(n)
# print 'root: ', root
xUpper = math.floor(root) if math.floor(root) != root else math.floor(root) - 1
xUpper = list(str(int(xUpper)))
# find max s(x)
if (len(xUpper) >= 2):
	# check if already maximum
	maxS = sum(map(int, xUpper))
	maxS_new = int(xUpper[0]) - 1 + 9*(len(xUpper) - 1)
	maxS = maxS if maxS > maxS_new else maxS_new
else:
	maxS = sum(map(int, xUpper))
# print 'maxS: ', maxS
minNum = root
for s in range(1, maxS + 1):
	num = -s + math.sqrt(s**2 + 4*n)
	if (num%2 == 0 and num/2 < minNum and sum(map(int,list(str(int(num/2))))) == s):
		if (int(num/2)**2 + s*int(num/2) == n):
			minNum = num/2
print int(minNum) if minNum != root else -1