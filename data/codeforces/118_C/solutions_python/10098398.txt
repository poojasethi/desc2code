n, k = map(int, raw_input().split())
s = raw_input()

ORD = [
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 0, 3, 4, 5, 6, 7, 8, 9],
	[2, 3, 1, 4, 0, 5, 6, 7, 8, 9],
	[3, 4, 2, 5, 1, 6, 0, 7, 8, 9],
	[4, 5, 3, 6, 2, 7, 1, 8, 0, 9],
	[5, 6, 4, 7, 3, 8, 2, 9, 1, 0],
	[6, 7, 5, 8, 4, 9, 3, 2, 1, 0],
	[7, 8, 6, 9, 5, 4, 3, 2, 1, 0],
	[8, 9, 7, 6, 5, 4, 3, 2, 1, 0],
	[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
	]

DC = [0 for i in range(0, 10)]

for c in s:
	DC[int(c)] += 1

mdigit = -1
mcost = 1234567890
ms = ''
for i in range(0, 10):
	cost = 0
	rem = k
	ss = s
	for j in ORD[i]:
		diff = abs(i-j)
		pp = min(rem, DC[j])
		cost += pp*diff
		rem -= pp
		if j < i:
			ss = ss[::-1].replace(str(j), str(i), pp)[::-1]
		else:
			ss = ss.replace(str(j), str(i), pp)
	if mcost > cost or mcost == cost and ss < ms:
		mcost = cost
		mdigit = i
		ms = ss

print mcost
print ms
