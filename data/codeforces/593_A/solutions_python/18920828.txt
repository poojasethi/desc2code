import string

letters = string.lowercase

a = []

n = input()
for _ in xrange(n):
	a.append(raw_input())

ans = 0

for l1 in letters:
	for l2 in letters:
		cur = 0
		if l1 != l2:
			for word in a:
				# if l1 in word or l2 in word:
					# print "set(word)",set(word), "set(l1,l2)",set([l1,l2])
				if set(word) == set([l1, l2]) or set(word) == set(l1) or set(word) == set(l2):
					# print "found one"
					cur += len(word)
		ans = max(cur, ans)
print ans
