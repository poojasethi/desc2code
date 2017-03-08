n = int(raw_input())
a = raw_input()
b = raw_input()

mismatches = {}
num_mismatches = 0

for i in range(n):
	if (a[i] != b[i]):
		num_mismatches += 1
		t = (a[i], b[i])
		mismatches[t] = i + 1

for a, b in mismatches:
	if (b, a) in mismatches:
		print(num_mismatches - 2)
		print("%d %d" % (mismatches[(a, b)], mismatches[(b, a)]))
		exit(0)

for a, b in mismatches:
	for c in "abcdefghijklmnopqrstuvwxyz":
		if (c, a) in mismatches:
			print(num_mismatches - 1)
			print("%d %d" % (mismatches[(a, b)], mismatches[(c, a)]))
			exit(0)
		if (b, c) in mismatches:
			print(num_mismatches - 1)
			print("%d %d" % (mismatches[(a, b)], mismatches[(b, c)]))
			exit(0)

print(num_mismatches)
print("-1 -1")