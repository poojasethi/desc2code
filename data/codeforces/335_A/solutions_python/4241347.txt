import sys


s = raw_input()
n = input()

d = [0] * 40
for i in s:
	d[ord(i) - 97] += 1

sn = len(filter(lambda x: x > 0, d))
		
if n < sn:
	print -1
else:
	for ans in xrange(1, len(s) + 1):
		tmp = 0
		for i in xrange(40):
			tmp += (d[i] + ans - 1) / ans
		if tmp <= n:
			cnt = 0
			print ans
			for i in xrange(40):
				for j in xrange ((d[i] + ans - 1) / ans):
					cnt += 1
					sys.stdout.write(chr(i + 97))
			while cnt < n:
				sys.stdout.write('a')
				cnt += 1
			break



			
		
