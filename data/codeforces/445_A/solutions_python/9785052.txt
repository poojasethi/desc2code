n, m = map(int, raw_input().split())

table = []

for i in range(n):
	table.append("")
	line = raw_input()
	for j in range(len(line)):
		if line[j] == ".":
			if (i + j) % 2 == 0:
				table[i] += "B"
			else:
				table[i] += "W"
		else:
			table[i] += line[j]

for lin in table:
	print lin
