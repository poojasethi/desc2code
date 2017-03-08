# coding =utf-8
n = input()
a = map(int,raw_input().split())
a0,a1,a2 = 0,0,0
chk = 1
for i in a:
	if i == 25:
		a0 += 1
	if i == 50:
		if a0>=1:
			a0 -= 1
			a1 += 1
		else:
			print 'NO'
			chk = 0
			break
	if i == 100:
		if (a0>=1 and a1>=1) or (a0>=3):
			if a1>=1:
				a1 -= 1
				a0 -= 1
				a2 += 1
			else:
				a2 += 1
				a0 -= 3
		else:
			print 'NO'
			chk = 0
			break
if chk:
	print 'YES'