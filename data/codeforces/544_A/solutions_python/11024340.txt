
k = int(raw_input())
q = raw_input()

s = []

last = 0

letter_used = [False]*255

i = 0

while i < len(q):
	s.append(i)
	letter_used[ord(q[i])] = True
	while i < len(q) and letter_used[ord(q[i])]:
		i += 1
if k == 1:
	print "YES"
	print q

elif len(s) >= k:
	print "YES"
	for i in range(1,k):
		print q[s[i-1]:s[i]]
	print q[s[k-1]:]
else:
	print "NO"