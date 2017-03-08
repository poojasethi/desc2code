a = map(int, raw_input());
cnt = [0] * 10;
c = [1869, 1968, 1689, 6198, 1698, 1986, 1896];
sz = len(a);

for i in xrange(sz):
	cnt[a[i]] += 1;
if cnt[0] == sz - 4:
	print "1869" + "0" * cnt[0];
else:
	cnt[1] -= 1;
	cnt[8] -= 1;
	cnt[6] -= 1;
	cnt[9] -= 1;
	res = 0;
	s = "";
	for i in xrange(9, -1, -1):
		s += str(i) * cnt[i];
		for j in xrange(0, cnt[i]):
			res = (res * 10 + i) % 7;
	print s + str(c[(7 - res * 10000 % 7) % 7]);

