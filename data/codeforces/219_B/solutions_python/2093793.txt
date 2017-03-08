def count9(x):
	x = str(x)
	x = list(x)
	count = 0
	i = len(x) - 1
	while (x[i] == '9') and (i >= 0):
		count += 1
		i -= 1
	return count


k = raw_input('')
k = k.split()

d = int(k[0])
p = int(k[1])

maxcount = count9(d)
ans = d

str_d = str(d)
i = len(str_d) - 1

while (i > 0):
	str_d = list(str_d)
	str_d[i] = '9'
	if (int(str_d[i-1]) != 0):
		str_d[i-1] = str(int(str_d[i-1]) - 1)
	str_d = ''.join(str_d)
	if ( (int(str_d) >= d - p) and (int(str_d) <= d) ):
		ans = int(str_d)
	i -= 1

if (count9(ans) <= maxcount):
	print d
else:
	print ans