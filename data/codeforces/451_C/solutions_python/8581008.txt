import math

t = int(raw_input())

for i in range(t):
	found = False
	tn = raw_input().split()

	if int(tn[0]) % 3 != 0:
		print "no"
		continue
	
	d1 = int(tn[2])
	d2 = int(tn[3])

	for i in range(-1,2,2):
		for j in range(-1,2,2):
			D1 = d1 * i
			D2 = d2 * j
			
			x2 = (int(tn[1]) - D1 + D2) / 3
			
			if (int(tn[1]) - D1 + D2) % 3 != 0:
				continue

			if x2 >= 0 and x2 <= int(tn[1]):
				x1 = D1 + x2
				x3 = x2 - D2			
				if x1 >= 0 and x3 >= 0 and x1 <= int(tn[1]) and x3 <= int(tn[1]):
					if x1 <= int(tn[0]) / 3 and x3 <= int(tn[0]) / 3 and x2 <= int(tn[0]) / 3:
						found = True

		if found and abs(x1 - x2) == d1 and abs(x2 - x3) == d2:
			break 

	if not found:
		print "no"
                continue

	print "yes"
