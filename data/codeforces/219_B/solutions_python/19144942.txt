p_original, d = map(int, raw_input().split())
p_disc = list(str(p_original))
m = p_original
for i in range(len(p_disc) - 1, 0, -1):
	if p_disc[i] == '9':
		pass
	else:
		p_disc[i] = 9
		# take carry
		j = i-1
		# print '--------------while loop starts----------'
		while (j >= 1 and p_disc[j] == '0'):
			p_disc[j] = str((int(p_disc[j]) - 1)%10)
			j -= 1

		if p_disc[j] != '0':
			p_disc[j] = str((int(p_disc[j]) - 1))

		# print '--------------while loop ends----------'

	# check if discount available
	p = int(''.join(map(str, p_disc)))
	if (p_original - p <= d):
		m = p
print m