s = raw_input()
pre = -1; ans = 0
for i in xrange(len(s)-3):
	if s[i:i+4] == "bear":
		ans += (i-pre)*(len(s)-i-3)
		pre = i
print ans
