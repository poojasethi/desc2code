a = raw_input()
b = raw_input()
cnt_a, cnt_b = [0] * 26, [0] * 26
for i in xrange(len(a)):
	cnt_a[ord(a[i]) - ord('a')] += 1
for i in xrange(len(b)):
	cnt_b[ord(b[i]) - ord('a')] += 1
ans = 0
flag = 1
for i in xrange(26):
	if cnt_a[i] >= cnt_b[i]:
		ans += cnt_b[i]
	elif cnt_a[i] == 0 and cnt_b[i] != 0:
		flag = 0;
		break;
	else:
		ans += cnt_a[i]
print -1 if flag == 0 else ans