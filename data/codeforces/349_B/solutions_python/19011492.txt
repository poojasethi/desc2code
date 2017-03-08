def main():
	v = input()
	w = [int(i) for i in raw_input().split()]
	w = [0] + w
	minValue = 1000000
	for i in range(1,len(w)):
		if w[i] <= minValue:
			minValue = w[i]
			minIdx = i
	if (minValue > v):
		print -1
		return
	# collect maximum digits
	ans = [[minValue, minIdx] for i in range(v/minValue)]
	residue = v - (v/minValue)*minValue
	# optimize left residue by updating ans values
	i = 0
	while (residue and i < len(ans)):
		for j in range(1,len(w)):
			maxVal = ans[i][1]
			if (w[j] <= residue + ans[i][0] and j > maxVal):
				residue = ans[i][0] + residue - w[j]
				ans[i][0] = w[j]
				ans[i][1] = j
				maxVal = ans[i][1]
		i += 1
	print ''.join(map(str,[ans[i][1] for i in range(len(ans))]))


if __name__ == '__main__':
	main()