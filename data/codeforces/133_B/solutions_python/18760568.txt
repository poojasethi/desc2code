hashT = {">": 1000, "<": 1001, "+": 1010, "-": 1011, ".": 1100, ",": 1101, "[": 1110, "]": 1111}
codes = raw_input()
final = ''
for c in codes:
	final += str(hashT[c])
print int(final, 2)%1000003