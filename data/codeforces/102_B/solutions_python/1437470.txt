a = raw_input()
cnt = 0
while len(a) > 1:
	a = [int(i) for i in a]
	a = str(sum(a))
	cnt += 1
print cnt
