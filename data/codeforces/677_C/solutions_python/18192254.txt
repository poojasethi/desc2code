import math 

modulo = pow(10, 9) + 7

def map_ch(ch):
	if ord(ch) >= 48 and ord(ch) <= 57:
		return ord(ch)-48
	if ord(ch) >= 97 and ord(ch) <= 122:
		return ord(ch)-61
	if ord(ch) >= 65 and ord(ch) <= 90:
		return ord(ch)-55
	if ch == '-': 
		return 62
	if ch == '_':
		return 63

word = raw_input().strip()

as_digits = [map_ch(ch) for ch in list(word)]

all_possible = range(64)

combinations = [0 for _ in xrange(64)]

for i in xrange(64):
	for j in xrange(64):
		combinations[i&j] += 1

total = 1
for digit in as_digits:
	total = (total * combinations[digit]) % modulo

print total

