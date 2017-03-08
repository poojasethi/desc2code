from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	n = int(stdin.readline())
	a = stdin.readline().strip()
	if "I" in a:
		stdout.write("INDIAN\n")
	else:
		if "Y" not in a:
			stdout.write("NOT SURE\n")
		else:
			stdout.write("NOT INDIAN\n")