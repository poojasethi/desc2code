n = input()
a = [int(i) for i in raw_input().split()]
hashT = {}
for i in range(n):
	try:
		hashT[a[i]].append(i)
	except Exception, e:
		hashT[a[i]] = [i]
result = []
keys = hashT.keys()
keys = sorted(keys)
for key in keys:
	if len(hashT[key]) == 1:
		result.append((key, 0))
	else:
		i = 0
		diff = hashT[key][i+1] - hashT[key][i]
		while(i < len(hashT[key]) - 1):
			if (diff != (hashT[key][i+1] - hashT[key][i])):
				break
			i += 1
		if i == len(hashT[key])-1:
			result.append((key, diff))

print len(result)
for a,b in result:
	print a, b



